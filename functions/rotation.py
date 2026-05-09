from PIL import Image

def rotate_image(img_array, angle=0, maxrotate=360):
    #maximum or the num
    angle = max(0, min(angle, maxrotate))
    pil_img = Image.fromarray(img_array)
    rotated_pil = pil_img.rotate(angle, expand=True)
    return rotated_pil
