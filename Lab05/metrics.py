import numpy as np

def psnr(img1, img2):

    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)

    mse = np.mean((img1 - img2) ** 2)

    if mse == 0:
        return 100.0

    return 10 * np.log10((255.0 * 255.0) / mse)
