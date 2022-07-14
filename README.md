# dighum150a_demos
Exercises for DIGHUM150A
This repo contains demos and exercises for DIGHUM150A.

The program convertHeicToJpg.py requires that both the python library Wand and the package ImageMagick be installed.
If you are on a mac, you can download ImageMagick from here and install it:
https://imagemagick.org/script/download.php

If you are using your VM for the class, install it with the following command.

sudo apt-get install imagemagick

To install wand, you can use

pip install Wand

However, I recommand that you instead use the requirements.txt It has a list of all the Python libraries you need, and pip will get all of them for you, including Pillow, which you will need for the exif_data.py program. To use it, type the following commands.

python -m venv demoenv

source demoenv/bin/activate

pip -r requirements.txt
