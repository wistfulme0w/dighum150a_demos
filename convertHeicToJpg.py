import argparse
import os.path
from webbrowser import get
from wand.image import Image

# This program takes a folder full of HEIC files and an output directory
# and converts them to jpgs, saving them in the directory.
# this program requires the ImageMagick program. Get it by typing
# sudo apt-get install imagemagick
# then, install the Python Library "wand" by typing
# pip install wand


def getOutgoingJpgPath(filename, outputdir):
    # get the bare filename of the heic file without the path
    # change the extension to jpg
    # add the new filename to tthe outgoing path.
    outgoingfilename = os.path.basename(filename)
    outgoingfilename = os.path.splitext(outgoingfilename)[0]
    outgoingfilename += ".jpg"
    return os.path.join(outputdir, outgoingfilename)


def convertToJpg(filestoconvert, outputdir):
    # for each file, use wand to convert the format of the file from
    # heic to jpg.

    for heic in filestoconvert:
        outgoingpath = getOutgoingJpgPath(heic, outputdir)
        print(f"Converting {heic} to {outgoingpath}")
        img = Image(filename=heic)
        img.format = 'jpg'
        img.save(filename=outgoingpath)
        img.close


if __name__ == "__main__":

    # Sets up a parser to get the arguments from the command line.
    parser = argparse.ArgumentParser(prog="HEIC Converter")
    parser.add_argument(
        "heicdir", help="a directory which has some heic files in it.")
    parser.add_argument(
        "outdir", help="A directory where you want the jpgs to be saved.")
    args = parser.parse_args()

    # if the specified output directory doesn't exist, try to make it.

    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    # gets all the HEIC files in the directory specified. Note: this does not recurse through
    # children directories.
    filestoprocess = []
    for file in os.listdir(args.heicdir):
        if file.endswith(".heic") or file.endswith(".HEIC"):
            filestoprocess.append(os.path.join(args.heicdir, file))
    convertToJpg(filestoprocess, args.outdir)
