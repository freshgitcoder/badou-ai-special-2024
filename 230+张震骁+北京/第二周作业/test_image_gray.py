#将指定图片三通道转为单通道灰度图，进而传为二值化图像，用python实现

import cv2
import numpy as np

def color_to_gray(img):
    img_h = img.shape[0] #the image row num 
    img_w = img.shape[1] #the image column num
    
    img_gray = img  #copy the orignal image for gray img
    
    for i in range(img_h):      #read every line
        for j in range(img_w):  #read the data in the line
            img_gray[i,j,0] = int((11*img_gray[i,j,0] + 59*img_gray[i,j,1] + 30*img_gray[i,j,2])/100) #change the gray
            img_gray[i,j,1] = img_gray[i,j,0]
            img_gray[i,j,2] = img_gray[i,j,0]
        #print(pix)
    cv2.imshow("image",img_gray) # display the gray img
    if cv2.waitKey(10000):
        cv2.destroyAllWindows()
    return img_gray

def gray_to_binary(img): #by average way
    img_h = img.shape[0] #the image row num 
    img_w = img.shape[1] #the image column num
    
    img_bin = img  #copy the orignal image for gray img
    
    threshold = np.mean(img_bin)
    
    for i in range(img_h):      #read every line
        for j in range(img_w):  #read the data in the line
            if img_bin[i,j,0]>threshold:
                img_bin[i,j,0]=255
                img_bin[i,j,1]=255
                img_bin[i,j,2]=255
            else:
                img_bin[i,j,0]=0
                img_bin[i,j,1]=0
                img_bin[i,j,2]=0
        #print(pix)

    cv2.imshow("image",img_bin) # display the binary img
    if cv2.waitKey(10000):
        cv2.destroyAllWindows()
    return img_bin

#img = cv2.imread("D:\source\lenna.png", 0) #read the image by gray mode
img = cv2.imread("D:\source\lenna.png", 1) #read the image

img_gray = color_to_gray(img)

img_bin = gray_to_binary(img_gray)


