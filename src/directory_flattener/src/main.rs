use clap::Parser;

/// Simple program to greet a person
#[derive(Parser, Debug)]
#[clap(author, version, about, long_about = None)]
struct Args {
    /// Name of the person to greet
    #[clap(short, long, default_value = "./processing/directory_flattener/input")]
    input_directory: String,

    /// Number of times to greet
    #[clap(short, long, default_value = "./processing/directory_flattener/output")]
    output_directory: String,
}

fn main() {
    let args = Args::parse();

    println!(
        "Input Something! {}! Output {}!",
        args.input_directory, args.output_directory
    )

    // TODO: Iterate over the input directory

    // TODO: If the path is a directory then go in

    // TODO: Walk through the directory

    // TODO: If the file extension matches the CLI extension then copy the file
    // And save it to a directory mapping.

    // Save the directory mapping to drive.
}
