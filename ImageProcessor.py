import cv2
import numpy as np

from Log import *

class Image:
    def __init__(self, path):
        self.path = path
        self.img = cv2.imread(path)
        self.dtype = self.img.dtype

        assert self.img is not None, "No image found. Need to provide os.path if not in current directory"

    def get_image(self):
        return self.img

    def get_image_shape(self):
        return self.img.shape

    def show_image(self):
        cv2.imshow("Image", self.img)
        cv2.waitKey(0)

def embed_image(img: Image, msg: str):
    Log.log_info(f"Embedding image with binary message: {msg}")

    image = img.get_image().copy()

    image_shape = img.get_image_shape()
    max_msg_size = image_shape[0] * image_shape[1] * image_shape[2]

    image_dir = img.path[:(img.path.rfind('/') + 1)]
    file_name = img.path[(img.path.rfind('/') + 1): img.path.rfind('.')]
    file_type = img.path[img.path.rfind('.'):]

    new_img_file = image_dir + file_name + "-encrypted" + file_type

    if len(msg) > max_msg_size:
        Log.log_warning("Message is too long. Part of it will be truncated")

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
                    write_status = cv2.imwrite(new_img_file, image)
                    if write_status:
                        Log.log_success(f"Image successfully saved to {new_img_file}")
                    else:
                        Log.log_error(f"Image write failed")

                    return new_img_file

    return None

def extract_msg(img):
    Log.log_info(f"Extracting message from image: {img.path}")

    image = img.get_image()
    image_shape = img.get_image_shape()

    msg  = ""
    word = ""

    for row in range(image_shape[0]):
        for col in range(image_shape[1]):
            for colour in range(0, 3):
                value = int(image[row][col][colour])
                # Log.log_info(f"value: {value}")

                word += str(value)

                if len(word) == 8:
                    if word == "00000000":
                        msg += word
                        Log.log_info(f"Extracted message: {msg}")
                        return msg
                    else:
                        msg += word
                        word = ""

    return msg

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
    print("Display image")

    row_count = 1
    image = img.get_image()
    # for row in image:
    row = image[0]
    col_count = 1
    for col in row:
        print(f"row: {row_count} col: {col_count}\nG: {col[0]}\nB: {col[1]}\nR: {col[2]}")

