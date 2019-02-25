import numpy
		
def dis_r_out(x,y,cx,cy,rx,ry):
	disx = ((x-cx)**2)/((rx)**2)
	disy = ((y-cy)**2)/((ry)**2)
	dis = disx + disy
	if dis > 1:
		return True
	else:
		return False
		
def dis_r_in(x,y,cx,cy,rx,ry):
	disx = ((x-cx)**2)/((rx)**2)
	disy = ((y-cy)**2)/((ry)**2)
	dis = disx + disy
	if dis < 1:
		return True
	else:
		return False
		
def gen_samp(med,var):
	axu = numpy.random.normal(med,var,1)
	axi = axu[0]
	return axi
	
def cut_2c(x,y,cx,cy):
	if((x > cx) and (y > cy)):
		return False
	else:
		return True

def cut_3c(x,y,cx,cy):
	if((x < cx) and (y < cy)):
		return False
	else:
		return True

xm1 = 34 #media en x
vx1 = 24 #distancia elipse mayor
vxr1 = 16 #distancia elipse menor

ym1 = 30
vy1 = 18
vyr1 = 12

xm2 = 30
vx2 = 24
vxr2 = 16

ym2 = 48
vy2 = 20
vyr2 = 14



n = 500 #tamaño de los clusters

ax = numpy.array([])
ay = numpy.array([])

bx = numpy.array([])
by = numpy.array([])

for i in range(0,n):
	while True:
		axi = gen_samp(xm1,vx1)
		
		ayi = gen_samp(ym1,vy1)

		if (dis_r_in(axi,ayi,xm1,ym1,vx1,vy1)) and (dis_r_out(axi,ayi,xm1,ym1,vxr1,vyr1)) and (axi > 0) and (ayi > 0) and (cut_2c(axi,ayi,xm1,ym1)):
			ax = numpy.append(ax,axi)
			ay = numpy.append(ay,ayi)

			break

for i in range(0,n):
	while True:
		bxi = gen_samp(xm2,vx2)
		
		byi = gen_samp(ym2,vy2)

		if (dis_r_in(bxi,byi,xm2,ym2,vx2,vy2)) and (dis_r_out(bxi,byi,xm2,ym2,vxr2,vyr2)) and (bxi > 0) and (byi > 0) and (cut_3c(bxi,byi,xm2,ym2)):
			bx = numpy.append(bx,bxi)
			by = numpy.append(by,byi)

			break
		
f = open ('dataset_elip_02.txt','w')

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


	
