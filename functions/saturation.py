import numpy as np
from skimage import color

def saturation(image, saturation_value):
    multiplier = saturation_value + 1.0

    if image.dtype != np.uint8:
        image = (np.clip(image, 0, 1) * 255).astype(np.uint8)

    # Handle Alpha channel if present
    if image.ndim == 3 and image.shape[2] == 4:
        image_rgb = color.rgba2rgb(image)
    else:
        image_rgb = image

    # Process in HSV space
    image_hsv = color.rgb2hsv(image_rgb)
    image_hsv[:, :, 1] *= np.clip(multiplier, 0, 2)

    result_image = color.hsv2rgb(image_hsv)
    
    # Return as uint8 for OpenCV compatibility
    return (np.clip(result_image, 0, 1) * 255).astype(np.uint8)
