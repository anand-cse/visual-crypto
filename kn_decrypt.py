import numpy as np
import cv2 as cv2

def lagrange(j,x,k):
    final=[1,0]
    for m in range(k):
        if m != j:
            temp=np.polynomial.polynomial.polydiv((-1*x[m],1),(x[j]-x[m]))
            final=np.polynomial.polynomial.polymul(temp[0],final)
    #print(final)    
    return final
    

def linear_combination(x,y,k):
    pol=[0]
    for j in range(k):
        temp=np.polynomial.polynomial.polymul(lagrange(j, x, k),y[j])
        pol=np.polynomial.polynomial.polyadd(pol,temp)
    #print(pol)
    return pol

def reconstruct(shares,k,p):
    if len(shares) < k:
        raise Exception("Need more participants")
    x = [a for a, b in shares]
    y = [b for a, b in shares]
    return linear_combination(x, y, k)[0]%p

def kn_decrypt(k):
    im1=cv2.imread('Share_0.png')
    width,height,channels = im1.shape
    share=np.zeros((k,width, height,3),np.uint8)
    final=np.zeros((width, height,3),np.uint8)
    
    for i in range(k):
        x=cv2.imread('Share_'+str(i)+'.png')
        share[i]=x
    shares_local=[]

    for m in range(width):
        for n in range(height):
            for p in range(channels):
                for i in range(k):
                    shares_local.append((i+1,share[i][m][n][p]))
                final[m][n][p]=reconstruct(shares_local,k,256)
                shares_local=[]

    cv2.imshow('final',final)
    cv2.imwrite('final.png',final)

if __name__ == "__main__":
    kn_decrypt(2)
    if cv2.waitKey(0) & 0xff == 27:  
        cv2.destroyAllWindows()  