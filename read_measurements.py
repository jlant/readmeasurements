# Author: Jeremiah Lant
# Purpose: Script to read a set of measurement files.

import sys

def read_file(file_str):
	""" Return file lines for a file """

	file_obj = open(file_str, "r")
	file_lines = file_obj.readlines()
	
	return file_lines

def extract_column_names(file_lines):
	""" Return a list of tuples containing column names and its respective index. Mutates the file lines list by extracting first element (first row of data file) """
	column_names = file_lines.pop(0)
	column_names = column_names.rstrip().split("\t")
	column_names = list(enumerate(column_names))
	
	return column_names		

def get_data(file_lines, column_names):
	""" Return a dictionary of data containing each data parameter"""
	data = {}
	for column_index, column_name in column_names:
		values = []
		for line in file_lines:
			line_list = line.rstrip().split("\t")
			value = line_list[column_index]
			values.append(value)
		
		data[column_name] = values
	
	return data			
	
def compute_stats(parameter_list):
	""" Return average, max, min for a data parameter list"""
	
	avg_param = sum(parameter_list) / len(parameter_list)
	max_param = max(parameter_list)
	min_param = min(parameter_list)	
	
	return avg_param, max_param, min_param

def find_date(date_list, parameter_list, value):
	""" Return the string date that corresponds to a particular value in a parameter list"""
	value_index = parameter_list.index(value)		# find where the value occurs in the parameter list
	date = date_list[value_index]					# get the date that corresponds to the value index
	
	return date

def extract_dates_parameters(data, date_key):
	""" Return a list of dates extracted from the data dictionary along with the modified data dictionary"""
	dates = data.pop(date_key)
	
	return dates, data

def convert_to_float(str_list):
	""" Return a list of floats """
	values = []
	for value in str_list:
		values.append(float(value))	
	
	return values
	
def format_parameters(parameters):
	""" Return a dictionary with each key containing lists of floating point numbers """
	
	for key, values in parameters.iteritems():
		values = convert_to_float(values)
		parameters[key] = values
	
	return parameters

def print_results(name, avg_value, max_value, min_value, max_date, min_date):
	""" Print the results in a nice format """
	print("")
	print("\t{}".format(name))
	print("\t\t Average: {0}".format(avg_value))
	print("\t\t Maximum: {0} occurred on {1}".format(max_value, max_date))
	print("\t\t Minimum: {0} occurred on {1}".format(min_value, min_date))

def process_data(dates, parameters): 
	""" Process the data by computing stats, finding dates of interest, and printing results """
	
	for key, item in parameters.iteritems():
		avg_param, max_param, min_param = compute_stats(parameter_list = item)		
		max_date = find_date(date_list = dates, parameter_list = item, value = max_param)
		min_date = find_date(date_list = dates, parameter_list = item, value = min_param)	

		print_results(key, avg_param, max_param, min_param, max_date, min_date)
	
def main():
	python_filename = sys.argv[0]
	all_files = sys.argv[1:]

	for measurements_file_str in all_files:
	
		print("{}".format(measurements_file_str))
		
		file_lines = read_file(file_str = measurements_file_str)
		column_names = extract_column_names(file_lines) 
		data = get_data(file_lines, column_names)
		dates, parameters = extract_dates_parameters(data, date_key = "date")
		parameters = format_parameters(parameters)
		process_data(dates, parameters)
		
		print("-" * 50)
		
if __name__ == "__main__":
	main()