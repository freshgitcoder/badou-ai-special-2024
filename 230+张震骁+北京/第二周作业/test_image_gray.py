#将指定图片三通道转为单通道灰度图，用python实现

import cv2

#img = cv2.imread("D:\source\lenna.png", 0) #read the image by gray mode
img = cv2.imread("D:\source\lenna.png", 1) #read the image

img_h = img.shape[0] #the image row num 
img_w = img.shape[1] #the image column num

img_gray = img  #copy the orignal image for gray img

for i in range(img_h):      #read every line
    for j in range(img_w):  #read the data in the line
        img_gray[i,j,0] = int((11*img_gray[i,j,0] + 59*img_gray[i,j,1] + 30*img_gray[i,j,2])/100) #change the gray
        img_gray[i,j,1] = img_gray[i,j,0]
        img_gray[i,j,2] = img_gray[i,j,0]
    #print(pix)

print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow("image",img_gray) # display the gray img
if cv2.waitKey(10000):
    cv2.destroyAllWindows()
cv2.imwrite("D:\source\lenna_gray.png",img_gray) # store the gray img







#print(img[0,0])


#print(img.shape)
#print(img.size)
#print(img.dtype)

#print(img_tmp[0,0])
#
#pix = img_tmp[0,0]
#print(pix)
#pix[0] = int((11*pix[0] + 59*pix[1] + 30*pix[2])/100)
#pix[1] = pix[0] 
#pix[2] = pix[0] 
#
#print(pix)




#cv2.imshow("image show gray",img_tmp)
#plt.subplot(221)


#print(img[0])
#print(img[0,0])
#h,w,d = img.shape

#printf('height = %d, width = %d, depth = %d'%h%w%d)
#printf('height = %d, width = %d, depth = %d',h)

