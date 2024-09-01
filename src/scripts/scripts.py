import pickle
import numpy as np


def load_highscore() -> str:
    try:
        with open('../score.dat', 'rb') as file:
            highscore = pickle.load(file)
    except:
        highscore = 0
    return highscore
