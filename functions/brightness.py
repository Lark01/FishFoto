def is_rgba(img):
    return img.ndim == 3 and img.shape[2] == 4
#returns min and max depending on type no image data, so 1-255 but the highest is 185, this returns 255
def get_absolute_limits(img):
    if np.issubdtype(img.dtype, np.integer):
        info = np.iinfo(img.dtype)
        return info.min, info.max
        
    elif np.issubdtype(img.dtype, np.floating):
        return 0.0, 1.0
    else:
        raise TypeError(f"Unexpected image data type: {img.dtype}")

#brightens image by different types
def brightenimage(img, intensity=1, maxintensity=10, type="simple"):
    
    if intensity > maxintensity:
        intensity = maxintensity
    elif intensity < 0.01:
        intensity = 0.01
        
    percentage = (intensity / maxintensity) * 100
    
    clip_min, clip_max = get_absolute_limits(img)
    fImg = img.astype(np.float32)
    
    if is_rgba(img):
        colors = fImg[:, :, :3]
        alpha = fImg[:, :, 3:]
    else:
        colors = fImg
    norm_colors = colors / clip_max
    #multiplying simple by 10 because it works differently
    if type == "simple":
        intensity*=10
        bright_colors = colors + intensity
    
    elif type == "log":
        c = clip_max / np.log1p(intensity)
        bright_colors = c * np.log1p(norm_colors * intensity)

    elif type == "exposure":
        bright_colors = colors * intensity
    #gamma
    elif type == "power":
        c=clip_max/np.power(clip_max, intensity)
        bright_colors=c*np.power(colors, intensity)
    # also inversed
    elif type == "exp":
        c = clip_max / np.expm1(intensity)
        bright_colors = c * np.expm1(norm_colors * intensity)

    if is_rgba(img):
        brightimage = np.concatenate((bright_colors, alpha), axis=-1)
    else:
        brightimage = bright_colors
        
    return np.clip(brightimage, clip_min, clip_max).astype(img.dtype), percentage