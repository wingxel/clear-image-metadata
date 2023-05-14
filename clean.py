#!/usr/bin/python3

"""
Delete EXIF information from an image
https://wingxel.github.io/website.index.html
"""

import libs
import os


def main() -> None:
    """
    Remove EXIF info for each provided image
    :return:
    """
    provided_args = libs.get_args()
    for image_file in provided_args["images"]:
        if os.path.isdir(image_file):
            pass
        elif libs.is_image(image_file):
            libs.delete_exif_info(image_file, os.path.join())


if __name__ == '__main__':
    main()
