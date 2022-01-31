
#from sympy import symbols, cos , diff , sin , exp
import sympy as sp
#from pylab import*
import vpython as vp
spring=vp.helix(pos=vp.vector(-2,0,0),radius=0.2,color=vp.color.orange,axis=vp.vector(3,0,0),coils=25)
particle=vp.sphere(pos=vp.vector(1,0,0),color=vp.color.purple,radius=0.4,mass=1)
stiffness=1
momentum=vp.vector(0,0,0)
dt=0.05
hbar=1e-34
w=vp.sqrt(stiffness/particle.mass)
g1=vp.graph(xtitle='position',ytitle='Energy',fast=False)
g2=vp.graph(xtitle='Potential',ytitle='position')
g3=vp.graph(xtitle='wavefunction',ytitle='position')
Egraph=vp.gcurve(color=vp.color.orange,graph=g1)
Pgraph=vp.gcurve(color=vp.color.purple,graph=g2)
Psigraph=vp.gcurve(color=vp.color.blue,graph=g3)
#Euler Cromer Method
def Animation():
    i=0;
    A=sp.sqrt(1/((2**i)*(sp.factorial(i))))
    A0=((particle.mass*(w)/(sp.pi*hbar))**(1/4))
    Eterm=sp.exp((particle.mass*w*(particle.pos.x)**2)/(hbar))
    Eterm2=sp.exp(-((particle.mass*w*(particle.pos.x)**2)/(2*hbar)))
    while(i<=2000):
        vp.rate(50)
        Force=-(stiffness)*(particle.pos.x)
        momentum.x=momentum.x+(Force)*dt
        particle.pos.x=particle.pos.x+(momentum.x/particle.mass)*dt
        spring.axis.x=spring.axis.x+(momentum.x/particle.mass)*dt      
        En=(1/2)*particle.mass*(w**2)*(particle.pos.x)**2
        #Psin=A*A0*sp.exp(particle.mass*w*(particle.pos)**2/(hbar))*Hermitefn
        Egraph.plot(pos=(particle.pos.x,En))
        print(En)
        i=i+1
b1=vp.button(bind=Animation,text='Click me to Start',color=vp.color.orange)
print('Hi')
