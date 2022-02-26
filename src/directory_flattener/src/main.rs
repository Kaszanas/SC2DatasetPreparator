pub mod replaypack_walker;

use clap::Parser;

fn main() {
    let args = replaypack_walker::Args::parse();

    println!(
        "Input Something! {}! Output {}!",
        args.input_directory, args.output_directory
    );

    replaypack_walker::directory_flattener(args);
}
