from urllib.request import urlopen
import pickle

stuff = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for line in stuff:
    print("".join([k*v for k, v in line]))
