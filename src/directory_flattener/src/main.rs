use std::str::FromStr;

use clap::Parser;
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

    #[clap(short, long, default_value = ".SC2Replay")]
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

        // Find all of the files:
        if entry.file_type().is_file() {
            let extension =
                String::from_str(entry.path().extension().unwrap().to_str().unwrap()).unwrap();
            // If the file extension matches then copy the file:
            if extension == args.file_extension {
                println!("Found a file with extension!")
            }
            println!("Found a file");
        }
        println!("{}", entry.path().display());
    }

    // TODO: If the path is a directory then go in

    // TODO: Walk through the directory

    // TODO: If the file extension matches the CLI extension then copy the file
    // And save it to a directory mapping.

    // Save the directory mapping to drive.
}
