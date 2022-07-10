import argparse
import os.path
from PIL import ExifTags, Image


def getEXIF(filename):
    if not os.path.exists(filename):
        print(f"Can't Find File {filename}")
        return
    with Image.open(filename) as img:
        exif = img.getexif()
        if exif:
            print(f"Exif Data for {filename}")
            print("=========================")
            for k, v in exif.items():
                if k in ExifTags.TAGS:
                    tag = ExifTags.TAGS[k]
                    print(f"{tag}     =     {v}")
        else:
            print("No exif data, sorry!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Exif Data")
    parser.add_argument(
        "filename", help="An image file from which you want to get the exif data.")
    args = parser.parse_args()
    getEXIF(args.filename)
