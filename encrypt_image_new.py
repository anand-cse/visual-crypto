import numpy as np
from cv2 import cv2
import pywt
from Crypto.Cipher import AES
from keyGeneration import *    
        
def decrypt_AES(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def encrypt_AES(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(data)
    return ciphertext

def decryptBlockWise(imageData, key, iv):
    n,m,p=imageData.shape
    string=''
    string=imageData.tobytes()
    string=decrypt_AES(string, key, iv)
    index=0
    for i in range(0,n):
        for j in range(0,m):
            for k in range(p):
                imageData[i][j][k]=string[index]
                index=index+1
    return imageData

def encryptBlockWise(imageData, key, iv):
    n,m,p=imageData.shape
    string=''
    string=imageData.tobytes()
    string=encrypt_AES(string, key, iv)
    index=0
    for i in range(0,n):
        for j in range(0,m):
            for k in range(p):
                imageData[i][j][k]=string[index]
                index=index+1
    return imageData

if __name__ == "__main__":
    key="Hello I'm Encrypted key how shuold I encrypt for you"
    iv="Never the less I'm in here just give a glass"
    key=generate_key(16,key).tobytes()
    iv=generate_key(16,iv).tobytes()
    
    image_cv=cv2.imread('baboon.png')
    image_cv=cv2.resize(image_cv,(64,64))
    image_enc=encryptBlockWise(image_cv, key, iv)
    cv2.imshow('Encrypted', image_enc)
    cv2.imwrite('Encrypted.png', image_enc)
    
    # image_enc=cv2.imread('final.png')
    # image_dec=decryptBlockWise(image_enc, key, iv)
    # cv2.imshow('Decrypted', image_dec)
    # cv2.imwrite('Decrypted_0.png', image_dec)
    
    # print(cv2.PSNR(image_dec, image_cv))
    
    if cv2.waitKey(0) & 0xff == 27:  
        cv2.destroyAllWindows()  