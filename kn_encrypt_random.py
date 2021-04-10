import numpy as np
import cv2 as cv2
from util_conversion import decimal_to_binary as de2bi, binary_to_decimal as bi2de

def generate_random ( data , n , k ):
    data_bin=de2bi(data)
    n_randoms_bin = np.zeros((n, 8 ), np.uint8)
    n_randoms=[]
    for i in range ( 8 ):   
        if data_bin[i]== 1 :
            temp=np.random.permutation(n)[0:n-k+1]
            for j in range (n-k+1):
                n_randoms_bin[temp[j]][i]= 1
    for i in range (n):
        n_randoms.append(bi2de(n_randoms_bin[i]))
    return n_randoms

def kn_encrypt ( x , n , image ):
    shares=[]
    measures=image.shape
    if len (measures)== 3 :#for color image
        shares = np.zeros((n,measures[ 0 ], measures[ 1 ], measures[ 2 ]))
        for i in range (measures[ 0 ]):
            for j in range (measures[ 1 ]):
                for k in range (measures[ 2 ]):
                    n_randoms=generate_random(image[i][j][k],n,x)
                    for a in range (n):
                        shares[a][i][j][k]=n_randoms[a]
    elif len (measures)== 2 :#for black and white image
        shares = np.zeros((n,measures[ 0 ], measures[ 1 ]), np.uint8)
        for i in range (measures[ 0 ]):
            for j in range (measures[ 1 ]):
                n_randoms=generate_random(image[i][j],n,x)
                for a in range (n):
                    shares[a][i][j]=n_randoms[a]
    for i in range (n):
        ith_share = shares[i]
        cv2.imshow( 'Share_' + str (i), ith_share)
        cv2.imwrite( 'share_' + str (i)+ '.png' ,ith_share)
    
    return shares

if __name__ == "__main__":

    image = cv2.imread('lena512.tiff')
    image = cv2.resize(image, (64,64))
    kn_encrypt(2,4,image)
    if cv2.waitKey(0) & 0xff == 27:  
        cv2.destroyAllWindows()