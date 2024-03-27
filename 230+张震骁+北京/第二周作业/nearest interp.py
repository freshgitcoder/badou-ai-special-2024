#实现最临近插值法，用作图片的上采样和下采样，用python实现

import cv2
import numpy as np

def image_zoom(org_img,new_h,new_w):    
    img_h = org_img.shape[0] #the image row num 
    img_w = org_img.shape[1] #the image column num
    
    if (new_h%2!=0) | (new_w%2!=0): #check the parameter
        print('parameter must be even') 
        try:
            (new_h%2!=0) | (new_w%2!=0)
        except 'parameter must be even':
        
    else:
        #emptyImage=np.zeros((new_h,new_w,channels),np.uint8) #create the empty image
        emptyImage=np.zeros((new_h,new_w,org_img.shape[2]),np.uint8) #create the empty image
        sh = new_h/img_h
        sw = new_w/img_w    
        
        for i in range(new_h):
            for j in range(new_w):
                x=int(i/sh + 0.5)  #int(),转为整型，使用向下取整。
                y=int(j/sw + 0.5)
                emptyImage[i,j]=org_img[x,y]
            
        return emptyImage    

img = cv2.imread("D:\source\lenna_gray.png", 1) #read the image
  
new_image = image_zoom(img,1001,1000)

cv2.imshow("image",new_image) # display the gray img
if cv2.waitKey(10000):
    cv2.destroyAllWindows()