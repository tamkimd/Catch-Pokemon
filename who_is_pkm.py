import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
from fastai.vision.all import *
x = load_learner("catch_pkm.pkl")

def classify(img_path):
    pkm=x.predict(img_path)
    return "abra" if pkm[2][1] > 0.985 else "other"
