import matplotlib.pyplot as plt
import numpy as np
import os
import patchify
from conv import convapool
import pickle
import random

# Loading in Frame 1 as base for star detection
base = plt.imread(os.path.join("images","aligned_project night 2_00127.png"))
        
base = convapool(base,20)

plt.imshow(base, cmap="gray")
plt.show()


pickle_in = open("stars.pickle", "rb")
stars = pickle.load(pickle_in)
pickle_in.close()

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

    avg = 0
    for i in range(10):
        num = random.randint(0,len(stars)-1)
        avg += frame[stars[num][1]][stars[num][0]]

    avg = avg/10

    for star in range(len(stars)):
        star_light[star].append((frame[stars[star][1]][stars[star][0]])/avg)

pickle_out = open("star_light.pickle","wb")
pickle.dump(star_light,pickle_out)
pickle_out.close()
    
# Printing sky
plt.figure(1)
plt.imshow(base, cmap="gray")
print(base[stars[2][1]][stars[2][0]])
plt.show()