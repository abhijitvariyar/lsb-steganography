import cv2
import numpy as np

from Log import *

class Image:
    def __init__(self, path):
        self.path = path
        self.img = cv2.imread(path)
        self.dtype = self.img.dtype

        assert self.img is not None, "No image found. Need to provide os.path if not in current directory"

        # print(f"Path: {self.path.split('/')[:-1]}")
        print(f"Path: {self.path[:(self.path.rfind('/') + 1)]}")

    def get_image(self):
        return self.img

    def get_image_shape(self):
        return self.img.shape

# def display_image(img: Image):
#     cv2.imshow("Image", img)
#     cv2.waitKey(0)

def embed_image(img: Image, msg: str):
    print(f"Embedding image with binary message: {msg}")

    image = img.get_image()
    image_shape = img.get_image_shape()
    max_msg_size = image_shape[0] * image_shape[1] * image_shape[2]

    if len(msg) > max_msg_size:
        Log.log_warning("Message is too long. Part of it will be truncated")

    end_of_msg = False

    char_ind = 0
    for row in range(image_shape[0]):
        for col in range(image_shape[1]):
            for colour in range(0, 3):
                bin_val = int(msg[char_ind])
                value = int(image[row][col][colour])

                new_val = (value + bin_val) if (value == 0) else (value - bin_val)

                image[row][col][colour] = new_val

                char_ind += 1

                if char_ind == len(msg):
                    # end_of_msg = True
                    # path = img.path.split('/')[:-1]
                    path = img.path[:(img.path.rfind('/') + 1)]
                    return image

    path = img.path.split('/')[:-1]


    return image

def display_image_pixels(img: np.ndarray):
    print("Display image pixels")

    row_count = 1
    image = img
    # for row in image:
    row = image[0]
    col_count = 1
    for col in row:
        print(f"row: {row_count} col: {col_count}\nG: {col[0]}\nB: {col[1]}\nR: {col[2]}")

def display_image(img: Image):
    print("Display image pixels")

    row_count = 1
    image = img.get_image()
    # for row in image:
    row = image[0]
    col_count = 1
    for col in row:
        print(f"row: {row_count} col: {col_count}\nG: {col[0]}\nB: {col[1]}\nR: {col[2]}")

