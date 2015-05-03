import math, numpy, sys
import matplotlib.pyplot as pplot

# Read input, optional last argument plots errors instead of values
filename = sys.argv[1]
initialx = float(sys.argv[2])
initialv = float(sys.argv[3])
step = float(sys.argv[4])
cycles = int(sys.argv[5])
plottype = sys.argv[6]

def nextx(oldx, oldv, h):
	return oldx + h*oldv

def nextv(oldx, oldv, h):
	return oldv - h*oldx

def oscillate(startx, startv, h, laps):
	counter = 0
	position = 0
	x = [startx]
	v = [startv]
	time = [0]
	while(counter < laps):
		x.append(nextx(x[position],v[position],h))
		v.append(nextv(x[position],v[position],h))
		position += 1
		time.append(position*h)
		if(x[position] >= startx and x[position-1] < startx):
			counter += 1
	return [x,v,time]

def computeimplicites(startx, startv, h, laps):
	counter = 0
	p = 0
	x = [startx]
	v = [startv]
	time = [0]
	while(counter < laps):
		v.append((v[p]-h*x[p])/(1+h*h))
		x.append((h*v[p] + x[p])/(1+h*h))
		p += 1
		time.append(p*h)
		if(x[p] >= startx and x[p-1] < startx):
			counter += 1
	return [x,v,time]

def symplecticeuler(startx, startv, h, laps):
	counter = 0
	p = 0
	x = [startx]
	v = [startv]
	time = [0]
	while(counter < laps):
		v.append((1-h*h)*v[p] - h*x[p])
		x.append(x[p] + h*v[p])
		p += 1
		time.append(p*h)
		if(x[p] >= startx and x[p-1] < startx):
			counter += 1
	return [x,v,time]

def computereals(xamp,vamp,omega,h,steps):
	x = []
	v = []
	t = []
	for i in range(steps):
		x.append(xamp*math.sin(omega*h*i))
		v.append(vamp*math.cos(omega*h*i))
		t.append(h*i)
	return [x,v,t]

if(plottype == "plot"):
	numericals = oscillate(initialx, initialv, step, cycles)
	pplot.plot(numericals[2],numericals[0],c='g')
	pplot.plot(numericals[2],numericals[1],c='r')
	pplot.title("Position (green) and velocity (red) for a mass on a spring")
	pplot.xlabel("time")
	pplot.ylabel("Position/Velocity")
	pplot.savefig(filename)
elif(plottype == "errors"):
	numericals = oscillate(initialx, initialv, step, cycles)
	reals = computereals(1,1,1,step,len(numericals[0]))
	errors = [[],[],[]]
	errors[0] = [reals[0][i] - numericals[0][i] for i in range(len(reals[0]))]
	errors[1] = [reals[1][i] - numericals[1][i] for i in range(len(reals[1]))]
	errors[2] = reals[2]
	pplot.plot(errors[2],errors[0],c='g')
	pplot.plot(errors[2],errors[1],c='r')
	pplot.title("Position (green) and velocity (red) error in euler's method")
	pplot.xlabel("time")
	pplot.ylabel("errors")
	pplot.savefig(filename)
elif(plottype == "hcomparison"):
	thingstoplot = [[],[]]
	hs = [step, step/2, step/4, step/8, step/16]
	for i in range(len(hs)):
		numerical = oscillate(initialx, initialv, hs[i], cycles)
		real = computereals(1,1,1,hs[i],len(numerical[0]))
		error = [[],[],[]]
		error[0] = [real[0][i] - numerical[0][i] for i in range(len(real[0]))]
		error[1] = [real[1][i] - numerical[1][i] for i in range(len(real[1]))]
		thingstoplot[0].append(max(error[0]))
		thingstoplot[1].append(max(error[1]))
	pplot.plot(hs,thingstoplot[0],c='g')
	pplot.plot(hs,thingstoplot[1],c='r')
	pplot.title("Maximum error vs step size, xerror in green and verror in red")
	pplot.xlabel("Step size")
	pplot.ylabel("Maximum error")
	pplot.savefig(filename)
elif(plottype == "energy"):
	numericals = oscillate(initialx, initialv, step, cycles)
	energies = [numericals[0][i]**2 + numericals[1][i]**2 for i in range(len(numericals[0]))]
	pplot.plot(numericals[2], energies)
	pplot.title("Evolution of total energy over time, should be constant")
	pplot.xlabel("Time")
	pplot.ylabel("Normalized total energy")
	pplot.savefig(filename)
elif(plottype == "impliciterror"):
	numericals = oscillate(initialx, initialv, step, cycles)
	implicites = computeimplicites(initialx,initialv,step,cycles)
	reals = computereals(1,1,1,step,len(numericals[0]))
	impreals = computereals(1,1,1,step,len(implicites[0]))
	errors = [[],[],[],[]]
	errors[0] = [reals[0][i] - numericals[0][i] for i in range(len(reals[0]))]
	errors[1] = [reals[1][i] - numericals[1][i] for i in range(len(reals[1]))]
	errors[2] = [impreals[0][i] - implicites[0][i] for i in range(len(impreals[0]))]
	errors[3] = [impreals[1][i] - implicites[1][i] for i in range(len(impreals[1]))]
	pplot.plot(reals[2],errors[0],c='g')
	pplot.plot(reals[2],errors[1],c='r')
	pplot.plot(impreals[2],errors[2],c='c')
	pplot.plot(impreals[2],errors[3],c='y')
	pplot.title("Explicit position (g), velocity (r), Implicity position(b), velocity(y) errors")
	pplot.xlabel("time")
	pplot.ylabel("errors")
#	pplot.axis([0,35,-.002,.002])
	pplot.savefig(filename)
elif(plottype == "expphase"):
	numericals = oscillate(initialx, initialv, step, cycles)
	pplot.plot(numericals[0],numericals[1],c='g')
	pplot.title("Position vs Velocity for explicit Euler method")
	pplot.xlabel("Position")
	pplot.ylabel("Velocity")
	pplot.savefig(filename)
elif(plottype == "impphase"):
	implicites = computeimplicites(initialx, initialv, step, cycles)
	pplot.plot(implicites[0],implicites[1],c='g')
	pplot.title("Position vs Velocity for implicit Euler method")
	pplot.xlabel("Position")
	pplot.ylabel("Velocity")
	pplot.savefig(filename)
elif(plottype == "symphase"):
	positions = symplecticeuler(initialx, initialv, step, cycles)
	pplot.plot(positions[0],positions[1],c='g')
	pplot.title("Position vs Velocity for symplectic Euler method")
	pplot.xlabel("Position")
	pplot.ylabel("Velocity")
	pplot.savefig(filename)
elif(plottype == "symenergy"):
	positions = symplecticeuler(initialx, initialv, step, cycles)
	energies = [positions[0][i]**2 + positions[1][i]**2 for i in range(len(positions[0]))]
	pplot.plot(positions[2], energies)
	pplot.title("Evolution of total energy over time for symplectic Euler method")
	pplot.xlabel("Time")
	pplot.ylabel("Normalized total energy")
	pplot.savefig(filename)
elif(plottype == "phasecheck"):
	symplects = symplecticeuler(initialx,initialv,step,1000*cycles)
	reals = computereals(1,1,1,step,len(symplects[0]))
	length = len(symplects[0])
	start = int(length/1000)*999
	pplot.plot(symplects[2][start:],symplects[0][start:],c='g')
	pplot.plot(reals[2][start:],reals[0][start:],c='r')
	pplot.title("Analytic solution (red) vs symplectic euler method (green), cycles")
	pplot.xlabel("Time")
	pplot.ylabel("Position")
	pplot.savefig(filename)
else:
	print "6th command must be the type of plot, 'plot', 'errors', 'energy', 'implicites', 'expphase', 'symenergy', 'symphase', 'phasecheck', or 'hcomparison'"
