import matplotlib.pyplot as plt
import numpy as np
import os
import patchify
from conv import convapool
import pickle
import random

def common_list_of_lists(lst):
    temp = set(lst[0]).intersection(*lst)
    return list(temp)

pickle_in = open("star_data.pickle","rb")
stars = pickle.load(pickle_in)
pickle_in.close()

stars = common_list_of_lists(stars)

pickle_out = open("stars.pickle","wb")
pickle.dump(stars, pickle_out)
pickle_out.close()

print(len(stars))

print(stars)

print(stars[43])