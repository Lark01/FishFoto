import math
import numpy as np
import cv2
from skimage.feature import peak_local_max

def dist_center(y, x, cx, cy):
    return math.sqrt( (x - cx)**2 + (y - cy)**2)
def band_reject_filter(image, W, n, noise_center):
    rows, cols = image.shape
    center_x, center_y = rows // 2, cols // 2
    
    D0 = np.sqrt((noise_center[0] - center_x)**2 + (noise_center[1] - center_y)**2)
    
    Y, X = np.ogrid[:rows, :cols]
    
    D = np.sqrt((Y - center_x)**2 + (X - center_y)**2)
    
    denom_term = (D * W) / ((D**2 - D0**2) + 1e-5) 
    
    H = 1 / (1 + np.power(denom_term, 2 * n))
    
    return image * H
def find_noise_frequencies_band_reject(noisy_image, min_distance=20, W = 10, n = 2):
    if noisy_image.ndim == 3:
        hsv_image = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        
        denoised_v = find_noise_frequencies_band_reject(v, min_distance, W, n)
        
        denoised_v = np.clip(denoised_v, 0, 255).astype(np.uint8)
        denoised_hsv = cv2.merge((h, s, denoised_v))
        return cv2.cvtColor(denoised_hsv, cv2.COLOR_HSV2BGR)
    fft_result = np.fft.fft2(noisy_image)
    fft_shifted = np.fft.fftshift(fft_result)
    
    mag_spec = np.abs(fft_shifted)
    mag_spec_copy = mag_spec.copy()
    
    imp_center = (mag_spec_copy.shape[0] // 2, mag_spec_copy.shape[1] // 2)
    mag_spec_copy[imp_center[0]-3:imp_center[0]+4, imp_center[1]-3:imp_center[1]+4] = 0
    threshold = np.mean(mag_spec_copy) + 2 * np.std(mag_spec_copy)
    peak_list = peak_local_max(mag_spec_copy, min_distance=min_distance, threshold_abs=threshold)
    for r, c in peak_list:
        fft_shifted = band_reject_filter(fft_shifted, W=W, n=n, noise_center=(r,c))
    result = np.fft.ifft2(np.fft.ifftshift(fft_shifted)).real
    return np.clip(result, 0, 255).astype(np.uint8)
