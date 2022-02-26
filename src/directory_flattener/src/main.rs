pub mod directory_flattener;
pub mod utils;

use clap::Parser;

fn main() {
    let args = directory_flattener::Args::parse();

    println!(
        "Input Something! {}! Output {}!",
        args.input_directory, args.output_directory
    );

    directory_flattener::directory_flattener(args);
}
