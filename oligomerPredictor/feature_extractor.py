from pfeature_feature import *
from protInter_feature import *
from dssp_feature import *
from protvec_feature import *
from oligo_utils import *
import time

def get_features_df(filepath):
    
    start_time = time.time()
    pfeature_feat = pfeature_main(filepath)
    protinter_feat = protinter_main(filepath)
    dssp_feat = dssp_main(filepath)
    protvec_feat = protvec_main(get_sequence(filepath), get_id(filepath))
    print("Time of execution = " + str(time.time() - start_time))
    
    return pd.concat([pfeature_feat, protinter_feat, dssp_feat, protvec_feat], 1)


if __name__ == '__main__':
    df = get_features_df('18gs.pdb')
    print(df)