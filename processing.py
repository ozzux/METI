import pickle
import matplotlib.pyplot as plt

pickle_in = open("star_light.pickle","rb")
star_light = pickle.load(pickle_in)
pickle_in.close()

for star in range(len(star_light)):
    plt.plot(star_light[star])
    plt.title(str(star))
    plt.show()