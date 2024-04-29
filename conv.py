import matplotlib.pyplot as plt
import numpy as np
import os
import patchify

def convapool(image, tilesize):
    shap = (tilesize,tilesize)

    split_image = patchify.patchify(image,shap,step=shap[0])

    image2 = []

    for row in range(len(split_image)):
        image2.append([])
        for chunk in split_image[row]:
            nchunk = chunk.reshape((shap[0]*shap[1],))
            image2[row].append(nchunk.mean())

    image2 = np.array(image2)

    return image2