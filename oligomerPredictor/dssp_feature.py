import warnings
import pandas as pd
from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP

dssp_dict = dict()
dssp_fails = list()
p = PDBParser()

def get_dssp(filepath):
    id = filepath[:filepath.rfind('.')]
    if '/' in id:
        id = filepath[filepath.rfind('/')+1:]
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            structure = p.get_structure(id, filepath)
            model = structure[0]
            dssp = DSSP(model, filepath).property_dict
            columns_map = {'level_0': 'chain_id', 'level_1': 'residue_id', 0:'dssp_index', 1:'aa', 
                2:'sec_structure', 3:'relative_asa', 4:'phi', 5:'psi', 6:'NH–>O_1_relidx', 
                7:'NH–>O_1_energy', 8:'O–>NH_1_relidx', 9:'O–>NH_1_energy', 10:'NH–>O_2_relidx', 
                11:'NH–>O_2_energy', 12:'O–>NH_2_relidx', 13:'O–>NH_2_energy'}
            df = pd.DataFrame(dssp).T.reset_index().rename(columns=columns_map)
            ps = df.drop(['residue_id', 'dssp_index'],1)
            df1 = pd.DataFrame(ps.groupby('sec_structure')['aa'].value_counts())
            df1 = pd.DataFrame({k:v for k,v in zip([''.join(x) for x in list(df1.T.columns)], df1.values)})
            df2 = pd.DataFrame(ps.groupby('sec_structure').count()).T.reset_index(drop=True).head(1)
            df3 = ps.groupby('sec_structure').sum().stack()
            df3.index = df3.index.map('ss_sum{0[0]}_{0[1]}'.format)
            df3 = df3.to_frame().T
            df4 = ps.groupby('aa').sum().stack()
            df4.index = df4.index.map('aa_sum{0[0]}_{0[1]}'.format)
            df4 = df4.to_frame().T
            df5 = ps.groupby('sec_structure').std().stack()
            df5.index = df5.index.map('ss_std_{0[0]}_{0[1]}'.format)
            df5 = df5.to_frame().T
            df6 = ps.groupby('aa').std().stack()
            df6.index = df6.index.map('aa__std{0[0]}_{0[1]}'.format)
            df6 = df6.to_frame().T
            ps = list(pd.concat([df2,df1,df3, df4, df5, df6], 1).T.to_dict().values())[0]   
            cols = pd.read_csv('oligomerPredictor/data/dssp_cols.csv').columns
            return pd.DataFrame({k:ps.get(k, 0) for k in cols}, index = [id])

    except Exception as e:
        print(f'DSSP feature extractoin for {filepath} failed with error {e}.')
