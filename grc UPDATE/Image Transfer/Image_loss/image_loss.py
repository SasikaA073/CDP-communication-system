#!/usr/bin/env python3
# image_loss.py  - calculates the loss of the image after transmission
# Author: Sasika Amarasinghe (amarasingheywsp.21@uom.lk)

from PIL import Image
import numpy as np
import os

try: 

    print("\n # Communication System - Image Loss Calculator")
    # Get the path of the current file
    file_path = os.path.realpath(__file__)
    file_path = file_path.split("\\")
    file_path.pop()
    file_path = "\\".join(file_path)

    # Open images 
    transmitted_image = Image.open(file_path + "\\" + "transmitted_image.jpg")
    received_image = Image.open(file_path + "\\"+ "received_image.jpg")

    # Get the mode of the image
    trans_img_mode = transmitted_image.mode

    
except Exception as e:
    print(e)

