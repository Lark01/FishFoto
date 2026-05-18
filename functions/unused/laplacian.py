def laplacian_filter(image):
    if image.ndim == 3:
        processed_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        processed_image = image

    blurred = cv2.GaussianBlur(processed_image, (3, 3), 0)

    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

    laplacian = np.absolute(laplacian)

    laplacian = np.clip((laplacian / laplacian.max()) * 255, 0, 255).astype(np.uint8)
    
    return laplacian
