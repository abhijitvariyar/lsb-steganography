from ImageProcessor import *
from Encoder import *

from Crypto.Random import get_random_bytes

if __name__ == "__main__":
    image = Image("img/test-image.jpg")

    print(f"Image size: {image.get_image_shape()}")

    # display_image_pixels(image)

    plain_text = "This is a password"

    # Use a cryptographically secure random key generator
    # The key must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes long
    encryption_key = get_random_bytes(32) # 256-bit key

    encoder = Encoder(encryption_key)

    ciphertext, tag, nonce = encoder.encrypt_msg(plain_text)

    bit_word_list, encoded_text = encoder.encode_msg(ciphertext)

    # Embed image with new binary encoded string
    embedded_image = embed_image(image, encoded_text)

    display_image_pixels(embedded_image)

    decoded_text = encoder.decode_msg(encoded_text)

    orig_msg = encoder.decrypt_msg(decoded_text, tag, nonce)
    print(f"orig_msg: {orig_msg.decode("utf-8")}")
