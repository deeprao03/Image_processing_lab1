import numpy as np

def estimate_noise_type(img):

    img = img.astype(np.float32)

    med = np.median(img)
    diff = img - med

    high = np.mean(diff > 40)
    low  = np.mean(diff < -40)

    if high + low > 0.02:
        return "salt_pepper"

    return "gaussian"
