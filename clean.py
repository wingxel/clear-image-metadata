#!/usr/bin/python3

"""
Delete EXIF information from an image
This will also help reduce the image size
https://wingxel.github.io/website.index.html
--------------------------------------------
"""

import utils
import os
import time
from concurrent.futures import ProcessPoolExecutor


def delete_from_file(
        img_file: str,
        destination_folder: str,
        preserve: bool,
        delete_source: bool
) -> None:
    """
    Helper function to main function
    :param img_file: source/original image
    :param destination_folder: destination folder to save cleaned files
    :param preserve: Preserve original file name
    :param delete_source: Delete original image
    :return:
    """
    print(f"{time.asctime(time.localtime())} - [cleaning] - {img_file}")
    destination_filename = utils.get_filename(img_file, preserve)
    utils.delete_exif_info(
        img_file,
        os.path.join(destination_folder, destination_filename),
        delete_source
    )


def main() -> None:
    """
    Remove EXIF info for each provided image
    :return:
    """
    provided_args = utils.get_args()
    # This uses multiple python processes to make the cleaning process fast
    # The number of processes launched will be determined by the number
    # available cpu cores
    # You can view the launched processes in any system monitor tool/software
    with ProcessPoolExecutor(max_workers=provided_args["num_procs"]) as executor:
        for image_file in provided_args["images"]:
            if os.path.isdir(image_file):
                for parent_dir, child_dirs, child_files in os.walk(image_file):
                    for child_f in child_files:
                        img = str(os.path.join(parent_dir, child_f))
                        if utils.is_image(img):
                            executor.submit(
                                delete_from_file,
                                img,
                                provided_args["destination_folder"],
                                provided_args["preserve"],
                                provided_args["remove"]
                            )
            elif utils.is_image(image_file):
                executor.submit(
                    delete_from_file,
                    image_file,
                    provided_args["destination_folder"],
                    provided_args["preserve"],
                    provided_args["remove"]
                )
            else:
                print(f"Error! Unknown file : the file {image_file} might not be an image.")


if __name__ == '__main__':
    main()
