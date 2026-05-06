
def is_rgba(img):
    return img.ndim == 3 and img.shape[2] == 4
def get_absolute_limits(img):
    if np.issubdtype(img.dtype, np.integer):
        info = np.iinfo(img.dtype)
        return info.min, info.max
        
    elif np.issubdtype(img.dtype, np.floating):
        return 0.0, 1.0
    else:
        raise TypeError(f"Unexpected image data type: {img.dtype}")
#puts brightest to max and darkest to min
def contrast_stretch(img):
    clip_min, clip_max = get_absolute_limits(img)
    fImg = img.astype(np.float32)
    
    if is_rgba(img):
        colors = fImg[:, :, :3]
        alpha = fImg[:, :, 3:]
    else:
        colors = fImg
        
    c_min = colors.min()
    c_max = colors.max()
    
    if c_max-c_min==0:
        return img
    stretched_colors = (colors - c_min) * ((clip_max - clip_min) / (c_max - c_min)) + clip_min
    
    if is_rgba(img):
        stretched_image = np.concatenate((stretched_colors, alpha), axis=-1)
    else:
        stretched_image = stretched_colors

    return np.clip(stretched_image, clip_min, clip_max).astype(img.dtype)