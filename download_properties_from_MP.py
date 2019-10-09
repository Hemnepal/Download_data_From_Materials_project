#run the first part only and download all structures_cif
#you need to delete the last line of these cif to proceed further
#because the last line contains MPID

#part 1
from pymatgen import MPRester
api = MPRester(api_key="your_api")#your api from materials-project dashboard

#If you want only Oxygen containing compounds, "$all":["O"] in criteria
#also you can include other elements 

#criteria1={"elements":{"$all": ["O"]}, "nelements":{'$lt':4}}  
criteria={"nelements":{'$lt':4}}
properties=["pretty_formula","cif","material_id", "formation_energy_per_atom", "band_gap"]

c = api.query(criteria=criteria,properties=properties)
#write band gap and formation energy in a single file
g = open("one_file.txt", "w")
g.write("Material" + " " + "Formation_energy" + " " + "band_gap" + "\n")
for i in c:
	formula = i.get("pretty_formula", " ")
	material_id = i.get("material_id")
	formation_energy_per_atom = i.get("formation_energy_per_atom")
	band_gap = i.get("band_gap")
	print(formation_energy_per_atom, band_gap)
	f = open(str(material_id) + str(formula) + ".cif", "w")
	for key, value in i.items():
		f.write(str(value))
	g.write(str(material_id) +str(formula) + ".cif"+ " " + str(formation_energy_per_atom) + " " +  str(band_gap) + "\n")

#after first part  is done uncomment part2 and comment part1
#part 2
######################3
#make a list of all cifs to remove the last line
#import os
#listdir = os.listdir("./")
#g = open("one_file.txt", "r")
#f = open("file_data.dat", "w")
#for lines in g:
#        line = lines.split(" ")[0]
#        f.write(str(line) + "\n")

#once part 2 is done comment part1 and 2 then run the following
#which will read the list in part2 and delete the last line and make a new cif filw with same name
#part 3
#####################
#import shutil
#from shutil import copyfile
#f = open("file_data.dat", "r")
#for lines in f:
#        header = lines.split()[0]
#        lines = open(str(header)).readlines()
#        temp = open(str(header) + "1", "w")
#        temp.writelines([item for item in lines[:-1]])
#        temp.close()
#        shutil.move(str(header) + "1", str(header))
