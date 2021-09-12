import warnings
import os
from Bio import SeqIO

def generate_fasta_file(id, sequence):

    with open('pfeature/pfeature_AC/input.fasta', 'w') as file:
        file.write(f'>{id}\n')
        file.write(f'{sequence}\n')
    with open('pfeature/pfeature_AI/input.fasta', 'w') as file:
        file.write(f'>{id}\n')
        file.write(f'{sequence}\n')

def get_id(filepath):
    id = filepath[:filepath.rfind('.')]
    if '/' in id:
        id = filepath[filepath.rfind('/')+1:]
    return id

def get_sequence(filepath):
    with warnings.catch_warnings():
        sequence = ''
        try:
            sequence = ''.join(set([str(record.seq) for record in SeqIO.parse(filepath, "pdb-seqres")]))
        except:
            try:
                sequence = ''.join(set([str(record.seq) for record in SeqIO.parse(filepath, "pdb-atom")]))

            except:
                pass
    if sequence is '':
        print('Failed to fetch sequence from file')
    return sequence