#Kate Zator's first proper Python programme: A general Huckel solver
import numpy as np

#interface menu to decide what to calcuate:
print("Hello, which pi energy would you like to calculate?:")
print("1 - linear poly-ene,")
print("2 - cyclic poly-ene,")
print("3 - tetrahedron,")
print("4 - cube, or")
print("5 - dodecahedron")
print("6 - buckminsterfullerene")
print("7 - exit")
choice = int(input("Please key in the corresponding number:"))

def get_eigenvalues(M):
    #calculates eigenvalues and eigenvectors as nd.arrays
    evals, evecs = np.linalg.eig(M)
    #recognises degeneracies and creates dictionary of energies:degeneracies
    j = 0
    unique = {}
    while j < n:
        non_unique = np.isclose(evals[j],evals[j+1:])
        if np.isclose(np.array(list((unique.keys()))), evals[j]).any() == True:
            pass
        elif non_unique.any() == True:            
            unique[evals[j]] = sum(non_unique) + 1
        else:
            unique[evals[j]] = 1
        j = j + 1    
    #prints out energies
    i = 0
    for i in range(len(unique)):         
        print('orbital(s) of energy', '%.2f' % np.array(list((unique.keys())))[i],
               'and degeneracy of', np.array(list((unique.values())))[i])
        i = i + 1
    return

if choice == 1:
    #case 1) linear poly-enes
    n = int(input ('Please input an integer number of atoms, n:'))
    print('The linear molecule has a series of', n, 'molecular orbitals, which are:')
    Mat = np.zeros((n,n))
    i = 0
    while i < n-1:
        Mat[i][i+1] = -1
        Mat[i+1][i] = -1
        i = i + 1
    get_eigenvalues(Mat)

elif choice == 2:
    #case 2) cyclic poly-enes
    n = int(input ('Please input an integer number of atoms, n:'))
    print('The cyclic molecule has a series of', n, 'molecular orbitals, which are:')
    Mat = np.zeros((n,n))
    i = 0
    while i < n-1:
        Mat[i][i+1] = -1
        Mat[i+1][i] = -1
        i = i + 1
    Mat[0][n-1] = -1
    Mat[n-1][0] = -1
    get_eigenvalues(Mat)

elif choice == 3:
    #case 3) Platonic solids: tetrahedron
    print('The tetragedral molecule has a series of 4 molecular orbitals, which are:')
    n = 4
    Mat = np.ones((4,4))
    Mat = -Mat
    for i in range(4):
        Mat[i][i] = 0
    get_eigenvalues(Mat)

elif choice == 4:
    #case 4) Platonic solids: cube
    print('The cubic molecule has a series of 8 molecular orbitals, which are:')
    n = 8
    Mat = np.zeros((8,8))
    Mat[0][3] = Mat[3][0] = -1
    Mat[0][4] = Mat[4][0] = -1
    Mat[1][5] = Mat[5][1] = -1
    Mat[2][6] = Mat[6][2] = -1
    Mat[3][7] = Mat[7][3] = -1
    Mat[4][7] = Mat[7][4] = -1
    for i in range(7):
        Mat[i][i+1] = -1
        Mat[i+1][i] = -1
    Mat[3][4] = Mat[4][3] = 0
    get_eigenvalues(Mat)

elif choice == 5:
    #case 5) Platonic solids: dodecahedron
    print('The dodecahedral molecule has a series of 20 molecular orbitals, which are:')
    n = 20
    Mat = np.zeros((20,20))
    Mat[0][4] = Mat[4][0] = -1
    Mat[0][13] = Mat[13][0] = -1
    Mat[1][11] = Mat[11][1] = -1
    Mat[2][9] = Mat[9][2] = -1
    Mat[3][7] = Mat[7][3] = -1
    Mat[5][14] = Mat[14][5] = -1
    Mat[6][16] = Mat[16][6] = -1
    Mat[8][17] = Mat[17][8] = -1
    Mat[10][18] = Mat[18][10] = -1
    Mat[12][19] = Mat[19][12] = -1
    Mat[15][19] = Mat[19][15] = -1
    for i in range(19):
        Mat[i][i+1] = -1
        Mat[i+1][i] = -1
    get_eigenvalues(Mat)
    
elif choice == 6:
    #case 6) Platonic solids: buckminsterfullerene
    print('The buckminsterfullerene molecule has a series of 60 molecular orbitals, which are:')
    n = 60
    Mat = np.zeros((60,60))
    Mat[0][5] = Mat[5][0] = -1
    Mat[0][18] = Mat[18][0] = -1
    Mat[1][16] = Mat[16][1] = -1
    Mat[2][13] = Mat[13][2] = -1
    Mat[3][11] = Mat[11][3] = -1
    Mat[4][8] = Mat[8][4] = -1
    Mat[6][20] = Mat[20][6] = -1
    Mat[7][23] = Mat[23][7] = -1
    Mat[9][25] = Mat[25][9] = -1
    Mat[10][27] = Mat[27][10] = -1
    Mat[12][29] = Mat[29][12] = -1
    Mat[14][31] = Mat[31][14] = -1
    Mat[15][33] = Mat[33][15] = -1
    Mat[17][35] = Mat[35][17] = -1
    Mat[19][37] = Mat[37][19] = -1
    Mat[21][38] = Mat[38][21] = -1
    Mat[22][52] = Mat[52][22] = -1
    Mat[24][51] = Mat[51][24] = -1
    Mat[26][49] = Mat[49][26] = -1
    Mat[28][47] = Mat[47][28] = -1
    Mat[30][46] = Mat[46][30] = -1
    Mat[32][44] = Mat[44][32] = -1
    Mat[34][42] = Mat[42][34] = -1    
    Mat[36][41] = Mat[41][36] = -1
    Mat[56][43] = Mat[56][43] = -1
    Mat[48][58] = Mat[58][48] = -1
    Mat[40][55] = Mat[55][40] = -1
    Mat[45][57] = Mat[57][45] = -1
    Mat[50][59] = Mat[59][50] = -1
    Mat[54][59] = Mat[59][54] = -1
    Mat[53][39] = Mat[39][53] = -1
    for i in range(59):
        Mat[i][i+1] = -1
        Mat[i+1][i] = -1
    get_eigenvalues(Mat)

else: 
    print("Goodbye! Enjoy solving other chemical problems!")