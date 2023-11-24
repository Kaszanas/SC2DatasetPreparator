from setuptools import setup, find_packages

PACKAGE_VERSION = "1.2.0"

PACKAGE_NAME = "sc2datasetpreparator"

DIRECTORY_FLATTENER = "directory_flattener"
FILE_PACKAGER = "file_packager"
FILE_RENAMER = "file_renamer"
JSON_MERGER = "json_merger"
PROCESSED_MAPPING_COPIER = "processed_mapping_copier"
SC2_MAP_DOWNLOADER = "sc2_map_downloader"
SC2_REPLAYPACK_PROCESSOR = "sc2_replaypack_processor"
setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    package_dir={"": "src"},  # Specify the root package directory
    packages=find_packages(where="src"),  # Locate packages under src
    install_requires=["Click"],
    extras_require={
        SC2_MAP_DOWNLOADER: ["sc2reader"],
        "all": ["sc2reader"],
    },
    entry_points={
        "console_scripts": [
            f"{DIRECTORY_FLATTENER} = {DIRECTORY_FLATTENER}:main",
            f"{FILE_PACKAGER} = {FILE_PACKAGER}:main",
            f"{FILE_RENAMER} = {FILE_RENAMER}:main",
            f"{JSON_MERGER} = {JSON_MERGER}:main",
            f"{PROCESSED_MAPPING_COPIER} = {PROCESSED_MAPPING_COPIER}:main",
            f"{SC2_MAP_DOWNLOADER} = {SC2_MAP_DOWNLOADER}:main",
            f"{SC2_REPLAYPACK_PROCESSOR} = {SC2_REPLAYPACK_PROCESSOR}:main",
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
