import numpy as np
import struct
import cv2

SPATIAL = {0:100, 1:200, 2:400, 3:800}
BITDEPTH = {0:1, 1:2, 2:4, 3:8}

def decode(infile):
    with open(infile,"rb") as f:
        header = struct.unpack('B', f.read(1))[0]
        sidx = (header >> 2) & 3
        bidx = header & 3

        size = SPATIAL[sidx]
        bits = BITDEPTH[bidx]
        levels = 2**bits

        data = np.frombuffer(f.read(), dtype=np.uint8)
        imgq = data.reshape((size,size))

    img = (imgq/(levels-1))*255
    img = img.astype(np.uint8)
    return img
