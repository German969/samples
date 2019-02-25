import numpy

xm = 15
vx = 3
vxr = 6
vx2 = 9
ym = 15
vy = 3
vyr = 6
vy2 = 9

f = open ('dataset_circ_02.txt','w')

for k in range(0,50):
	x = numpy.random.uniform(15.0,18.0)
	y = numpy.random.uniform(15.0,18.0)
	s = str(x) + '	' + str(y) + '\n'
	f.write(s)
	
for l in range(0,50):
	x = numpy.random.uniform(21.0,24.0)
	y = numpy.random.uniform(21.0,24.0)
	s = str(x) + '	' + str(y) + '\n'
	f.write(s)
	
f.close()