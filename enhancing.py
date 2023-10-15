import cv2
import os

# Create a new folder to save the clear images
if not os.path.exists('C:\\Users\\vamshi\Desktop\\im_proj\\final_img'):
    os.makedirs('C:\\Users\\vamshi\\Desktop\\im_proj\\final_img')

# Load the blur image\
image = cv2.imread('op/plates/scaned_img_2.jpg')
#cv2.imshow("result",image)
#cv2.waitKey(0) DISPLAYS THE IMAGE
# Apply Gaussian blur to reduce noise (optional)
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply image enhancement techniques (e.g., unsharp masking)
enhanced12 = cv2.addWeighted(image, 1,blurred, -0.5, 0)
# Save the enhanced image in the new folder
#cv2.imwrite('C:\Users\vamshi\Documents\plates\extracted_letters\clear')
cv2.imwrite("C:\\Users\\vamshi\\Desktop\\im_proj\\final_img\\img111.jpg",enhanced12)
