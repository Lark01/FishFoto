def sobel_filter(image):
    if image.ndim == 3:
        processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        processed_image = image

    sobelx = cv2.Sobel(processed_image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(processed_image, cv2.CV_64F, 0, 1, ksize=3)

    magnitude = np.sqrt(sobelx**2 + sobely**2)
    magnitude = np.clip((magnitude / magnitude.max()) * 255, 0, 255).astype(np.uint8)
    
    return magnitude
