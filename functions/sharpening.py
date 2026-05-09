from PIL import Image, ImageFilter

def sharpening(image, radius=1, amount=1.0):
    return image.filter(ImageFilter.UnsharpMask(radius=radius, amount=amount))
