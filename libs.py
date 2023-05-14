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


def get_args():
    """
    Get commandline arguments
    :return:
    """
    parser = argparse.ArgumentParser(
        description="Delete image EXIF information",
        prog="clean.py"
    )

    parser.add_argument("-i", "--image", nargs="+", help="Image file(s) to delete metadata")
    parser.add_argument("-d", "--destination", help="Destination folder to cleaned images")
