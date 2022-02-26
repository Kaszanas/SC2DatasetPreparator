use clap::Parser;
use std::panic;
use walkdir::WalkDir;

use crate::utils;

#[derive(Parser, Debug)]
#[clap(author, version, about, long_about = None)]
pub struct Args {
    /// Input directory that will be walked and searched for replaypacks
    #[clap(
        short,
        long,
        default_value = "F:\\Projects\\SC2DatasetPreparator\\processing\\directory_flattener\\input"
    )]
    pub input_directory: String,

    /// Output directory where the files will be copied into a flat directory structure
    #[clap(
        short,
        long,
        default_value = "F:\\Projects\\SC2DatasetPreparator\\processing\\directory_flattener\\output"
    )]
    pub output_directory: String,

    /// File extension which will be used to detect the files that ought to be copied to a new flat directory structure
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
        // Iterating over all of the files and subdirectories of a replaypack:
        // TODO: Return output_dir_path from this:
        let copier_result = utils::file_copier(&input_replaypack, &args);

        // Save the directory mapping to the drive
        match copier_result.output_dir_path {
            Some(_) => (),
            None => {
                panic!("Could not create a directory mapping file! Found output_dir_path = None")
            }
        }

        utils::save_dir_mapping(
            copier_result.output_dir_path.unwrap(),
            copier_result.directory_mapping,
        );
    }
}
