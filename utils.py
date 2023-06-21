"""
Project utility functions
https://wingxel.github.io/website.index.html
"""

import argparse
from pathlib import Path
import os
from imghdr import what
import sys
from PIL import Image
import time


def get_default_folder() -> str:
    """
    Get the computer Pictures folder
    :return:
    """
    default_pictures_folder = os.path.join(str(Path.home()), "Pictures")
    if os.path.isdir("/sdcard/"):
        default_pictures_folder = "/sdcard/Pictures/no_exif"
    if not os.path.exists(default_pictures_folder):
        try:
            os.makedirs(default_pictures_folder)
        except Exception as error:
            sys.exit(f"Error creating folder {default_pictures_folder}\n{str(error)}")
    return default_pictures_folder


def get_args() -> dict:
    """
    Get commandline arguments
    :return:
    """
    parser = argparse.ArgumentParser(
        prog="clean.py",
        description="Delete image EXIF information",
        epilog="python3 clean.py -i image1 image2 image3 folder1 -d /home/user/Pictures -n 3"
    )

    parser.add_argument(
        "-n", "--num_procs", default=os.cpu_count(), type=int,
        help=f"Number of python processes to use, default is {os.cpu_count()} (recommended - number less "
             "or equal to number of cpu core available in your computer, if you "
             "set more that cpu_core_count the computer will freeze)"
    )

    parser.add_argument(
        "-i", "--image", nargs="+", required=True,
        help="Image file(s) to delete metadata or folder(s) containing images"
    )
    parser.add_argument(
        "-p", "--preserve", action="store_true",
        help="Preserve file names"
    )
    parser.add_argument(
        "-r", "--remove", action="store_true",
        help="Delete source/original image file"
    )
    parser.add_argument(
        "-d", "--destination", default=get_default_folder(),
        help=f"Destination folder to save cleaned images, default is {get_default_folder()}"
    )

    args = parser.parse_args()

    if os.path.exists(args.destination) and os.path.isfile(args.destination):
        sys.exit(f"{args.destination} is not a folder. -d or --destination should be a folder")

    if not os.path.exists(args.destination):
        try:
            os.makedirs(args.destination)
        except Exception as error:
            sys.exit(f"Failed to create directory {args.destination}\n{str(error)}")

    if args.num_procs > os.cpu_count():
        response = input(f"Using {args.num_procs} processes might freeze the computer continue? (y/n): ")
        if response.strip().lower() not in ["y", "yes", "continue"]:
            sys.exit(f"{response} - Aborted")

    return {
        "images": args.image,
        "destination_folder": args.destination,
        "preserve": args.preserve,
        "remove": args.remove,
        "num_procs": args.num_procs
    }


def delete_exif_info(input_image: str, destination_file: str, delete_original: bool) -> None:
    """
    Remove EXIF info and save the cleaned image
    :param delete_original: remove source file
    :param input_image: input image file
    :param destination_file: output image file
    :return:
    """
    try:
        with Image.open(input_image) as img:
            img_bytes = list(img.getdata())
            new_img = Image.new(img.mode, img.size)
            new_img.putdata(img_bytes)
            new_img.save(destination_file)
            new_img.close()
        if delete_original:
            print(f"{time.asctime(time.localtime())} - [deleting] - {input_image}")
            os.remove(input_image)
    except Exception as error:
        print(f"Error removing EXIF data for file {input_image}\n{str(error)}")


def is_image(input_file: str) -> bool:
    """
    Check if provided file is an image file
    :param input_file:
    :return:
    """
    return os.path.exists(input_file) and os.path.isfile(input_file) and what(input_file) is not None


def get_random_hex(length: int = 16) -> str:
    """
    Get a random hex to be used as file name
    :param length: byte size
    :return:
    """
    return os.urandom(length).hex()


def get_filename(abs_file_name: str, preserve: bool) -> str:
    """
    Get final filename for cleaned image
    :param abs_file_name: source file
    :param preserve: use hex or original filename
    :return:
    """
    destination_filename = str(os.path.basename(abs_file_name))
    if not preserve:
        destination_filename = f"{get_random_hex()}.{destination_filename.split('.')[-1]}"
    return destination_filename
