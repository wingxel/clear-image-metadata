import argparse
from pathlib import Path
import os


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

    args = parser.parse_args()
    return {
        "images": args.image,
        "destination_folder": args.destination
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
    pass
