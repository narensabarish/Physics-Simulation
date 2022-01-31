import vpython as vp
import pandas as pd
import astropy as ap
Gs=1
G=6.67e-11
vp.scene.autoscale=False
bg=vp.sphere(radius=70,shininess=0,color=vp.color.orange)
vp.scene.range=15
sun=vp.sphere(pos=vp.vector(0,0,0),texture='https://i.imgur.com/PWnSJQd.jpg',mass=1000,radius=2.5,momentum=vp.vector(0,0,0))
mercury=vp.sphere(pos=vp.vector(4,0,0),texture='https://i.imgur.com/SLgVbwD.jpg',radius=0.3,mass=0.330,momentum=vp.vector(0,50,0))
venus=vp.sphere(pos=vp.vector(7,0,0),texture='https://i.imgur.com/7A1m7IY.jpgg',radius=0.7,mass=4.87,momentum=vp.vector(0,45,0))
earth=vp.sphere(pos=vp.vector(10,0,0),texture=vp.textures.earth,radius=0.75,mass=5.79,momentum=vp.vector(20,0,0))
mars=vp.sphere(pos=vp.vector(15,0,0),texture='https://i.imgur.com/e2pP7Ma.jpg',radius=0.4,mass=0.642,momentum=vp.vector(-20,30,0))
jupiter=vp.sphere(pos=vp.vector(20,0,0),texture='https://i.imgur.com/yygNA8D.jpg',radius=1.6,mass=200,momentum=vp.vector(0,30,10))
satur=vp.sphere(pos=vp.vector(25,0,0),texture='https://image.shutterstock.com/image-illustration/saturn-ring-background-texture-3d-260nw-1856278243.jpg',radius=1.2,mass=170,momentum=vp.vector(20,10,-10))
rins=vp.ring(pos=vp.vector(25,0,0),radius=1.4,texture='https://blenderartists.org/uploads/default/original/4X/d/f/d/dfda2d1cabfa176fe1c415208deea3b30be87eb0.jpg',thickness=0.1,axis=vp.vector(0,1,0))
saturn=vp.compound([satur,rins])
uranus=vp.sphere(pos=vp.vector(30,0,0),radius=0.8,texture='https://i.imgur.com/2kZNvFw.jpg',mass=86.8,momentum=vp.vector(25,-15,0))
neptune=vp.sphere(pos=vp.vector(35,0,0),radius=0.9,texture='https://i.imgur.com/lyLpoMk.jpg',mass=102,momentum=vp.vector(-18,30,0))
print('Hi')
def Gforce(g1,g2):
   rvec=g2.pos-g1.pos
   rmag=vp.mag(rvec)
   rhat=rvec/rmag
   GFs=-(Gs*g1.mass*g2.mass)/(rmag)**2
   force=GFs*(rhat)
   GFscaled=(GFs)*G
   return force
def Gpe(g1,g2):
    rvec=g2.pos-g1.pos
    rmag=vp.mag(rvec)
    rhat=rvec/rmag
    Pot=-(Gs*g1.mass*g2.mass)/rmag
    return Pot
def Ke(g1):
     Kine=1/2*g1.mass*(g1.pos.x/dt)**2
     return Kine

#EULER CROMER ANIMATION
i=0;
t=0;
dt=0.0001;
while True:
    vp.rate(1000)
     #Total force
    sun.force=Gforce(sun,mercury)+Gforce(sun,venus)+Gforce(sun,earth)+Gforce(sun,mars)+Gforce(sun,jupiter)+Gforce(sun,saturn)+Gforce(sun,uranus)+Gforce(sun,neptune)
    mercury.force=Gforce(sun,mercury)+Gforce(mercury,venus)+Gforce(mercury,earth)+Gforce(mercury,mars)+Gforce(mercury,jupiter)+Gforce(mercury,saturn)+Gforce(mercury,uranus)+Gforce(mercury,neptune)
    venus.force=Gforce(venus,sun)+Gforce(venus,mercury)+Gforce(venus,earth)+Gforce(venus,mars)+Gforce(venus,jupiter)+Gforce(venus,saturn)+Gforce(venus,uranus)+Gforce(venus,neptune)
    earth.force=Gforce(earth,sun)+Gforce(earth,venus)+Gforce(earth,mars)+Gforce(earth,jupiter)+Gforce(earth,saturn)+Gforce(earth,uranus)+Gforce(earth,neptune)+Gforce(earth,mercury)
    mars.force=Gforce(mars,mercury)+Gforce(mars,venus)+Gforce(mars,earth)+Gforce(mars,sun)+Gforce(mars,jupiter)+Gforce(mars,saturn)+Gforce(mars,uranus)+Gforce(mars,neptune)
    jupiter.force=Gforce(jupiter,sun)+Gforce(jupiter,venus)+Gforce(jupiter,earth)+Gforce(jupiter,mars)+Gforce(jupiter,saturn)+Gforce(jupiter,uranus)+Gforce(jupiter,neptune)+Gforce(jupiter,mercury)
    saturn.force=Gforce(saturn,sun)+Gforce(saturn,venus)+Gforce(saturn,earth)+Gforce(saturn,mars)+Gforce(saturn,mercury)+Gforce(saturn,uranus)+Gforce(saturn,neptune)+Gforce(jupiter,saturn)
    uranus.force=Gforce(uranus,sun)+Gforce(uranus,mercury)+Gforce(uranus,venus)+Gforce(uranus,earth)+Gforce(uranus,mars)+Gforce(uranus,jupiter)+Gforce(uranus,saturn)+Gforce(uranus,neptune)
    neptune.force=Gforce(neptune,sun)+Gforce(neptune,mercury)+Gforce(neptune,venus)+Gforce(neptune,earth)+Gforce(neptune,mars)+Gforce(neptune,jupiter)+Gforce(neptune,saturn)+Gforce(neptune,uranus)
     #Euler cromer for momentum
    sun.momentum=sun.momentum+sun.force*dt
    mercury.momentum=mercury.momentum+sun.force*dt
    venus.momentum=venus.momentum+venus.force*dt
    earth.momentum=earth.momentum+earth.force*dt
    mars.momentum=mars.momentum+mars.force*dt
    jupiter.momentum=jupiter.momentum+jupiter.force*dt
    saturn.momentum=saturn.momentum+saturn.force*dt
    uranus.momentum=uranus.momentum+uranus.force*dt
    neptune.momentum=neptune.momentum+neptune.force*dt
     #Euler cromer for position
    sun.pos=sun.pos+sun.momentum/sun.mass*dt
    t=t+dt
while True:
    pass






    







