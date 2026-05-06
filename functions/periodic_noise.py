#returns min and max depending on type no image data, so 1-255 but the highest is 185, this returns 255
def get_absolute_limits(img):
    if np.issubdtype(img.dtype, np.integer):
        info = np.iinfo(img.dtype)
        return info.min, info.max
        
    elif np.issubdtype(img.dtype, np.floating):
        return 0.0, 1.0
    else:
        raise TypeError(f"Unexpected image data type: {img.dtype}")
def add_periodic_noise(image, noise_ratio=1.0, maxvalue=20):
    if noise_ratio > maxvalue:
        noise_ratio = maxvalue
    if noise_ratio < 0.1:
        noise_ratio = 0.1 

    h, w = image.shape[:2]
    img = image.astype(np.float32)

    y = np.arange(h).reshape(-1, 1)
    x = np.arange(w).reshape(1, -1)
    
    frequency = noise_ratio * 0.05
    
    wave = 30 * np.sin((x + y) * frequency)

    if is_rgba(img):
        colors = img[:, :, :3]
        alpha = img[:, :, 3:]
        wave_3d = wave[:, :, np.newaxis]
        noisy_colors = colors + wave_3d 
        noisy = np.concatenate((noisy_colors, alpha), axis=-1)
    elif img.ndim == 3:
        wave_3d = wave[:, :, np.newaxis]
        noisy = img + wave_3d
    else:
        noisy = img + wave 

    clip_min, clip_max = get_absolute_limits(image) 
    return np.clip(noisy, clip_min, clip_max).astype(image.dtype)