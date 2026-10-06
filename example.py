import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()

ax.axis('equal')
#ax.set(xlim=[-1, 1000], ylim=[-1,1000])

positions = [[0, 1000], [0,0]]

def get_new_position(masses,positions,vitesses,dt):
    X = positions[0]
    Y = positions[1]
    Vx = vitesses[0]
    Vy = vitesses[1]
    
    newX += Vx*dt
    newY += Vy*dt
    new_positions = np.array([newX,newY])

    tab_masses = (masses*np.ones((n,n))) * (np.transpose(masses)*np.ones((n,n))) # en position i,j : mi*mj

    positions = np.transpose(positions)
    colonnes = positions*(np.ones((4,4))[:,:,np.newaxis]) # en position i,j : [xi,yi]
    lignes = np.moveaxis(colonnes,0,1) # en position i,j : [xj,yj]
    distances = lignes - colonnes
    distances = distances**2
    distances = np.sum(distances,axis=2) # en position i,j : distance corps i - corps j au carré
    distances[distances == 0] = np.inf
    Forces = 

    Vx += 




    return [[Xs[0]+1, Xs[1]-1], [Ys[0]+1, Ys[1]+1]]

scat = ax.scatter(positions[0], positions[1])


def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global positions
    positions = get_new_position(positions)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(positions).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=100)
plt.show()
