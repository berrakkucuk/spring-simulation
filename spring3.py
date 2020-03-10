from vpython import*

scene = canvas(width=1080,height=720,range=30)

balls=[]
helixs = []

scene.center=vector(0,0,0)

N=27

wallL = box(pos=vector(0, 0, 0), size=vector(0.1, 7, 7), color=color.blue)
balls.append(sphere(pos=vector(0, 0, 0), radius=1, color=color.red, opacity=0))

tt = label(pos=vector(2,15,0),text='Picture3',height=20,color=color.blue,linecolor=color.red)


for i in range(1,N+2):

    if(i==1):
        balls.append(sphere(pos=vector(i * 3 , 0, 0), radius=1, color=color.red))
    elif(i==N):
        balls.append(sphere(pos=vector(i * 3 , 0, 0), radius=1, color=color.red))
    elif(i==N+1):
        wallR = box(pos=vector(i*3, 0, 0), size=vector(0.1, 7, 7), color=color.blue)
        balls.append(sphere(pos=vector(i*3, 0, 0), radius=1, color=color.red, opacity=0))
    else:
        balls.append(sphere(pos=vector(i * 3 , 0, 0), radius=1, color=color.red))
    helixs.append(helix(pos=balls[i-1].pos, axis=balls[i].pos-balls[i-1].pos, radius=1,coils=10, thickness=0.03,
                        color=color.green))

scene.center=balls[len(balls)//2].pos
F=[vector(0,0,0) for i in range(N)]
V=[vector(0,0,0) for i in range(len(balls))]
t=0
dt=0.05
Etop=[0 for i in range(len(helixs))]
for m in range(0, len(helixs)):
    Etop[m] = (1 / 2) * helixs[m].length

V[0]=vector(0,25,0)
sleep(3)
while t<90:
    rate(100)
    for i in range(0,N):

        F[i]=balls[i].pos+balls[i+2].pos-2*(balls[i+1].pos)


    for j in range(0,N):
        V[j] = V[j] + F[j] * dt
        balls[j+1].pos = balls[j+1].pos+ V[j] * dt

    for m in range(0,len(helixs)):

        helixs[m].pos=balls[m].pos
        helixs[m].axis=balls[m+1].pos-balls[m].pos
        Epot2=(1/2)*helixs[m].length
        tt.text='Epot = '+'%f'%(Epot2)+'\n'+'Ekit = '+'%f'%(Epot2-Etop[m])
    t=t+dt