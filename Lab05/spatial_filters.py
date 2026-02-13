import cv2

def spatial_filter(img, noise_type):

    if noise_type == "salt_pepper":
        return cv2.medianBlur(img, 5)
    else:
        return cv2.GaussianBlur(img, (5, 5), 1.0)
