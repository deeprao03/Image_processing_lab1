import numpy as np
import cv2

def lowpass_frequency_filter(img, radius=30):

    img_f = img.astype(np.float32)

    dft = np.fft.fft2(img_f)
    dft = np.fft.fftshift(dft)

    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2

    mask = np.zeros((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), radius, 1, -1)

    dft_filt = dft * mask

    idft = np.fft.ifftshift(dft_filt)
    img_back = np.fft.ifft2(idft)
    img_back = np.abs(img_back)

    img_back = np.clip(img_back, 0, 255).astype(np.uint8)

    return img_back
