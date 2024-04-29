# import required modules 
import cv2 
import matplotlib.pyplot as plt 
  
# read the image 
image = cv2.imread('emma.jpg') 
  
# convert color image into grayscale image 
img1 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 
  
# cmap stands for colormap 


flipped = cv2.flip(img1, 0)
plt.imshow(img1) 
plt.show()