import os
import cv2

from utils import read_gray, save_image
from noise_estimation import estimate_noise_type
from spatial_filters import spatial_filter
from frequency_filters import lowpass_frequency_filter
from metrics import psnr


# use your real folders (raw string!)
IMAGE_DIR  = r"D:\Image\Image_processing\Lab05\Images"
RESULT_DIR = r"D:\Image\Image_processing\Lab05\results"


def main():

    # ------------------------------------------------
    # reference image = 0.tif
    # ------------------------------------------------
    ref_path = os.path.join(IMAGE_DIR, "0.tif")
    ref = read_gray(ref_path)

    print("Reference image loaded")

    # ------------------------------------------------
    # process images 1 to 7
    # (images exist from 0 to 7, but 0 is reference)
    # ------------------------------------------------
    for i in range(1, 8):

        fname = f"{i}.tif"
        path = os.path.join(IMAGE_DIR, fname)

        img = read_gray(path)

        # resize if size is different (important for 7.tif)
        if img.shape != ref.shape:
            img = cv2.resize(img, (ref.shape[1], ref.shape[0]))

        noise_type = estimate_noise_type(img)

        print(f"{fname}  -> estimated noise: {noise_type}")

        # spatial domain filtering
        spatial_out = spatial_filter(img, noise_type)

        # frequency domain filtering
        freq_out = lowpass_frequency_filter(img)

        # PSNR
        psnr_spatial = psnr(ref, spatial_out)
        psnr_freq    = psnr(ref, freq_out)

        print(f"   Spatial PSNR   : {psnr_spatial:.2f} dB")
        print(f"   Frequency PSNR : {psnr_freq:.2f} dB")

        base = os.path.splitext(fname)[0]

        save_image(
            os.path.join(RESULT_DIR, base + "_spatial.png"),
            spatial_out
        )

        save_image(
            os.path.join(RESULT_DIR, base + "_frequency.png"),
            freq_out
        )

        report_path = os.path.join(
            RESULT_DIR, base + "_report.txt"
        )

        with open(report_path, "w") as f:
            f.write(f"Image        : {fname}\n")
            f.write(f"Noise type   : {noise_type}\n")
            f.write(f"Spatial PSNR : {psnr_spatial:.4f} dB\n")
            f.write(f"Freq PSNR    : {psnr_freq:.4f} dB\n")

    print("\nAll results saved in results folder.")


if __name__ == "__main__":
    main()
