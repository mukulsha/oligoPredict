import os
import pandas as pd
from oligo_utils import *
import pfeature.pfeature_AC.feature_vectors_multiprocessing as pac
import pfeature.pfeature_AI.feature_vectors_multiprocessing as pai


def pfeature_main(filepath):
    id = get_id(filepath)
    sequence = get_sequence(filepath)
    generate_fasta_file(id, sequence)
    try:
        cwd = os.getcwd()
        os.chdir(f'{cwd}/pfeature/pfeature_AC')
        pac.main()
        os.chdir(f'{cwd}/pfeature/pfeature_AI')
        pai.main()
        os.chdir(cwd)
        df1 = pd.read_csv(f'{cwd}/pfeature/pfeature_AC/output_ALLCOMP.txt')
        df2 = pd.read_csv(f'{cwd}/pfeature/pfeature_AI/output_AAI.txt')
        df = pd.concat([df1,df2], axis = 1)
        df.index = [id] 
        return df
    except Exception as e:
        print(f'PFeature feature extraction for {filepath} failed with error {e}.')

if __name__ == '__main__':
    print(pfeature_main('18gs.pdb').shape)
    
