from numpy import sqrt, sin, cos

''' IT'S WORKING '''

''' I think I could compare the trajectories given by Newton's mechanics, and Einstein's,
    as seen from a moving inertial frame.''' 

''' The idea of this program is to visualize the effects like length contraction
    this can be done if we plot the subsequent positions of particles, for exemple,
    in different reference frames '''

c = 299792458

def gamma(v): 
    return 1/sqrt(1-(v*v)/(c*c))

def lorentzTransformations(s, v):

    '''Position in S' reference frame'''
    sPrime = []
    sPrime.append(gamma(v)*(s[0]-(v*s[1])/(c*c)))
    sPrime.append(gamma(v)*(s[1]-(v*s[1])/c))
    sPrime.append(s[2])
    sPrime.append(s[3])

    return sPrime

def velocityAddition(u, v):

    uPrime = []
    '''uPrime.append( gamma*(u[0]-(v*s[1])/(c*c)) )'''
    uPrime.append( (u[0]-v)/(1-(v*u[0])/(c*c)) )
    uPrime.append( u[1]/(gamma(v)*(1-(v*u[0])/(c*c))) )
    uPrime.append( u[2]/(gamma(v)*(1-(v*u[0])/(c*c))) )

    return uPrime

'''four vector position'''
t = 0
x = 0
y = 0
z = 0
s = [c*t, x, y, z]
sPrime = [x, y, z]
sNewton = [x, y, z]

'''relative velocity between frames'''
v = 0.65*c
dt = 0.001

'''tri vector velocity'''
ux = sin(t)
uy = cos(t)
uz = 1
u = [ux, uy, uz]

f = open("S_Positions.txt", "a")
g = open("SPrime_Positions.txt", "a")
h = open("SPrimeNewton_Positions.txt", "a")

f.write(str(x) + " " + str(y) + " " + str(z) + "\n")
g.write(str(x) + " " + str(y) + " " + str(z) + "\n")
h.write(str(x) + " " + str(y) + " " + str(z) + "\n")

while t<6:
    t = t + dt

    ux = sin(t)
    uy = cos(t)
    u = [ux, uy, uz]

    xPrevious = s[1]

    '''New position in S reference frame'''
    s = [c*dt, s[1] + ux*dt, s[2] + uy*dt, s[3] + uz*dt]

    xNext = s[1]

    '''New position in S' reference frame by Newton's Mechanics'''
    sNewton = [sNewton[0]+(ux-v)*dt, sNewton[1]+uy*dt, sNewton[2]+uz*dt]

    h.write(str(sNewton[0]) + " " + str(sNewton[1]) + " " + str(sNewton[2]) + "\n")

    dtPrime = gamma(v)*(dt-(v*(xNext-xPrevious))/(c*c))

    '''Equivalent position in S' reference frame
    sPrime = lorentzTransformations(s, v)'''

    '''Velocity of the particle at new time t, seen from S' '''
    uPrime = velocityAddition(u, v)

    '''New position in S' reference frame'''
    sPrime = [sPrime[0]+uPrime[0]*dtPrime, sPrime[1]+uPrime[1]*dtPrime, sPrime[2]+uPrime[2]*dtPrime]

    f.write(str(s[1]) + " " + str(s[2]) + " " + str(s[3]) + "\n")
    g.write(str(sPrime[0]) + " " + str(sPrime[1]) + " " + str(sPrime[2]) + "\n")

f.close()
g.close()
h.close()