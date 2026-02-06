Digital Image Processing – Chapter 3 Assignment
(Gonzalez & Woods)

Objective
---------
Apply intensity transformations, histogram processing and spatial filtering
operations to all images in a folder.

All images inside the "images" folder are processed automatically and the
results are stored in the "result" folder.

Folder structure
----------------
```
project/
│
├── images/
├── result/
│
├── part1_intensity.py
├── part2_histogram.py
├── part3_spatial.py
├── part4_mixed.py
└── run_all.py
```
How to run
----------
python run_all.py

Part 1 – Intensity Transformations
----------------------------------
- Log transformation
- Gamma correction (γ = 0.6, 0.4, 0.3, 3, 4, 5)
- Bit-plane slicing (0 to 7)

Part 2 – Histogram Processing
-----------------------------
- Global histogram equalization (manual implementation)
- Local histogram equalization using a 3×3 window (manual implementation)

Part 3 – Spatial Filtering
--------------------------
- Box (mean) filtering (3×3 and 5×5)
- Gaussian filtering
- Laplacian sharpening
- Unsharp masking

Part 4 – Mixed Spatial Enhancement
----------------------------------
Combination of:
- Laplacian operator
- Sobel gradient magnitude
- Gamma correction

Processing details
------------------
- All images are read from the "images" folder.
- All processing is done in grayscale.
- No built-in histogram equalization functions are used.
- Global and local histogram equalization are implemented manually.

Output
------
All results are saved in the existing folder:

result/
```
Output file naming format:
- <image>_log.png
- <image>_gamma_0.4.png
- <image>_bit_0.png ... <image>_bit_7.png
- <image>_hist_eq.png
- <image>_local_hist_eq.png
- <image>_box3.png
- <image>_box5.png
- <image>_gauss5.png
- <image>_laplacian.png
- <image>_unsharp.png
- <image>_mixed.png
```
Note
----
All output files are overwritten automatically if they already exist.
