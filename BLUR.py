import cv2

# Load the image
image = cv2.imread('C:\\Users\\vamshi\\Desktop\\im_proj\\op\\plates\\scaned_img_2.jpg')

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 4)
cv2.imwrite("op/plates/input_img_" + ".jpg",blurred_image)
# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
