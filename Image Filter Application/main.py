import cv2 # cv2 is the name of the library

image_path = './images/Tabby Cat.jpg'

# The files can be read in three different ways, each one will take information on a different way from the other
# cv2.IMREAD_COLOR means that OpenCV will take the file with color, but will not get the alpha channel of the image, which is the one used for transparency (such as PNG images)
# cv2.IMREAD_GRAYSCALE will get the image only on grayscale
# cv2.IMREAD_UNCHANGED will not make any type of modifications to the images, it will also include the alpha channel if there is one
color_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

if color_image is not None:
    print("Image successfully loaded. Image will be displayed shortly")

    # cv2.imshow will display the image, the first attribute will be the name of the window, and the second will be the actual image. The image has to be read beforehand using the cv2.imread function
    # waitKey with a value of 0 means the window won't close until the user presses a key, after that all the windows will be destroyed
    cv2.imshow("Tabby Cat", color_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error loading the image on {image_path}")