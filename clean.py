#!/usr/bin/python3

"""
Delete EXIF information from an image
This will also help reduce the image size
https://wingxel.github.io/website.index.html
"""

import utils
import os
import time
from concurrent.futures import ThreadPoolExecutor


def delete_from_file(img_file: str, destination_folder: str, preserve: bool, delete_source: bool) -> None:
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
    utils.delete_exif_info(img_file, os.path.join(destination_folder, destination_filename), delete_source)


def main() -> None:
    """
    Remove EXIF info for each provided image
    :return:
    """
    provided_args = utils.get_args()
    executor = ThreadPoolExecutor(max_workers=4)
    for image_file in provided_args["images"]:
        if os.path.isdir(image_file):
            for parent_dir, child_dirs, child_files in os.walk(image_file):
                for child_f in child_files:
                    img = os.path.join(parent_dir, child_f)
                    if utils.is_image(img):
                        # delete_from_file(
                        #     img, provided_args["destination_folder"],
                        #     provided_args["preserve"], provided_args["remove"]
                        # )
                        executor.submit(
                            delete_from_file, img, provided_args["destination_folder"],
                            provided_args["preserve"], provided_args["remove"]
                        )
        elif utils.is_image(image_file):
            # delete_from_file(
            #     image_file, provided_args["destination_folder"],
            #     provided_args["preserve"],
            #     provided_args["remove"]
            # )
            executor.submit(
                image_file, provided_args["destination_folder"],
                provided_args["preserve"],
                provided_args["remove"]
            )
    executor.shutdown(wait=True)


if __name__ == '__main__':
    main()
