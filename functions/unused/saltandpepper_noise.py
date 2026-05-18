
def add_sp_noise(img, noise_ratio=0.1):
    if noise_ratio>1:
        noise_ratio=1
    if noise_ratio<0:
        noise_ratio=0

    noisy = img.copy()
    h, w = img.shape[:2]

    total_pixels = h * w
    noise_amount = int(total_pixels*noise_ratio)

    for i in range(noise_amount//2):
        r = random.randint(0, h-1)
        c = random.randint(0, w-1)
        if len(img.shape) == 2:
            noisy[r, c] = 255
        else:
            noisy[r, c] = [255] * img.shape[2]

    for i in range(noise_amount // 2):
        r = random.randint(0, h-1)
        c = random.randint(0, w-1)
        if len(img.shape) == 2:
            noisy[r, c]= 0
        else:
            noisy[r, c]=[0]*img.shape[2]

    return noisy