#! python3
# fix_and_extend.py — An exercise in using Pillow to edit image files.
# For more information, see project_details.txt.

import logging
import os
from PIL import Image

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.DEBUG)  # Note out to enable logging.

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"

logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size

os.makedirs("with_logo", exist_ok=True)

extension_list = ['.png', '.PNG', '.jpg', '.JPG', '.gif', '.GIF', '.bmp', '.BMP']

# Loop over all files in the working directory.
for filename in os.listdir("."):
    for extension in extension_list:
        if (
            not (filename.endswith(extension))
            or filename == LOGO_FILENAME
        ):
            continue
        logging.info(filename)
        img = Image.open(filename)
        width, height = img.size

    # Check if image needs to be resized.
        if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
            # Calculate the new width and hieght to be resized.
            if width > height:
                height = int((SQUARE_FIT_SIZE / width) * height)
                width = SQUARE_FIT_SIZE
            else:
                width = int((SQUARE_FIT_SIZE / height) * width)
                height = SQUARE_FIT_SIZE

            # Resize the image.
            print(f"Resizing {filename}")
            img = img.resize((width, height))

        # Add the logo.
        print(f"Adding logo to {filename} ...")
        img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

        # Save changes.
        img.save(os.path.join("with_logo", filename))
