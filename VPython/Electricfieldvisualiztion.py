from vpython import *
cyl=cylinder(pos=vector(-2,0,0),color=color.white,radius=1,axis=vector(4,0,0))
cr1=shapes.circle(radius=2,thickness=0.1)
extrusion(path=[vector(0,0,0),vector(0.1,0,0)],shape=cr1,pos=vector(2,0,0))
cr2=shapes.circle(radius=2,thickness=0.1)
extrusion(path=[vector(0,0,0),vector(0.1,0,0)],shape=cr2,pos=vector(-2,0,0))
l1=shapes.line(start=(1,0),end=(5,0))
extrusion(path=[vector(0,0,0),vector(0,0,0.1)],shape=l1,pos=vector(0,2,0))
l2=shapes.line(start=(1,0),end=(5,0))
extrusion(path=[vector(0,0,0),vector(0,0,0.1)],shape=l2,pos=vector(0,-2,0))
i=0;
particle=[]
Ncharges=10
phi=0
L=4
while i<Ncharges:
    rate(50)
    x=L*cos(phi)*random()
    y=L*sin(phi)*random()
    z=L
    particle.append(simple_sphere(pos=vector(x,y,z),textures='https://imgur.com/gallery/dsaT85K?nc=1',radius=0.1))
    phi=phi+2*pi
while True:
    pass

