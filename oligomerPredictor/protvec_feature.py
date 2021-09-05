import os
import biovec
import pickle
import numpy as np
import pandas as pd

def generate_vector(fasta_sequence, id):
    pv = pickle.load(open('oligomerPredictor/data/protvec_32X32_win17_model.pkl', 'rb'))
    df = pd.DataFrame(np.hstack(pv.to_vecs(fasta_sequence))).T
    df.index = [id]
    return df