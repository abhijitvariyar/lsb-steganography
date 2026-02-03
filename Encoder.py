from Crypto.Cipher import AES

from Log import Log

class Encoder:
    def __init__(self, key):
        self.key = key

# -----------------------------------------------------------------------------------------------------
    def encrypt_msg(self, msg):
        enc_cipher = AES.new(self.key, AES.MODE_GCM)

        ciphertext, tag = enc_cipher.encrypt_and_digest(msg.encode("utf-8"))
        ciphertext += b"\x00"

        # Log.log_info(f"Encrypted message: {msg}")

        return ciphertext, tag, enc_cipher.nonce

# -----------------------------------------------------------------------------------------------------
    @staticmethod
    def encode_msg(msg):
        bit_words = []

        # iterate through all characters in message
        for unicode_char in msg:
            word = ""

            # convert to binary
            while unicode_char > 0:
                bit = str(unicode_char % 2)
                word = bit + word
                unicode_char = unicode_char // 2

            if len(word) < 8:
                pad_len = 8 - len(word)
                word = ("0" * pad_len) + word

            bit_words.append(word)
        bit_str = ""

        for word in bit_words:
            bit_str += str(word)

        return bit_words, bit_str

# -----------------------------------------------------------------------------------------------------
    @staticmethod
    def decode_msg(msg):
        word_size = 8
        offset = 0
        decoded_msg = b""

        while True:
            ascii_val = 0
            for i in range(0, word_size):
                bit = int(msg[offset + i])
                ascii_val = ascii_val + bit * (2 ** (word_size - i - 1))

            if ascii_val == 0:
                return decoded_msg

            decoded_msg += chr(ascii_val).encode("latin-1")

            offset += word_size

# -----------------------------------------------------------------------------------------------------
    def decrypt_msg(self, msg, tag, nonce):
        dec_cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)

        plain_text = dec_cipher.decrypt(msg)
        try:
            dec_cipher.verify(tag)
            Log.log_success("Tag verified successfully")
        except ValueError:
            Log.log_error("Tag verification failed")

        return plain_text
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
