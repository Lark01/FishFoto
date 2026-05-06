def saturation(image, saturation_value):
  saturation_value += 1

  # If image is RGBA
  if image.ndim == 4:
    image_rgb = color.rgba2rgb(image)

  # If image is RGB
  else:
    image_rgb = image

  image_hsv = color.rgb2hsv(image_rgb)
  image_hsv[:, :, 1] *= np.clip(saturation_value, 0, 2)

  result_image = color.hsv2rgb(image_hsv)
  result_image = np.clip(result_image, 0, 1) # Prevents a range warning.

  return result_image
