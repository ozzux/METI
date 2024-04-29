import matplotlib.pyplot as plt
import numpy as np
import os
import patchify
from conv import convapool
import pickle
import random

# Loading in Frame 1 as base for star detection
base = plt.imread(os.path.join("images","aligned_project night 2_00001.png"))
        
base = convapool(base,20)

plt.imshow(base, cmap="gray")
plt.show()


# Identifying Stars
stars = []
for row in range(len(base)):
    for chunk in range(len(base[row])):
        if base[row][chunk] > 0.18:
            stars.append((row,chunk))

print(len(stars))

# Collecting Light Data on Each Star
star_light = []
for star in stars:
    star_light.append([])

rand_stars = []
for num in range(10):
    rand_stars.append(random.randint(0,len(stars)))

for image in range(1,286):
    try:
        frame = plt.imread(os.path.join("images","aligned_project night 2_" + str(image).zfill(5) + ".png"))
        frame = convapool(frame, 20)
    except:
        pass
    
    i = 0
    avg = 0

    for row in frame:
        for chunk in row:
            if chunk == 0:
                pass
            else:
                i = i + 1
                avg = avg + chunk

    avg = avg/i

    for star in range(len(stars)):
        star_light[star].append((frame[stars[star][0]][stars[star][1]])/avg)

pickle_out = open("star_light.pickle","wb")
pickle.dump(star_light,pickle_out)
pickle_out.close()
    
# Printing sky
plt.figure(1)
plt.imshow(base, cmap="gray")
print(base[stars[2][0]][stars[2][1]])
plt.show()