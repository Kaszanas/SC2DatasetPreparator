use std::io::Write;
use std::str::FromStr;
use std::{
    fs::File,
    path::{Path, PathBuf},
};
use uuid::Uuid;
use walkdir::WalkDir;

use crate::directory_flattener;

pub struct FileCopierResult {
    pub directory_mapping: serde_json::Map<String, serde_json::Value>,
    pub output_dir_path: Option<PathBuf>,
}

pub fn save_dir_mapping(
    output_dir_path: PathBuf,
    dir_mapping: serde_json::Map<String, serde_json::Value>,
) {
    let mut output_json = File::create(Path::new(&output_dir_path)).unwrap();
    let serialized_json = serde_json::to_string_pretty(&dir_mapping).unwrap();

    let wrote_json = write!(output_json, "{}", serialized_json);
    match wrote_json {
        Err(error) => panic!(
            "Something wrong happened! Received the following error {:?}",
            error
        ),
        Ok(_) => (),
    }
}

pub fn file_copier(
    input_replaypack: &PathBuf,
    args: &directory_flattener::Args,
) -> FileCopierResult {
    let mut directory_mapping = serde_json::Map::new();
    let mut replaypack_input_dir = PathBuf::new();

    let mut saved_output_path: Option<PathBuf> = None;

    for entry in WalkDir::new(input_replaypack.as_path()) {
        let entry = entry.unwrap();

        // This needs to be in here because the code that is ran later skips iterations:
        if entry.depth() == 0 && entry.file_type().is_dir() {
            replaypack_input_dir.push(
                entry
                    .path()
                    .file_name()
                    .and_then(|dir_name| dir_name.to_str())
                    .unwrap(),
            );
            println!("{}", replaypack_input_dir.display());
        }

        // The code's function is only to copy files so we skip directories:
        if entry.file_type().is_dir() {
            println!("Detected a dir");
            continue;
        }

        // The extension needs to be passed as an argument
        // So all of the files without extension are skipped:
        let os_extension = entry.path().extension();
        if os_extension.is_none() {
            println!("Detected that file had no extension");
            continue;
        }
        let unwrap_os_extension = os_extension.unwrap();
        let extension = String::from_str(unwrap_os_extension.to_str().unwrap()).unwrap();

        // The extension needs to match the supplied extension
        // All of the files with a different extension are skipped:
        if extension != args.file_extension {
            println!("Detected a wrong file extension");
            continue;
        }

        // All of the previous conditions were met.
        // Checking if the entry is a file and if the extension fits:
        if entry.file_type().is_file() && extension == args.file_extension {
            let old_filename = entry
                .path()
                .file_stem()
                .and_then(|stem| stem.to_str())
                .unwrap();

            println!("{}", old_filename);

            // Full parent entry path is required to find the relative path for the mapping:
            let full_parent_entry_path = entry
                .path()
                .parent()
                .and_then(|path| path.to_str())
                .unwrap();
            println!("{}", full_parent_entry_path);

            // This will be used in the mapping.
            // {"new_filename.extension": "old/relative/path/old_filename.extension"}
            let relative_entry_path = full_parent_entry_path
                .strip_prefix(&args.input_directory)
                .unwrap();
            println!("{}", relative_entry_path);

            let mut unique_id_filename = Uuid::new_v4().to_simple().to_string();
            println!("{}", unique_id_filename);

            let mut extension_w_dot = String::from(".");
            extension_w_dot.push_str(&args.file_extension);
            unique_id_filename.push_str(&extension_w_dot);

            let output_dir_path = saved_output_path
                .insert(Path::new(&args.output_directory).join(&replaypack_input_dir));

            println!("{}", output_dir_path.to_str().unwrap());

            let copy_to_path = output_dir_path.join(&unique_id_filename);
            println!("{}", copy_to_path.to_str().unwrap());

            let is_output_dir = std::fs::create_dir_all(&output_dir_path);
            match is_output_dir {
                Ok(output_path) => output_path,
                Err(error) => panic!(
                    "Could not create the directory! Received the following error {:?}",
                    error
                ),
            };

            let is_copied = std::fs::copy(entry.path(), copy_to_path);
            match is_copied {
                Err(error) => panic!(
                    "Could not copy the file! The following error was raised: {:?}",
                    error
                ),
                Ok(_) => (),
            }

            directory_mapping.insert(
                unique_id_filename,
                serde_json::Value::String(relative_entry_path.to_string()),
            );
        }
    }

    let result = FileCopierResult {
        output_dir_path: saved_output_path,
        directory_mapping,
    };

    return result;
}
