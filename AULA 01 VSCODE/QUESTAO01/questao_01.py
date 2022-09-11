import matplotlib
import numpy 
from PDI.src.pdi_utils import show_image
from skimage import data
from skimage.color import rgb2gray

# Load the rocket image
rocket = data.rocket()

# Convert the image to grayscale
gray_scaled_rocket = rgb2gray(rocket)

# Show the original image
show_image(rocket, 'Original RGB image')

# Show the grayscale image
show_image(gray_scaled_rocket, 'Grayscale image')
