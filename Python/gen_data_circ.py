import numpy
		
def dis_r_out(x,y,cx,cy,r):
	dis = (((x-cx)**2)+((y-cy)**2))**(0.5)
	if dis > r:
		return True
	else:
		return False
		
def dis_r_in(x,y,cx,cy,r):
	dis = (((x-cx)**2)+((y-cy)**2))**(0.5)
	if dis < r:
		return True
	else:
		return False
		
def gen_samp(med,var):
	axu = numpy.random.normal(med,var,1)
	axi = axu[0]
	return axi
	

xm = 15 #media en x
vx = 1 #varianza en x
vxr = 5 #distancia interna circulo grande
vx2 = 6 #distancia externa circulo grande

ym = 15
vy = 1
vyr = 5
vy2 = 6

n = 100 #tamaño de los clusters

ax = numpy.array([])
ay = numpy.array([])

bx = numpy.array([])
by = numpy.array([])

for i in range(0,n):
	while True:
		axi = gen_samp(xm,vx)
		
		ayi = gen_samp(ym,vy)

		if (dis_r_in(axi,ayi,xm,ym,vx)) and (axi > 0) and (ayi > 0):
			ax = numpy.append(ax,axi)
			ay = numpy.append(ay,ayi)

			break

for i in range(0,n):
	while True:
		bxi = gen_samp(xm,vx2)
		
		byi = gen_samp(ym,vy2)

		if (dis_r_out(bxi,byi,xm,ym,vxr)) and (dis_r_in(bxi,byi,xm,ym,vx2)) and (bxi > 0) and (byi > 0):
			bx = numpy.append(bx,bxi)
			by = numpy.append(by,byi)

			break
		
f = open ('dataset_circ_04.txt','w')

for k in range(0,n):
	x = ax[k]
	y = ay[k]
	s = str(x) + '	' + str(y) + '\n'
	f.write(s)
	
for l in range(0,n):
	x = bx[l]
	y = by[l]
	s = str(x) + '	' + str(y) + '\n'
	f.write(s)
	
f.close()


	
