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
logging.disable(logging.CRITICAL)  # Note out to enable logging.
