from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16)

def encryptData(msg):
    cipher = AES.new(key, AES.MODE_CCM)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decryptData(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_CCM, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False
    
# nonce, ciphertext, tag = encrypt(input('enter data:  '))
# plaintext = decrypt(nonce, ciphertext, tag)
# print(f'Cipher text:  {ciphertext}')
# if not plaintext:
#     print('error')
# else:
#     print(f'plain text: {plaintext}')
    