use std::{path::Path, str::FromStr};

use clap::Parser;
use uuid::Uuid;
use walkdir::WalkDir;

/// Simple program to greet a person
#[derive(Parser, Debug)]
#[clap(author, version, about, long_about = None)]
struct Args {
    /// Name of the person to greet
    #[clap(
        short,
        long,
        default_value = "F:\\Projects\\SC2DatasetPreparator\\processing\\directory_flattener\\input"
    )]
    input_directory: String,

    /// Number of times to greet
    #[clap(
        short,
        long,
        default_value = "../processing/directory_flattener/output"
    )]
    output_directory: String,

    #[clap(short, long, default_value = "SC2Replay")]
    file_extension: String,
}

fn main() {
    let args = Args::parse();

    println!(
        "Input Something! {}! Output {}!",
        args.input_directory, args.output_directory
    );

    // Iterate over the input directory
    for entry in WalkDir::new(&args.input_directory) {
        let entry = entry.unwrap();

        // This needs to be in here because the code that is ran later skips iterations:
        let mut main_input_dir = String::from("");
        if entry.depth() == 1 && entry.file_type().is_dir() {
            main_input_dir.push_str(entry.path().to_str().unwrap());
            println!("{}", main_input_dir);
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

            let mut my_uuid = Uuid::new_v4().to_simple().to_string();
            println!("{}", my_uuid);

            // let old_file_no_extension = old_file_w_extension.strip_suffix(&extension).unwrap();

            let mut extension_w_dot = String::from(".");
            extension_w_dot.push_str(&args.file_extension);
            my_uuid.push_str(&extension_w_dot);
            let output_path = Path::new(&args.output_directory).join(my_uuid);
            println!("{}", output_path.to_str().unwrap());
            continue;

            // std::fs::copy(entry.path(), to)

            // And save it to a directory mapping.
            // Save the directory mapping to drive.
        }
    }
}
