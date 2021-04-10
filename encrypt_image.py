import numpy as np
import cv2
from keyGeneration import *
import pywt
def e_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = e_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modular_inv(a, p):
    gcd, x, y = e_gcd(a, p)
    if gcd != 1:
        raise Exception('Modular invers not possible')
    else:
        return x % p

def decryptBlockWise(imageData, key, iv, image):
    n,m,p=imageData.shape
    steps=4
    for i in range(0,n,steps):
        for j in range(0,m,steps):
            index=0
            res=[]
            for a in range(steps):
                for b in range(steps):
                    for k in range(p):
                        res.append(imageData[i+a][j+b][k])
                        imageData[i+a][j+b][k]=imageData[i+a][j+b][k]^key[index]
                        #imageData[i+a][j+b][k]=imageData[i+a][j+b][k]^iv[index]
                    index=index+1
            iv=res
    return imageData

def encryptBlockWise(imageData, key, iv):
    n,m,p=imageData.shape
    steps=4
    for i in range(0,n,steps):
        for j in range(0,m,steps):
            index=0
            res=[]
            for a in range(steps):
                for b in range(steps):
                    for k in range(p):
                        #imageData[i+a][j+b][k]=imageData[i+a][j+b][k]^iv[index]
                        imageData[i+a][j+b][k]=imageData[i+a][j+b][k]^key[index]     
                        res.append(imageData[i+a][j+b][k])
                    index=index+1
            iv=res
    return imageData

if __name__ == "__main__":
    key="Hello I'm Encrypted key how shuold I encrypt for you"
    iv="Never the less I'm in here just give a glass"
    key=generate_key(16,key)
    iv=generate_key(16,iv)
    # key=np.random.randint(256, size=256)
    # iv=np.random.randint(256, size=256)
    #np.savetxt('keys.txt',(key,iv))
    # print(key)
    # print(iv)
    
    image_cv=cv2.imread('peppers.png')
    image_enc=encryptBlockWise(image_cv, key, iv)
    cv2.imshow('Encrypted', image_enc)
    cv2.imwrite('Encrypted.png', image_enc)
    
    image_enc=cv2.imread('Encrypted.png')
    image_dec=decryptBlockWise(image_enc, key, iv, image_cv)
    cv2.imshow('Decrypted', image_dec)
    cv2.imwrite('Decrypted.png', image_dec)
    
    # print(cv2.PSNR(image_dec, image_cv))
    
    if cv2.waitKey(0) & 0xff == 27:  
        cv2.destroyAllWindows()  