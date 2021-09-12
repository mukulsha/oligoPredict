#!C:\Users\MUKUL SHARMA\AppData\Local\Microsoft\WindowsApps\python

from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import PPBuilder
import protinter.lib.interlib as pi
import pandas as pd
import argparse
import textwrap

__author__ = "Maxime Borry"
__editor__ = "Mukul Sharma"
__version__ = 0.2

def main(myfile, csv= True, hydrophobicRun=True, disulphideRun=True, ionicRun=True, aroaroRun=True, arosulRun=True, catpiRun=True, hb1Run=True, hb2Run=True, hb3Run=True, a=5.0, b=2.2, c=6.0, d=4.5, e=7.0, f=5.3, g=6.0, i=3.5, j=4, interval=0):
    # myfile, csv, hydrophobicRun, disulphideRun, ionicRun, aroaroRun, arosulRun, catpiRun, hb1Run, hb2Run, hb3Run, a, b, c, d, e, f, g, i, j, interval = get_args()
    p = PDBParser()
    count_dict = dict()
    structure = p.get_structure('X', myfile)
    for model in structure:
        for chain in model:
            for resid in chain:
                if resid.get_resname() in pi.amino["aroaro"]:
                    pi.center_mass(resid)
                hydrophobic = pi.get_res(chain, amino_type="hydrophobic")
                disulphide = pi.get_res(chain, amino_type="disulphide")
                ionic = pi.get_res(chain, amino_type="ionic")
                catpi = pi.get_res(chain, amino_type="cationpi")
                aroaro = pi.get_res(chain, amino_type="aroaro")
                arosul = pi.get_res(chain, amino_type="arosul")
                hbond = pi.get_res(chain, amino_type="all")
    ppb = PPBuilder()
    results_dict = dict()
    if hydrophobicRun:

        results_dict['hydrophobic'] = pi.calc_inter(
            hydrophobic,
            csv=csv,
            filename=myfile,
            distmax=a,
            amino_type="hydrophobic",
            inter=interval)

    if disulphideRun:
        results_dict['disulphide'] = pi.calc_inter(
            disulphide,
            csv=csv,
            filename=myfile,
            distmax=b,
            amino_type="disulphide",
            inter=interval)

    if ionicRun:
        results_dict['ionic'] = pi.calc_inter(
            ionic,
            csv=csv,
            filename=myfile,
            distmax=c,
            amino_type="ionic",
            inter=interval)

    if catpiRun:
        results_dict['catpi'] = pi.calc_inter(
            catpi,
            csv=csv,
            filename=myfile,
            distmax=g,
            amino_type="cationpi",
            inter=interval)

    if aroaroRun:
        results_dict['aroaro'] = pi.calc_inter(
            aroaro,
            csv=csv,
            filename=myfile,
            distmin=d,
            distmax=e,
            amino_type="aroaro",
            inter=interval)

    if arosulRun:
        results_dict['arosul'] = pi.calc_inter(
            arosul,
            csv=csv,
            filename=myfile,
            distmax=f,
            amino_type="arosul",
            inter=interval)

    if hb1Run:
        results_dict['hb1'] = pi.calc_inter(
            hbond,
            csv=csv,
            filename=myfile,
            distON=i,
            distS=j,
            amino_type="hbond_main_main",
            inter=interval)

    if hb2Run:
        results_dict['hb2'] = pi.calc_inter(
            hbond,
            csv=csv,
            filename=myfile,
            distON=i,
            distS=j,
            amino_type="hbond_main_side",
            inter=interval)

    if hb3Run:
        results_dict['hb3'] = pi.calc_inter(
            hbond,
            csv=csv,
            filename=myfile,
            distON=i,
            distS=j,
            amino_type="hbond_side_side",
            inter=interval)
#     count_dict['pdb_id'].append(file[:4].upper())
#     result_df = list()
#     for key in results_dict:
#         df = pd.DataFrame(results_dict[key], columns = ('res_1', 'resid_1','res_2', 'resid_2', 'dist_armst'))
#         df['property'] = key
#         result_df.append(df[['property', 'res_1', 'resid_1','res_2', 'resid_2', 'dist_armst']])
#         count_dict[key].append(len(results_dict[key]))
#     result_df = pd.concat(result_df, ignore_index = True)        
#     result_df.to_csv('protinter_csv/{}.csv'.format(myfile.split('/')[-1].split('.')[0]))
#     return count_dict
    return results_dict
