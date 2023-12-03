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

    # Check if the mode indicates grayscale or RGB
    if trans_img_mode == 'RGB':
        print("\t- The transmitted image is in RGB mode.")
    elif trans_img_mode == 'L':
        print("\t- The transmitted image is in grayscale mode.")
    else:
        print(f"\t- The transmitted image is in mode: {trans_img_mode}")

    trans_width, trans_height = transmitted_image.size
    rec_width, rec_height = received_image.size

    print("\t- Size of the transmitted image: ", transmitted_image.size)
    print("\t- Size of the received image: ", received_image.size)

    # Check if the size of the images are equal
    if (trans_width, trans_height) != (rec_width, rec_height):
        print("\t- Images size mismatched. Please check the images.")

    else: 
        if trans_img_mode == "RGB":
            # Split the image into its red, green, and blue channels
            r_trans, g_trans, b_trans = transmitted_image.split()
            r_rec, g_rec, b_rec = received_image.split()

            # Convet image channels to numpy arrays
            r_trans_pix, g_trans_pix, b_trans_pix = np.array(r_trans), np.array(g_trans), np.array(b_trans)
            r_rec_pix, g_rec_pix, b_rec_pix = np.array(r_rec), np.array(g_rec), np.array(b_rec)

            r_diff = r_trans_pix - r_rec_pix
            g_diff = g_trans_pix - g_rec_pix
            b_diff = b_trans_pix - b_rec_pix

            r_loss = np.sum(r_diff ** 2)
            g_loss = np.sum(g_diff ** 2)
            b_loss = np.sum(b_diff ** 2)

            total_loss = r_loss + g_loss + b_loss


        elif trans_img_mode == "L":
            grayscale_trans_pix = np.array(transmitted_image)
            grayscale_rec_pix = np.array(received_image)

            total_loss = np.sum((grayscale_trans_pix - grayscale_rec_pix) ** 2)

    print("\t- Total loss of the image: ", total_loss)

except Exception as e:
    print(e)

