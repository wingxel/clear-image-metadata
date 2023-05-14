import argparse
from pathlib import Path
import os
from imghdr import what
import sys


def get_default_folder() -> str:
    """
    Get the computer Pictures folder
    :return:
    """
    default_pictures_folder = os.path.join(str(Path.home()), "Pictures")
    if not os.path.exists(default_pictures_folder):
        try:
            os.makedirs(default_pictures_folder)
        except Exception as error:
            print(f"Error creating folder {default_pictures_folder}\n{str(error)}")
    return default_pictures_folder


def get_args() -> dict:
    """
    Get commandline arguments
    :return:
    """
    parser = argparse.ArgumentParser(
        prog="clean.py",
        description="Delete image EXIF information",
        epilog="python3 clean.py -i image1 image2 image3 -d /home/user/Pictures"
    )

    parser.add_argument(
        "-i", "--image", nargs="+", required=True,
        help="Image file(s) to delete metadata"
    )
    parser.add_argument(
        "-d", "--destination", default=get_default_folder(),
        help="Destination folder to save cleaned images"
    )
    parser.add_argument(
        "-p", "--preserve", action="store_true",
        help="Preserve file names"
    )

    args = parser.parse_args()

    if os.path.exists(args.destination) and os.path.isfile(args.destination):
        sys.exit(f"{args.destination} is not a folder. -d or --destination should be a folder")

    if not os.path.exists(args.destination):
        try:
            os.makedirs(args.destination)
        except Exception as error:
            sys.exit(f"Failed to create directory {args.destination}\n{str(error)}")

    return {
        "images": args.image,
        "destination_folder": args.destination,
        "preserve": args.preserve
    }


def delete_exif_info(input_image: str, destination_file: str) -> None:
    """
    Remove EXIF info and save the cleaned image
    :param input_image: input image file
    :param destination_file: output image file
    :return:
    """
    pass


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
