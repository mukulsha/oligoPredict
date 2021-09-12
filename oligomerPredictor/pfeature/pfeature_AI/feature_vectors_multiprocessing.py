
import os
import multiprocessing 

def read_output(filename,first):
	global all_features
	f = open(filename)
	line_no = 0
	for line in f:
		line = line[:-1]
		line = line.split(",")
		if(first):
			all_features.append(line)
		else:
			all_features[line_no] = all_features[line_no] + line

		line_no+=1
	f.close()
	os.system("rm " + filename)

def get_feature(command1, command2, feature):
	os.system(command1 + feature + command2 + "output_" + feature + ".txt")


def main():

	protein_file = "input.fasta"
	file_number = 1


	features = ['AAI']

	features_all = ['AAC','DPC','TPC','ATC','BTC','PCP','AAI','RRI','PRI','DDR','SEP','SER','SPC','ACR','CTC','CeTD','PAAC','APAAC','QSO','SOC','ALLCOMP']
	command1 = "python3 pfeature_comp.py -j "
	command2 = " -i " + protein_file + " -o "


	all_protein_names = ["Name"]
	f = open(protein_file)
	for line in f:
		if(line[0] == ">"):
			all_protein_names.append(line[1:-1])

	global all_features
	all_features = []

	processes = []
	for feature in features:
		
		p = multiprocessing.Process(target=get_feature, args=(command1,command2,feature,))
		processes.append(p)
		p.start()

	for process in processes:
		process.join()

