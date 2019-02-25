import numpy

def gen_samp(med,var):
	axu = numpy.random.normal(med,var,1)
	axi = axu[0]
	return axi
		
xm1 = 20 #media en x
vx1 = 12 #varianza en x
ym1 = 20
vy1 = 12
zm1 = 50
vz1 = 12

xm2 = 80 #media en x
vx2 = 3 #varianza en x
ym2 = 50
vy2 = 7
zm2 = 80
vz2 = 12

xm3 = 50 #media en x
vx3 = 12 #varianza en x
ym3 = 80
vy3 = 3
zm3 = 20
vz3 = 7

n = 500 #tamaño de los clusters

ax = numpy.array([])
ay = numpy.array([])
az = numpy.array([])

bx = numpy.array([])
by = numpy.array([])
bz = numpy.array([])

cx = numpy.array([])
cy = numpy.array([])
cz = numpy.array([])

for i in range(0,n):
	while True:
		axi = gen_samp(xm1,vx1)
		
		ayi = gen_samp(ym1,vy1)
		
		azi = gen_samp(zm1,vz1)

		if (axi > 0) and (ayi > 0) and (azi > 0):
			ax = numpy.append(ax,axi)
			ay = numpy.append(ay,ayi)
			az = numpy.append(az,azi)

			break
			
for i in range(0,n):
	while True:
		bxi = gen_samp(xm2,vx2)
		
		byi = gen_samp(ym2,vy2)
		
		bzi = gen_samp(zm2,vz2)

		if (bxi > 0) and (byi > 0) and (bzi > 0):
			bx = numpy.append(bx,bxi)
			by = numpy.append(by,byi)
			bz = numpy.append(bz,bzi)

			break
			
for i in range(0,n):
	while True:
		cxi = gen_samp(xm3,vx3)
		
		cyi = gen_samp(ym3,vy3)
		
		czi = gen_samp(zm3,vz3)

		if (cxi > 0) and (cyi > 0) and (czi > 0):
			cx = numpy.append(cx,cxi)
			cy = numpy.append(cy,cyi)
			cz = numpy.append(cz,czi)

			break
		
f = open ('dataset_circ_3d_3.txt','w')

for k in range(0,n):
	x = ax[k]
	y = ay[k]
	z = az[k]
	s = str(x) + '	' + str(y) + '	' + str(z) + '\n'
	f.write(s)
	
for l in range(0,n):
	x = bx[l]
	y = by[l]
	z = bz[l]
	s = str(x) + '	' + str(y) + '	' + str(z) + '\n'
	f.write(s)
	
for m in range(0,n):
	x = cx[m]
	y = cy[m]
	z = cz[m]
	s = str(x) + '	' + str(y) + '	' + str(z) + '\n'
	f.write(s)
	
f.close()


	
