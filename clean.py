#!/usr/bin/python3

"""
Delete EXIF information from an image
https://wingxel.github.io/website.index.html
"""

import libs
import os


def delete_from_file(img_file: str, destination_folder: str, preserve: bool) -> None:
    """
    Helper function to main function
    :param img_file:
    :param destination_folder:
    :param preserve:
    :return:
    """
    destination_filename = libs.get_filename(img_file, preserve)
    libs.delete_exif_info(img_file, os.path.join(destination_folder, destination_filename))


def main() -> None:
    """
    Remove EXIF info for each provided image
    :return:
    """
    provided_args = libs.get_args()
    for image_file in provided_args["images"]:
        if os.path.isdir(image_file):
            for parent_dir, child_dirs, child_files in os.walk(image_file):
                for child_f in child_files:
                    img = os.path.join(parent_dir, child_f)
                    if libs.is_image(img):
                        delete_from_file(img, provided_args["destination_folder"], provided_args["preserve"])
        elif libs.is_image(image_file):
            delete_from_file(image_file, provided_args["destination_folder"], provided_args["preserve"])


if __name__ == '__main__':
    main()
