def autoAdjustment(image, max_stretch=3.5, correction_strength=1.5):
  # If image is RGBA
  if image.ndim == 4:
    image = color.rgba2rgb(image)

  # If image is grayscale
  elif image.ndim == 2:
    image = color.gray2rgb(image)

  lab_img = color.rgb2lab(image)
  l = lab_img[:, :, 0]

  mu = np.mean(l)   # Overall brightness
  sigma = np.std(l) # Overall contrast

  ideal_sigma = 22.0
  upper_sigma = 50.0

  # If contrast is low, adjusts it. Otherwise, stays the same.
  if sigma < ideal_sigma:
    alpha = min(ideal_sigma / (sigma + 1e-5), max_stretch)

  # If contrast is very high, reduces it. Otherwise, stays the same.
  elif sigma > upper_sigma:
    alpha = max_stretch

  else:
    alpha = 1.0

  target_mu = mu + (50.0 - mu) * correction_strength

  l_adjusted = alpha * (l - mu) + target_mu
  l_adjusted = np.clip(l_adjusted, 0, 100)

  lab_adjusted = lab_img.copy()
  lab_adjusted[:, :, 0] = l_adjusted
  adjusted_img = color.lab2rgb(lab_adjusted)

  return adjusted_img
