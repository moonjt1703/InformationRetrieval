from math import log
import random

from nltk.lm import vocabulary
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer

k1 = 70
k2 = 100
b = 0.95
R = 0.0


def BM25(n, f, qf, r, N, dl, avdl):
    K = compute_K(dl, avdl)
    first = log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))
    second = ((k1 + 1) * f) / (K + f)
    third = ((k2 + 1) * qf) / (k2 + qf)
    return first * second * third


def compute_K(dl, avdl):
    return k1 * ((1 - b) + b * (float(dl) / float(avdl)))


def ltn(tf,dft,N):
    return(1+log(tf))*log(N/dft)

