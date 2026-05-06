# support RGB, RGBA, grayscale images
# according to https://towardsdatascience.com/image-processing-with-python-alternative-histogram-equalization-methods-c9088110b0ef/
# histogram equalization on RGB is not recommended
# thus we will equalize the V channel in HSV color space
def hist_equalization_helper(image):
    hist = np.bincount(image.flatten(), minlength=256)
    cdf = hist.cumsum()

    cdf_min = cdf[cdf > 0][0]
    total = image.size

    mapping = np.round((cdf - cdf_min) / (total - cdf_min) * 255)
    mapping = np.clip(mapping, 0, 255).astype(np.uint8)

    return mapping[image]

def hist_equalization(image):
    if(image.ndim == 2):
        return hist_equalization_helper(image)
    else:
        hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(hsv_image)
        equalized_v = hist_equalization_helper(v)
        equalized_hsv = cv2.merge((h, s, equalized_v))

        equalized_rgb = cv2.cvtColor(equalized_hsv, cv2.COLOR_HSV2RGB)
        return equalized_rgb
