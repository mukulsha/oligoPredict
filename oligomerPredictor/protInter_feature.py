
import warnings
import numpy as np
import pandas as pd
import protinter.protinter as pt
from oligo_utils import *

warnings.filterwarnings("ignore")


def protinter_main(filepath):
    id = get_id(filepath)
    final_results = {'pdb_id': list(),
                 'hydrophobic': list(),
                 'disulphide': list(),
                 'ionic': list(),
                 'catpi': list(),
                 'aroaro': list(),
                 'arosul': list(),
                 'hb1': list(),
                 'hb2': list(),
                 'hb3': list()}
    try:
        res = pt.main(filepath, csv= True, hydrophobicRun=True, disulphideRun=True, ionicRun=True, aroaroRun=True, arosulRun=True, catpiRun=True, hb1Run=True, hb2Run=True, hb3Run=True, interval=0)
        res = pd.DataFrame([(key, len(res[key])) for key in res]).set_index(0, drop=True).T
        res.index = [id]
        return res
    except Exception as e:
        print(f'ProtInter feature extraction for {filepath} failed with error {e}.')