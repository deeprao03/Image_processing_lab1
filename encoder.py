import cv2
import numpy as np
import struct

SPATIAL = {0:100, 1:200, 2:400, 3:800}
BITDEPTH = {0:1, 1:2, 2:4, 3:8}

def load_crop(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    side = min(h, w)
    sh = (h-side)//2
    sw = (w-side)//2
    return img[sh:sh+side, sw:sw+side]

def quantize(img, bits):
    levels = 2**bits
    img = img/255
    img = np.round(img*(levels-1)).astype(np.uint8)
    return img

def encode(image_path, spatial_idx, bit_idx, outfile):
    img = load_crop(image_path)
    size = SPATIAL[spatial_idx]
    bits = BITDEPTH[bit_idx]

    img = cv2.resize(img, (size,size))
    imgq = quantize(img,bits)

    header = (spatial_idx << 2) | bit_idx

    with open(outfile,"wb") as f:
        f.write(struct.pack('B',header))
        f.write(imgq.tobytes())

    print(f"[ENCODE] Saved → {outfile}")
