import matplotlib.pyplot as plt
import numpy as np
import os
import patchify
from conv import convapool
import pickle
import random

stars = []

for image in range(1,286):
    try:
        frame = plt.imread(os.path.join("images","aligned_project night 2_" + str(image).zfill(5) + ".png"))
        frame = convapool(frame, 20)
    except:
        pass
    stars.append([])
    for row in range(len(frame)):
        for chunk in range(len(frame[row])):
            if frame[row][chunk] > 1.1 * frame.mean():
                stars[image-1].append((chunk,row))

pickle_out = open("star_data.pickle", "wb")
pickle.dump(stars, pickle_out)
pickle_out.close()

print("Done")
