def blur_image(image, sigma, kernel_size):
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = kernel @ kernel.T
    blurred_image = cv2.filter2D(image, -1, kernel)
    return blurred_image
