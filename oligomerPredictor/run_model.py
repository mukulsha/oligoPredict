import pandas as pd
import numpy as np

def runner(filepath):
    print(filepath, 'runner')
    data = np.random.random((1,6))
    df = pd.DataFrame(data, columns=['DIMER', 'TRIMER', 'TETRAMER', 'PENTAMER', 'HEXAMER', 'HEPTAMER'], index=['p'])
    return df