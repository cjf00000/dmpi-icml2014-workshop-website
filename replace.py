import os, sys, glob

replace_file_name = "allreplace"

f = open(replace_file_name, 'r')
replace_table = f.readlines()
f.close()

replace_src = []
replace_dest = []

for i in xrange(len(replace_table)/2):
	replace_src.append(replace_table[i*2])
	replace_dest.append(replace_table[i*2+1])

for htmlname in glob.glob('*.html'):
	print htmlname
	
	f = open(htmlname, 'r')
	html = f.readlines()
	f.close()

	for i in xrange(len(html)):
		for j in xrange(len(replace_src)):
			if html[i] == replace_src[j]:
				print 'Line %d hit.' % i
				html[i] = replace_dest[j]

	f = open(htmlname, 'w')
	f.writelines(html)
	f.close()
