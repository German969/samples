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
		
dcx = 40 # distancia entre centros en x
rx = dcx # radio en x

ry = 5 # radio en y
de = ry # distancia entre clusters en y
dcy = 3*ry # distancia entre centros en y

xc1 = 50 #media en x
yc1 = 10 #distancia elipse mayor
rx1 = rx
ry1 = ry

xc2 = xc1 + dcx
yc2 = yc1 + dcy
rx2 = rx
ry2 = ry

xc3 = xc2 + dcx
yc3 = yc2 + dcy
rx3 = rx
ry3 = ry

n = 500 #tamaño de los clusters

ax = numpy.array([])
ay = numpy.array([])

bx = numpy.array([])
by = numpy.array([])

cx = numpy.array([])
cy = numpy.array([])

def compl_clus(arr_x,arr_y,cen_x,cen_y,rad_x,rad_y):
	for i in range(0,n):
		while True:
			axi = gen_samp(cen_x,rad_x)
			ayi = gen_samp(cen_y,rad_y)
			
			if (dis_r_in(axi,ayi,cen_x,cen_y,rad_x,rad_y)) and (axi > 0) and (ayi > 0):
				arr_x = numpy.append(arr_x,axi)
				arr_y = numpy.append(arr_y,ayi)
				
				break
	return [arr_x,arr_y]

ax = compl_clus(ax,ay,xc1,yc1,rx1,ry1)[0]
ay = compl_clus(ax,ay,xc1,yc1,rx1,ry1)[1]

for i in range(0,n):
	while True:
		bxi = gen_samp(xc2,rx2)
		
		byi = gen_samp(yc2,ry2)

		if (dis_r_in(bxi,byi,xc2,yc2,rx2,ry2)) and (bxi > 0) and (byi > 0):
			bx = numpy.append(bx,bxi)
			by = numpy.append(by,byi)

			break
			
for i in range(0,n):
	while True:
		cxi = gen_samp(xc3,rx3)
		
		cyi = gen_samp(yc3,ry3)

		if (dis_r_in(cxi,cyi,xc3,yc3,rx3,ry3)) and (cxi > 0) and (cyi > 0):
			cx = numpy.append(cx,cxi)
			cy = numpy.append(cy,cyi)

			break
		
f = open ('dataset_elip_03.txt','w')

def write_txt(file,arr_x,arr_y,num):
	for k in range(0,num):
		x = arr_x[k]
		y = arr_y[k]
		s = str(x) + '	' + str(y) + '\n'
		file.write(s)
		
write_txt(f,ax,ay,n)
	
for l in range(0,n):
	x = bx[l]
	y = by[l]
	s = str(x) + '	' + str(y) + '\n'
	f.write(s)
	
for m in range(0,n):
	x = cx[m]
	y = cy[m]
	s = str(x) + '	' + str(y) + '\n'
	f.write(s)
	
f.close()