import csv
import os

def remap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def normalize(filename):

	# Extraer datos y copiarlos en una matriz
	data = []
	with open(filename, 'r') as csvfile:
		csvreader = csv.DictReader(csvfile)
		for row in csvreader:			
			data.append(row)

	# Crear un diccionario vacío con mínimos y máximos
	minmax = {}
	for k in data[0]:
		minmax[k] = {'min': float('inf'),
					'max': -float('inf')}

	# recorrer datos y actualizar mínimos y máximos
	for objeto in data:
		for key in objeto:
			if int(objeto[key]) < minmax[key]['min']:
				minmax[key]['min'] = int(objeto[key])
			
			if int(objeto[key]) > minmax[key]['max']:
				minmax[key]['max'] = int(objeto[key])

	# normalize
	normalized = []

	for objeto in data:
		line = []
		for key in objeto:

			if key != 'Infectados':	
				OldValue = int(objeto[key])
				OldMax = minmax[key]['max']
				OldMin = minmax[key]['min']
				NewMax = 1
				NewMin = 0				
				NewValue = remap(OldValue, OldMax, OldMin, NewMax, NewMin)

			else:
				NewValue = 0

			line.append(NewValue)

		normalized.append(line)

	dump_data(normalized)

def dump_data(data):

	filename = 'n_data.csv'
	file_exists = os.path.isfile(filename)

	with open(filename, "a") as csvfile:
		
		writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')

		for row in data:
			writer.writerow(row)

def main():
	data_file = 'data.csv'
	normalize(data_file)

	

main()