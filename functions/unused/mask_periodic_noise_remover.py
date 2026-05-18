def mask_user_filter(image, center):
        #plan is:
        # user clicks on fourier transform -> get the coordinates of the click ->
        # apply a notch filter at that location
        if image.ndim == 3:
            hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv_image)
            
            denoised_v = mask_user_filter(v, center)
            
            denoised_v = np.clip(denoised_v, 0, 255).astype(np.uint8)
            denoised_hsv = cv2.merge((h, s, denoised_v))
            return cv2.cvtColor(denoised_hsv, cv2.COLOR_HSV2BGR)
        fft_result = np.fft.fft2(image)
        fft_shifted = np.fft.fftshift(fft_result)
        fft_shifted = notch_filter(fft_shifted, center)
        return np.fft.ifft2(np.fft.ifftshift(fft_shifted)).real
