# -*- coding: utf-8 -*
code = open("comm.py","r")
#Άνοιγμα του αρχείου comm
code_back = open("new_comm.py","w")
#Δημιουργία νέου αρχείου με όνομα new_comm
for line in code:
    if not line.startswith("#"): 
	# Δεν χρειάζεται κενό εδώ
        code_back.write(line)
code.close()
code_back.close()