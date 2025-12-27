import cv2

class Image:
    def __init__(self, path):
        self.path = path
        self.img = cv2.imread(path)
        assert self.img is not None, "No image found. Need to provide os.path if not in current directory"

    def get_image(self):
        return self.img

def display_image(img: Image):
    cv2.imshow("Image", img)
    cv2.waitKey(0)

def display_image_pixels(img: Image):
    print("Hello World")

def string_to_bits(msg: str) -> list:
    bit_words = []

    # iterate through all characters in message
    for char in msg:
        ascii_val = ord(char)
        word = ""

        # convert to binary
        while ascii_val > 0:
            bit = str(ascii_val % 2)
            word = bit + word
            ascii_val = ascii_val // 2

        if len(word) < 8:
            pad_len = 8 - len(word)
            word = ("0" * pad_len) + word

        bit_words.append(word)

    return bit_words

def bin_encode_str(msg: str):
    bit_words = string_to_bits(msg)
    bit_str = ""


    for word in bit_words:
        bit_str += str(word)

    return bit_words, bit_str

def bin_decode_str(msg: str) -> str:
    word_size = 8

    if len(msg) % word_size != 0:
        print(f"MessageLengthError: \"utf-8\" encoded messages require message sizes to be multiples of 8")