import os.path

import cv2 # cv2 is the name of the library

image_path = './images/Tabby Cat.jpg'

# The files can be read in three different ways, each one will take information on a different way from the other
# cv2.IMREAD_COLOR means that OpenCV will take the file with color, but will not get the alpha channel of the image, which is the one used for transparency (such as PNG images)
# cv2.IMREAD_GRAYSCALE will get the image only on grayscale
# cv2.IMREAD_UNCHANGED will not make any type of modifications to the images, it will also include the alpha channel if there is one
color_image = cv2.imread(image_path, cv2.IMREAD_COLOR_BGR)

if color_image is not None:
    print("Image successfully loaded. Image will be displayed shortly")

    # cv2.imshow will display the image, the first attribute will be the name of the window, and the second will be the actual image. The image has to be read beforehand using the cv2.imread function
    # waitKey with a value of 0 means the window won't close until the user presses a key, after that all the windows will be destroyed
    cv2.imshow("Tabby Cat", color_image)

    """
    cvtColor's main use is to convert the color spaces of images (color space being the system of how colors are being represented), depending on what we want to do it may be necessary to implement a different type of color space to ensure both the best performance possible and the best results
    
    The main color spaces are
        - BGR, the default color space used in OpenCV
        - RGB, the most commonly used color space, also used in other important Python libraries
        - Grayscale, great when it comes to face, edge or feature detection. It can greatly improve the process of finding edges and features in images as OpenCV wont have to work with color
        - HSV, it is great when it comes to object tracking and color detection because it is not based only on colors in order to work, instead it is based also on the Saturation and the Brightness (Value). With this color space, instead of having to track multiple shades of color, only a certain color can be follow no matter the saturation or brightness
        
        Color shifts are completely normal when doing something like this as they will perform changes on the images information that may result in a change of the number of channels (loss of data) or a swap of the channels such as the BGR to RGB where the blue and red channels are swapped
    """
    grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY) # turn image into grayscale
    rgb_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB) # Turn into rgb
    hsv_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV) # turn into hsv

    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Display the converted images
    cv2.imshow("Grayscale Tabby Cat", grayscale_image)
    cv2.imshow("RGB Tabby Cat", rgb_image)
    cv2.imshow("HSV Tabby Cat", hsv_image)

    # Save the converted files using the imwrite method
    cv2.imwrite('./images/Grayscale Tabby Cat.jpg', grayscale_image)
    cv2.imwrite('./images/RGB Tabby Cat.jpg', rgb_image)
    cv2.imwrite('./images/HSV Tabby Cat.jpg', hsv_image)

    """
    cv2.GaussianBlur as the name clearly suggest is used in order to blur images, this is done by averaging pixel values, this means that for any given pixel, the new value of it will be calculated by getting the average of the neighboring pixel values, resulting in the image being smooth and reducing the sharp edges and overall details of the image
    
    In the case of the gaussian blur, pixels that are closer to the image will have more influence over the new value, therefore resulting in a more pronounced blu compared to the ones further away from the center that will have a reduced influence over the new value
    
    This process is made by making use of a matrix called kernel, this matrix will be in charge of calculating the new value of each pixel by sliding into every pixel and performing a convolution. The kernel makes use of weights which are determined by the gaussian function
    
    Overall this type of blur is much more smooth and natural looking when compared to the usual box blur
    
    The function will take certain parameters
        - The source file, in this case the image that will be blurred
        - Ksize, a tuple that will determine the size of the neighborhood of pixels that will be used to average. The numbers must always be positive and odd integers. A larger tuple will result in more intense blurs
        - SigmaX is the standard deviation of the gaussian factor in the x direction. When SigmaX is a larger value it will give more weight to the pixels that are farther away
        - SigmaY is the same as SigmaX, but in the Y axis, usually only SigmaX is used as OpenCV will also apply the value of SigmaX to SigmaY
    """

    gaussian_blur = cv2.GaussianBlur(color_image, (51, 51), 0) # Create a new image with gaussian blur

    cv2.imwrite('./images/Gaussian Tabby Cat.jpg', gaussian_blur)
    cv2.imshow("Gaussian Blur Tabby Cat", gaussian_blur)

    """
    cv2.Canny is more like a series of steps that will result in the detection of edges in the image. Overall the Canny Edge Algo is used to find the edges of images in a picture. An edge being a rapid change in the pixel intensity, the overall idea of the algo is to provide a line drawing of the edges of the object
    
    The first step in all of this is to set the image to grayscale, as cv2.Canny will work only with grayscale images
    
    The first part of the Canny algo is the noise reduction, this is very important part as images will often contain noise that can result in small and insignificant changes being mistaken for edges. The solution to this is making use of a blur such as the cv2.GaussianBlur as it will smooth the image and reduce a great amount of noise, therefore preventing false detentions
    
    The second part of this is to Identify the Intensity Gradients, here the algo will search where the pixels change in intensity and the direction where they change to. Here a Sobel Kernel is used in both horizontal and vertical directions with the purpose of providing two values for each pixel, a derivative in the x-direction called Gx and another one on the Gy (y-direction), these gradients will allow the algo to calculate the magnitude (how steep the change is) and the direction of the edge. The higher a magnitude is, the sharper the change was, therefore likely being an edge
    
    The third part, called Non-Maximum Suppression is focused on reducing the thickness of the edges as the previous step will usually result in a very thick edge detection, therefore the algo will iterate the pixels that were identified as edges, in each one it will check if the gradiant magnitude is the largest one of the neighbouring pixels in the direction of the gradient. If a pixel is the "local maximum" meaning the sharpest point in the edge, it will preserved, if not it will be suppressed
    
    The last part will take care again of possible edges created by noise, here the algo will decide what lines are actually edges or which ones are not, in this stage two different thresholds are used, a minimum value and a maximum value, if an edge is above the maximum value it will be considered a "sure-edge" or true edge and be preserved, if its under the minimum value it will be considered a non-edge and removed, it is between the two thresholds, it will only be kept if it is connected to a "sure-edge" otherwise it will be removed.
    
    It is important to properly select the thresholds as a low max value will result in more edges and more noise, and a high min value will result in fewer, but more prominent edges. It is always a good idea for the max value to be 2 or 3 times as big as the minimum value
    """

    grayscale_tabby = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(grayscale_tabby, (5, 5), 0)

    # cv2.Canny will take three params, the grayscale image, the minimum threshold and the maximum threshold
    edges = cv2.Canny(blur_img, 50, 150)
    cv2.imshow('Edges Tabby', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error loading the image on {image_path}")