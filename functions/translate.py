def translate_image(img_array, dx, dy):
    pil_img = Image.fromarray(img_array)
    translated = pil_img.transform(pil_img.size, Image.AFFINE, (1, 0, -dx, 0, 1, -dy))
    return translated
