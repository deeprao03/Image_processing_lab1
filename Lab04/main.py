import numpy as np
import matplotlib.pyplot as plt
import os

from dft2d import dft2d
from basis import dft_basis_8x8_as_64x64

# Save + show helper (non-blocking, auto overwrite)


def save_and_show(filename):

    os.makedirs("Lab04/Result", exist_ok=True)

    plt.savefig(os.path.join("Lab04/Result", filename),
                bbox_inches="tight", dpi=150)

    plt.show(block=False)
    plt.pause(2)
    plt.close()


# Step 2 : Create binary rectangle image

def create_rectangle_image():

    img = np.zeros((64, 64))

    print("Enter top-left corner of rectangle")

    x0 = int(input("Row (x): "))
    y0 = int(input("Column (y): "))

    w = int(input("Width: "))
    h = int(input("Height: "))

    x1 = min(x0 + h, 64)
    y1 = min(y0 + w, 64)

    img[x0:x1, y0:y1] = 1

    return img


# Center image using (-1)^(x+y)

def center_image(img):

    M, N = img.shape
    centered = np.zeros_like(img, dtype=float)

    for x in range(M):
        for y in range(N):
            centered[x, y] = img[x, y] * ((-1) ** (x + y))

    return centered


# Show spectrum

def show_spectrum(F, title):

    mag = np.log(1 + np.abs(F))

    plt.figure(figsize=(5,5))
    plt.imshow(mag, cmap='gray')
    plt.title(title)
    plt.colorbar()

    fname = title.replace(" ", "_").replace("^", "").replace("(", "").replace(")", "")
    save_and_show(fname + ".png")


# Main

def main():

    # Step 1 : DFT basis
    dft_basis_8x8_as_64x64()

    # Step 2 : rectangle image
    img = create_rectangle_image()

    plt.figure(figsize=(4,4))
    plt.imshow(img, cmap='gray')
    plt.title("Original binary image")
    save_and_show("original_image.png")

    # Step 3 : DFT of original image
    print("Computing 2-D DFT (this may take time)...")

    F = dft2d(img)

    show_spectrum(F, "DFT of original image")

    # Step 4 : centered image and its DFT
    centered = center_image(img)

    plt.figure(figsize=(4,4))
    plt.imshow(centered, cmap='gray')
    plt.title("Centered image (-1)^(x+y)")
    save_and_show("centered_image.png")

    print("Computing 2-D DFT of centered image...")

    Fc = dft2d(centered)

    show_spectrum(Fc, "DFT of centered image")


if __name__ == "__main__":
    main()
