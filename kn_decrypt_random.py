import numpy
import cv2 as cv2

def kn_decrypt ( k ):
    im1=cv2.imread( 'Share_0.png' )
    width,height,channels = im1.shape
    share=numpy.zeros((k,width, height, 3 ),numpy.uint8)
    final=numpy.zeros((width, height, 3 ),numpy.uint8)
    for i in range (k):
        x=cv2.imread( 'Share_' + str (i)+ '.png' )
        share[i]=x
    for i in range (k):
        final=final | share[i]
    cv2.imshow( 'final' ,final)
    cv2.imwrite( 'final.png' ,final)

if __name__ == "__main__":
    kn_decrypt(2)
    if cv2.waitKey(0) & 0xff == 27:  
        cv2.destroyAllWindows()  