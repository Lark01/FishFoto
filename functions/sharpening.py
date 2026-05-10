import cv2
import numpy as np
from PIL import Image, ImageFilter

def sharpening(image, radius=1, amount=1.0):
    # 1. Convert NumPy array to PIL Image
    if len(image.shape) == 3:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
    else:
        image_pil = Image.fromarray(image)

    # 2. Apply filter using 'percent' instead of 'amount'
    # We multiply amount by 100 because Pillow expects an integer percentage (e.g., 150 for 150%)
    sharpened_pil = image_pil.filter(
        ImageFilter.UnsharpMask(radius=radius, percent=int(amount * 100))
    )

    # 3. Convert back to NumPy array
    sharpened_np = np.array(sharpened_pil)

    # 4. Convert back to BGR if needed
    if len(image.shape) == 3:
        return cv2.cvtColor(sharpened_np, cv2.COLOR_RGB2BGR)
    
    return sharpened_np
