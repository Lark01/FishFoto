import numpy as np
import cv2
from skimage.feature import peak_local_max

def notch_filter(fft_shifted, center, size=6):
    r, c = center
    h = size // 2
    
    Y, X = np.ogrid[:fft_shifted.shape[0], :fft_shifted.shape[1]]
    dist_from_center = (Y - r)**2 + (X - c)**2
    
    mask = dist_from_center <= h**2
    fft_shifted[mask] = 0
    
    return fft_shifted

def find_noise_frequencies(noisy_image, min_distance=20):
    if noisy_image.ndim == 3:
        hsv_image = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        
        denoised_v = find_noise_frequencies(v, min_distance)
        
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
    temp = peak_local_max(mag_spec_copy, min_distance=min_distance, threshold_abs=threshold)
    rows, cols = fft_shifted.shape
    crow, ccol = rows // 2, cols // 2
    MIN_RADIUS = int(min(rows, cols) * 0.02)
    for r, c in temp:
        dist = (r - crow)**2 + (c - ccol)**2
    
        if dist < MIN_RADIUS**2:
            continue  
        fft_shifted = notch_filter(fft_shifted, (r, c), size = 6)
    
        sym_r = 2 * crow - r
        sym_c = 2 * ccol - c
        fft_shifted = notch_filter(fft_shifted, (sym_r, sym_c), size = 6)
        
    result = np.fft.ifft2(np.fft.ifftshift(fft_shifted)).real
    return np.clip(result, 0, 255).astype(np.uint8)
