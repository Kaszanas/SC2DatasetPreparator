use clap::Parser;
use serde_json::{Map, Value};
use uuid::Uuid;
use walkdir::WalkDir;

use std::{panic, path::Path, str::FromStr};

/// Simple program to greet a person
#[derive(Parser, Debug)]
#[clap(author, version, about, long_about = None)]
pub struct Args {
    /// Name of the person to greet
    #[clap(
        short,
        long,
        default_value = "F:\\Projects\\SC2DatasetPreparator\\processing\\directory_flattener\\input"
    )]
    pub input_directory: String,

    /// Number of times to greet
    #[clap(
        short,
        long,
        default_value = "../processing/directory_flattener/output"
    )]
    pub output_directory: String,

    #[clap(short, long, default_value = "SC2Replay")]
    pub file_extension: String,
}

pub fn directory_flattener(args: Args) {
    // Iterate over the depth 1 from input dir.
    // This accesses directories (replaypacks) that are within the input directory:
    let test_vec = WalkDir::new(&args.input_directory)
        .min_depth(1)
        .max_depth(1)
        .into_iter()
        .map(|dir_entry| dir_entry.unwrap().path().to_owned());

    // Iterating over all of the replaypacks that were found in the input directory:
    for input_replaypack in test_vec {
        let mut directory_mapping = Map::new();
        let mut replaypack_input_dir = String::from("");
        // Iterating over all of the files and subdirectories of a replaypack:
        for entry in WalkDir::new(input_replaypack) {
            let entry = entry.unwrap();

            // This needs to be in here because the code that is ran later skips iterations:
            if entry.depth() == 0 && entry.file_type().is_dir() {
                replaypack_input_dir.push_str(
                    entry
                        .path()
                        .file_name()
                        .and_then(|dir_name| dir_name.to_str())
                        .unwrap(),
                );
                println!("{}", replaypack_input_dir);
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

                // let old_file_no_extension = old_file_w_extension.strip_suffix(&extension).unwrap();

                let mut extension_w_dot = String::from(".");
                extension_w_dot.push_str(&args.file_extension);
                unique_id_filename.push_str(&extension_w_dot);

                let output_dir_path = Path::new(&args.output_directory).join(&replaypack_input_dir);

                println!("{}", output_dir_path.to_str().unwrap());

                let output_dir = std::fs::create_dir_all(&output_dir_path);
                match output_dir {
                    Ok(output_path) => output_path,
                    Err(error) => panic!(
                        "Could not create the directory! Received the following error {:?}",
                        error
                    ),
                };

                let is_copied =
                    std::fs::copy(entry.path(), output_dir_path.join(&unique_id_filename));
                match is_copied {
                    Err(error) => panic!(
                        "Could not copy the file! The following error was raised: {:?}",
                        error
                    ),
                    Ok(_) => (),
                }

                directory_mapping.insert(
                    unique_id_filename,
                    Value::String(relative_entry_path.to_string()),
                );
            }
        }
    }

    // iterate over all of the paths with walkdir with the alg that's already defined
}
