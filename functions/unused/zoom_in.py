def zoom_in(img, zoom=2):
    if zoom <= 1:
        return img

    h, w = img.shape[:2]
    crop_h, crop_w = h // zoom, w // zoom
    start_h = (h - crop_h) // 2
    start_w = (w - crop_w) // 2
    crop = img[start_h:start_h + crop_h, start_w:start_w + crop_w]
    result = cv2.resize(crop, (w, h))    
    return result