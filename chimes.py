import os
import pandas as pd
import numpy as np
import csv
from typing import List, Any


os.chdir(r'.')


def get_file_list() -> List[str]:
	file_list: List[str] = []
	for filename in os.listdir(os.getcwd()):
		if filename.endswith('.csv'):
			file_list.append(filename)
	if int(len(file_list)) <= 0:
		print("Not enough .csv files in data folder")
	else:
		print(file_list)
	return file_list


def get_data_list(file_list: List[str]) -> List[Any]:
	data_list = []
	for filename in file_list:
		data_list.append(pd.read_csv(filename, sep=',', encoding='UTF-16', header=3))
	print(str(len(data_list)) + " files loaded into memory")
	return data_list


def get_fixed_list(data_list: List[Any]) -> List[Any]:
	fixed_list = []
	for data in data_list:
		num_cols = len(list(data))
		rng = range(1, num_cols + 1)
		column_names = []
		x = 1
		for i in rng:
			if i % 2 == 0:
				column_names.append('A' + str(x))
				x += 1
			else:
				column_names.append('V' + str(x))
		data.columns = column_names[:num_cols]
		#data.columns = ['V1', 'A1', 'V2', 'A2', 'V3', 'A3']
		if isinstance(data.at[0, 'V1'], str):
			#print(data.at[0,'V1'])
			data[0:] = data[0:].shift(-1)
			data = data.drop(data.tail(1).index, inplace=True)

		volts = np.array([])
		amps = np.array([])
		for name in column_names:
			if 'V' in name:
				volts = np.concatenate((volts, np.array(data[name])))
			elif 'A' in name:
				amps = np.concatenate((amps, np.array(data[name])))

#		volts = pd.Series()
#		amps = pd.Series()
#		for name in column_names:
#			if 'V' in name:
#					volts = volts.append(data[name], ignore_index=True)
#			elif 'A' in name:
#					amps = amps.append(data[name], ignore_index=True)
		d = {'V': volts, 'A': amps, }
		fixed_list.append(pd.DataFrame(data=d))
	return fixed_list


def get_combined_data(fixed_list: List[Any]) -> Any:
	d2 = {'V': fixed_list[0]['V'], }
	combined_data = pd.DataFrame(data=d2)
	x: int = 1
	for fix in fixed_list:
		combined_data[x] = fix['A']
		x += 1
	return combined_data


def get_combined_data_columns(file_list: List[str]) -> List[str]:
	combined_data_columns: List[str] = ['Volts']
	for filename in file_list:
		scan: str = filename[(len(filename) - len(".csv") - 3):len(filename) - len(".csv")]
		scan_list = list(scan)
		number_list: List[str] = ['0', '1', '3', '4', '5', '7', '8', '9']
		if scan_list[-2] not in number_list:
			scan_list[-2] = '0'
		if scan_list[-3] not in number_list:
			scan_list[-3] = '0'
		scan = ''.join(scan_list)
		combined_data_columns.append("scan_" + scan)
	#print(combined_data_columns)
	return combined_data_columns


def print_combined_data(combined_data: Any, combined_data_columns: List[str]) -> None:
	with open('chimesout.tsv', 'w', newline='', encoding='UTF-8') as csvfile:
		dataout = csv.writer(csvfile, delimiter='\t')
		dataout.writerow(combined_data_columns)
		for index, row in combined_data.iterrows():
			#print(row)
			dataout.writerow((row))
		print("Output.tsv file updated")


def mung() -> None:
	file_list = get_file_list()
	data_list = get_data_list(file_list)
	fixed_list = get_fixed_list(data_list)
	combined_data = get_combined_data(fixed_list)
	combined_data_columns = get_combined_data_columns(file_list)
	print_combined_data(combined_data, combined_data_columns)

	#reveal_type(file_list)
	#reveal_type(data_list)
	#reveal_type(fixed_list)
	#reveal_type(combined_data)
	#reveal_type(combined_data_columns)


if __name__ == "__main__":
	mung()
