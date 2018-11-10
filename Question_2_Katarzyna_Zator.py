#Kate Zator's second proper Python programme:  PES and vib. freq. predictor
from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import os

#inputting data and making it into a matrix
water_path = input("Please key in the path to the directory: ")

no_water_files = len([item for item in os.listdir(water_path) if os.path.isfile(os.path.join(water_path, item))])
water = zeros((no_water_files,3))
i = 0
 
for file in os.listdir(water_path):
    if file.endswith(".out"):
        n = open(os.path.join(water_path, file), "r")
        #reads in values for the matrix; dof for degree of freedom
        for line in n:
            if "Input=" in line:
                dof = line
                water[i][0] = dof[12:16]
                water[i][1] = dof[21:25]
            elif "A.U." in line:
                en = line.split()
                water[i][2] = en[4]
            else:
                pass
        i += 1
        n.close()
        
#plotting the potential energy surface
fig = plt.figure(figsize=(10,9))
ax = plt.axes(projection='3d')
X = reshape(water[:,0], (25, 91)) #plot_surface requires 2D arrays
Y = reshape(water[:,1], (25, 91))
Z = reshape(water[:,2], (25, 91))
pl = Axes3D.plot_surface(ax, X, Y, Z, cmap=cm.coolwarm, linewidth=0)
ax.set_xlim3d(0.6, 1.9)
ax.set_ylim3d(70, 160)
cb = fig.colorbar(pl, shrink=0.5)
ax.set_xlabel('X - H bond length / ${\AA}$')
ax.set_ylabel('Angle / degrees')
ax.set_zlabel('Energy / Hartree')
ax.set_title('Potential Energy Surface for H2X')
cset = ax.contour(X, Y, Z, zdir='z', offset=-76, cmap=cm.coolwarm)
ax.view_init(40, 70)
plt.savefig("Potential Energy Surface for H2X.jpg")
plt.show()

#finding an equilibrium geometry
min_en = water[:,2].min()
min_r = water[water[:,2].tolist().index(min_en), 0]
min_angle = water[water[:,2].tolist().index(min_en), 1]

def get_k(min_value, row_value, row_other, no_points_to_fit):
    '''fitting to find the constants, k(r), k(theta)'''
    m_subset = empty([1,2])
    for i in range (no_water_files):
        if water[i, row_value] == min_value:
            m_subset = vstack([m_subset, array([water[i, row_other], water[i,2]])])
    m_subset = delete(m_subset, (0), axis=0)
    centre = m_subset[:,1].tolist().index(min_en)
    fitting_m = empty([1,2])
    for i in range (-no_points_to_fit, no_points_to_fit + 1):
        fitting_m = vstack([fitting_m, m_subset[centre + i, :]])
    fitting_m = delete(fitting_m, (0), axis=0)
    p = polyfit(fitting_m[:,0], fitting_m[:,1], 2)
    k = 2 * p[0]
    return k

k_r = get_k(min_angle,1,0,2) #I assumed 'aroud minimum' to mean 1 A and 2 degrees away each side
k_theta = get_k(min_r,0,1,5)

v_stretch = (1/(2*pi)) * sqrt((k_r * 4.35974 * 6.0221415)/2) * 3335.6
v_bend = (1/(2*pi)) * sqrt((k_theta * 4.35974 * 6.0221415)* 2/power(min_r, 2)) * 3.3356 * power(10,3) * 180/pi
print("The symmetric stretch is ", v_stretch, "cm^-1 and the degenerate bend is", v_bend, "cm^-1.")