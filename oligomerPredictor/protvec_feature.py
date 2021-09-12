import os
import biovec
import pickle
import numpy as np
import pandas as pd
from oligo_utils import *

def protvec_main(sequence, id):
    try:
        pv = pickle.load(open(f'{os.getcwd()}/data/protvec_32X32_win17_model.pkl', 'rb'))
        df = pd.DataFrame(np.hstack(pv.to_vecs(sequence))).T
        df.index = [id]
        return df
    except Exception as e:
        print(f'ProtVec feature extraction for {filepath} failed with error {e}.')