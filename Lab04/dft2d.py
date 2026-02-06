import numpy as np

def dft2d(image):
    M, N = image.shape
    F = np.zeros((M, N), dtype=complex)

    for u in range(M):
        for v in range(N):
            s = 0.0 + 0.0j
            for x in range(M):
                for y in range(N):
                    angle = -2j * np.pi * ((u * x) / M + (v * y) / N)
                    s += image[x, y] * np.exp(angle)
            F[u, v] = s

    return F
