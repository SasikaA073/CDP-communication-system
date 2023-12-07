import argparse
import numpy as np
from PIL import Image

def calculate_image_loss(trans_img_path, rec_img_path):
    try:
        transmitted_image = Image.open(trans_img_path)
        width, height = transmitted_image.size # get the width and height

        received_image = Image.open(rec_img_path)

        trans_img_mode = transmitted_image.mode

        total_loss = 0

        if trans_img_mode == 'RGB':
            r_trans, g_trans, b_trans = transmitted_image.split()
            r_rec, g_rec, b_rec = received_image.split()

            r_trans_pix, g_trans_pix, b_trans_pix = np.array(r_trans), np.array(g_trans), np.array(b_trans)
            r_rec_pix, g_rec_pix, b_rec_pix = np.array(r_rec), np.array(g_rec), np.array(b_rec)

            r_diff = r_trans_pix - r_rec_pix
            g_diff = g_trans_pix - g_rec_pix
            b_diff = b_trans_pix - b_rec_pix

            r_loss = np.sum(r_diff ** 2)
            g_loss = np.sum(g_diff ** 2)
            b_loss = np.sum(b_diff ** 2)

            total_loss = r_loss + g_loss + b_loss
            mean_loss = total_loss / (3* width * height)

        elif trans_img_mode == 'L':
            grayscale_trans_pix = np.array(transmitted_image)
            grayscale_rec_pix = np.array(received_image)

            total_loss = np.sum((grayscale_trans_pix - grayscale_rec_pix) ** 2)

        return total_loss / (1 * width * height)

    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate image loss between two images.')

    parser.add_argument('trans_img_path', type=str, nargs='?', default='input.png', help='Path to the transmitted image')
    parser.add_argument('rec_img_path', type=str, nargs='?', default='output.png', help='Path to the received image')

    args = parser.parse_args()

    loss = calculate_image_loss(args.trans_img_path, args.rec_img_path)
    print(f"Total image loss: {loss}")
