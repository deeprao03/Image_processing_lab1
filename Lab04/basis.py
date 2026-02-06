import numpy as np
import matplotlib.pyplot as plt
import os

def dft_basis_8x8_as_64x64():

    os.makedirs("Lab04/Result", exist_ok=True)

    N = 8

    big = np.zeros((N * N, N * N))

    row = 0
    col = 0

    for u in range(N):
        for v in range(N):

            basis = np.zeros((N, N), dtype=complex)

            for x in range(N):
                for y in range(N):
                    basis[x, y] = np.exp(
                        -2j * np.pi * ((u * x) / N + (v * y) / N)
                    )

            patch = np.real(basis)

            big[row*N:(row+1)*N, col*N:(col+1)*N] = patch

            col += 1
            if col == N:
                col = 0
                row += 1

    plt.figure(figsize=(6,6))
    plt.imshow(big, cmap='gray')
    plt.title("8x8 2-D DFT basis shown as 64x64 image")
    plt.colorbar()

    plt.savefig("Lab04/Result/dft_basis.png", bbox_inches="tight", dpi=150)

    plt.show(block=False)
    plt.pause(2)
    plt.close()
