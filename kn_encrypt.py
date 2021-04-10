import numpy as np
import cv2 as cv2
from util_conversion import decimal_to_binary as de2bi, binary_to_decimal as bi2de
from random import randrange
from random import randint
from numpy.polynomial import Polynomial as Poly

def generate_secrets(s,n,k,p):
    temp=[s]
    temp.extend(np.random.permutation(256)[0:k-1])
    shares=[]
    for i in range(n):
        shares.append((i+1,np.polynomial.polynomial.polyval(i+1, temp)%p))
    return shares


def kn_encrypt(x,n,image):
    shares=[]
    measures=image.shape
    if len(measures)==3:
        shares = np.zeros((n,measures[0], measures[1], measures[2]), np.uint8)
        for i in range(measures[0]):
            for j in range(measures[1]):
                for k in range(measures[2]):
                    n_randoms=generate_secrets(image[i][j][k],n,x,256)    
                    for a in range(n):
                        shares[a][i][j][k]=np.uint8(n_randoms[a][1])

    elif len(measures)==2:
        shares = np.zeros((n,measures[0], measures[1]), np.uint8)
        for i in range(measures[0]):
            for j in range(measures[1]):
                    n_randoms=generate_secrets(image[i][j],n,x,256)    
                    for a in range(n):
                        shares[a][i][j]=n_randoms[a]

    for i in range(n):
        ith_share = shares[i]
        cv2.imshow('Share_'+str(i), ith_share)
        cv2.imwrite('share_'+str(i)+'.png',ith_share)
    return shares
        
if __name__ == "__main__":

    image = cv2.imread('Encrypted.png')
    # image = cv2.resize(image, (64,64))
    kn_encrypt(2,4,image)
    if cv2.waitKey(0) & 0xff == 27:  
        cv2.destroyAllWindows()
