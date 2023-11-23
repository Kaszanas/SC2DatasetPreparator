from setuptools import setup

PACKAGE_VERSION = "1.2.0"

DIRECTORY_FLATTENER = "directory_flattener"
setup(
    name=DIRECTORY_FLATTENER,
    version=PACKAGE_VERSION,
    py_modules=[f"{DIRECTORY_FLATTENER}.py"],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [f"{DIRECTORY_FLATTENER} = {DIRECTORY_FLATTENER}:cli"]
    },
)

FILE_PACKAGER = "file_packager"
setup(
    name=FILE_PACKAGER,
    version=PACKAGE_VERSION,
    py_modules=[f"{FILE_PACKAGER}.py"],
    install_requires=["Click"],
    entry_points={"console_scripts": [f"{FILE_PACKAGER} = {FILE_PACKAGER}:cli"]},
)

FILE_RENAMER = "file_renamer"
setup(
    name=FILE_RENAMER,
    version=PACKAGE_VERSION,
    py_modules=[f"{FILE_RENAMER}.py"],
    install_requires=["Click"],
    entry_points={"console_scripts": ["script = script:cli"]},
)

JSON_MERGER = "json_merger"
setup(
    name=JSON_MERGER,
    version=PACKAGE_VERSION,
    py_modules=[f"{JSON_MERGER}"],
    install_requires=["Click"],
    entry_points={"console_scripts": [f"{JSON_MERGER} = {JSON_MERGER}:cli"]},
)

PROCESSED_MAPPING_COPIER = "processed_mapping_copier"
setup(
    name=PROCESSED_MAPPING_COPIER,
    version=PACKAGE_VERSION,
    py_modules=[f"{PROCESSED_MAPPING_COPIER}.py"],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            f"{PROCESSED_MAPPING_COPIER} = {PROCESSED_MAPPING_COPIER}:cli"
        ]
    },
)

SC2_MAP_DOWNLOADER = "sc2_map_downloader"
setup(
    name=SC2_MAP_DOWNLOADER,
    version=PACKAGE_VERSION,
    py_modules=[f"{SC2_MAP_DOWNLOADER}.py"],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [f"{SC2_MAP_DOWNLOADER} = {SC2_MAP_DOWNLOADER}:cli"]
    },
)

SC2_REPLAYPACK_PROCESSOR = "sc2_replaypack_processor"
setup(
    name=SC2_REPLAYPACK_PROCESSOR,
    version=PACKAGE_VERSION,
    py_modules=[f"{SC2_REPLAYPACK_PROCESSOR}"],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            f"{SC2_REPLAYPACK_PROCESSOR} = {SC2_REPLAYPACK_PROCESSOR}:cli"
        ]
    },
)

# For future scripts:

# setup(
#     name="",
#     version=PACKAGE_VERSION,
#     py_modules=[""],
#     install_requires=[""],
#     entry_points={"console_scripts": ["script = script:cli"]},
# )
