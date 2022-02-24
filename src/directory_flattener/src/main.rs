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
    for entry in WalkDir::new(args.input_directory) {
        let entry = entry.unwrap();

        if entry.file_type().is_dir() {
            println!("Detected a dir");
            continue;
        }

        let os_extension = entry.path().extension();
        if os_extension.is_none() {
            println!("Detected that file had no extension");
            continue;
        }
        let unwrap_os_extension = os_extension.unwrap();
        let extension = String::from_str(unwrap_os_extension.to_str().unwrap()).unwrap();

        if extension != args.file_extension {
            println!("Detected a wrong file extension");
            continue;
        }

        // Find all of the files:
        if entry.file_type().is_file() && extension == args.file_extension {
            // If the file extension matches then copy the file:

            let old_filename = entry
                .path()
                .file_stem()
                .and_then(|stem| stem.to_str())
                .unwrap();

            let mut my_uuid = Uuid::new_v4().to_simple().to_string();
            println!("{}", my_uuid);

            println!("{}", old_filename);
            // let old_file_no_extension = old_file_w_extension.strip_suffix(&extension).unwrap();

            let mut extension_w_dot = String::from(".");
            extension_w_dot.push_str(&args.file_extension);
            my_uuid.push_str(&extension_w_dot);
            let output_path = Path::new(&args.output_directory).join(my_uuid);
            continue;

            // std::fs::copy(entry.path(), to)

            // And save it to a directory mapping.
            // Save the directory mapping to drive.
        }
    }
}
