from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    """Encrypts data using AES-GCM mode."""
    cipher = AES.new(key, AES.MODE_GCM)

    # Encrypt and generate authentication tag
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))

    # Nonce, tag, and ciphertext are needed for decryption
    return cipher.nonce, tag, ciphertext

def display_encrypted_message(ciphertext, nonce, tag):
    print(f"Encrypted message components: Nonce={nonce.hex()}, Tag={tag.hex()}, Ciphertext={ciphertext.hex()}")

def decrypt(nonce, ciphertext, key):
    """Decrypts data and verifies integrity using AES-GCM mode."""
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    # Decrypt and verify the tag; will raise ValueError if corrupted
    plaintext = cipher.decrypt_and_verify(ciphertext)
    return plaintext.decode('utf-8')

def display_decrypted_message(decrypted_message):
    print(f"Decrypted message: {decrypted_message}")
