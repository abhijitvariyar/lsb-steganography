import sys
import cv2 as cv

from ImageProcessor import *
from Encryptor import *

if __name__ == "__main__":
    print(f"OpenCV version: {cv.__version__}")

    image = Image("img/test-image.jpg")

    # display_image(image.get_image())

    # display_image_pixels(image.get_image())

    message = "<Please enter the message to be encoded>"

    bit_words, bit_str = bin_encode_str(message)

    for word in bit_words:
        print(f"{word}")

    # print(f"length of message string: {len(msg)}")
    # print(f"length of bit_words: {len(bit_words)}")

    # AES ENCRYPTION -----------------------------------------------------------------------
    # # Use a cryptographically secure random key generator
    # # The key must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes long
    # encryption_key = get_random_bytes(32) # 256-bit key
    #
    # # Encrypt the message
    # nonce, tag, ciphertext = encrypt(message, encryption_key)   #, encryption_key)
    #
    # # Decrypt the message
    # decrypted_message = decrypt(nonce, ciphertext, encryption_key)
