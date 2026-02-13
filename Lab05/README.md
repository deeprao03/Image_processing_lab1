Image Denoising and Quality Evaluation
------------------------------------------------
Aim

For the given images (1.tif to 7.tif), estimate the noise type, apply appropriate spatial-domain and frequency-domain denoising filters, and evaluate the quality of the restored images using PSNR.

Image 0.tif is used as the reference (clean) image.

Folder Structure
```
Lab05/
│
├─ main.py
├─ utils.py
├─ noise_estimation.py
├─ spatial_filters.py
├─ frequency_filters.py
├─ metrics.py
│
├─ Images/
│   ├─ 0.tif
│   ├─ 1.tif
│   ├─ 2.tif
│   ├─ 3.tif
│   ├─ 4.tif
│   ├─ 5.tif
│   ├─ 6.tif
│   └─ 7.tif
│
└─ results/
```
Problem Description

For each image from 1.tif to 7.tif:

Estimate the type of noise present in the image.

Apply a suitable spatial-domain filter for denoising.

Apply a suitable frequency-domain filter for denoising.

Compute the PSNR (Peak Signal-to-Noise Ratio) of the denoised image with respect to the reference image 0.tif.

Methodology
Reference Image

0.tif is treated as the original (noise-free) reference image.

All quality measurements are computed with respect to this image.

Noise Type Estimation

A simple statistical heuristic is used:

The number of pixels having large deviation from the median intensity is computed.

If a significant proportion of extreme values is present, the noise is classified as salt-and-pepper noise.

Otherwise, it is classified as Gaussian noise.

This approach is sufficient for laboratory-level noise classification.

Spatial-Domain Denoising

Based on the estimated noise type:

Salt-and-pepper noise
→ Median filter (5 × 5)

Gaussian noise
→ Gaussian smoothing filter

Frequency-Domain Denoising

A low-pass filter is implemented in the frequency domain using the following steps:

Compute the 2-D FFT of the image.

Shift the spectrum to the center.

Apply a circular low-pass mask.

Perform inverse FFT to obtain the denoised image.

Image Size Handling

All images must have the same dimensions for PSNR computation.

If a noisy image has a different size than the reference image, it is resized to match the size of 0.tif before filtering and evaluation.

Quality Evaluation

The quality of the restored images is evaluated using PSNR:
```
𝑃
𝑆
𝑁
𝑅
=
10
log
⁡
10
(
255
2
𝑀
𝑆
𝐸
)
PSNR=10log
10
	​

(
MSE
255
2
	​

)
```
where MSE is the mean squared error between the reference image and the denoised image.

PSNR is computed separately for:

Spatial-domain filtered image

Frequency-domain filtered image

Output
```
For each input image (1.tif to 7.tif), the following files are generated in the results folder:

<index>_spatial.png – spatially denoised image

<index>_frequency.png – frequency-domain denoised image

<index>_report.txt – report containing:

```
estimated noise type

PSNR of spatial result

PSNR of frequency result

Example:

1_spatial.png
1_frequency.png
1_report.txt

How to Run

Place all images (0.tif to 7.tif) inside the Images folder.

Open a terminal in the Lab05 directory.

Run:
```
python main.py
```

All denoised images and PSNR reports will be saved in the results folder.

Important Notes

Image 0.tif is not denoised; it is used only as the reference image.

PSNR values are meaningful only when the noisy image corresponds to the same scene as the reference image.

One of the test images (7.tif) has a different resolution and content. It is resized to the reference size before PSNR computation, which may affect its PSNR value.

Conclusion

The program successfully estimates the noise type for each given image, applies suitable spatial and frequency-domain filters, and evaluates the denoising performance using PSNR.