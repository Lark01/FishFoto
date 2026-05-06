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

#linear contrasting on an image
def contrastimage(img, intensity=1,maxintensity=250):
    
    if intensity>maxintensity:
        intensity=maxintensity
    elif intensity<0.01:
        intensity=0.01
    percentage=(intensity/maxintensity)*100

    #function : x-mean*intesity+mean
    fImg = img.astype(np.float32)
    if is_rgba(img):
        colors=fImg[:, :, :3]
        alpha=fImg[:, :, 3:]
        mean_val = colors.mean(axis=(0, 1)) 
        cc = (colors-mean_val)*intensity+mean_val
        contrasted = np.concatenate((cc, alpha), axis=-1)
        
    else:
        mean_val = fImg.mean(axis=(0, 1))
        contrasted = (fImg-mean_val)*intensity+mean_val
        
    return np.clip(contrasted,get_absolute_limits(img)[0],get_absolute_limits(img)[1]).astype(img.dtype), percentage