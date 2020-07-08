# %%
import vtk
import numpy as np
import vtk.util.numpy_support as npsup

# wczytywanie danych prosto z kodu
# targetLandmarks = np.array([[1.0, 2.0, 30],
#                             [2.0, 3.0, 50],
#                             [10.0, 20.0, 300.0],
#                             [11.0, 12.0, 130.0],
#                             [21.0, 22.0, 230.0],
#                             ])
# sourceLandmarks = np.array([[1.5, 2.0, 30],
#                             [2.0, 3.5, 50],
#                             [10.0, 20.5, 300.0],
#                             [11.0, 12.0, 135.0],
#                             [21.0, 22.0, 235.0],
#                             ])

# wczytywanie danych z pliku (liczby rozdzielone przecinkiem i spacją, jeśli sama spacja to delimiter=' ')
targetLandmarks = np.loadtxt("input1.txt", dtype='f', delimiter=',')
sourceLandmarks = np.loadtxt("input2.txt", dtype='f', delimiter=',')


vtkTargetLandmarks = vtk.vtkPoints()
vtkTargetLandmarks.SetData(npsup.numpy_to_vtk(targetLandmarks, deep=1))

vtkSourceLandmarks = vtk.vtkPoints()
vtkSourceLandmarks.SetData(npsup.numpy_to_vtk(sourceLandmarks, deep=1))

lmTransform = vtk.vtkLandmarkTransform()
lmTransform.SetTargetLandmarks(vtkTargetLandmarks)
lmTransform.SetSourceLandmarks(vtkSourceLandmarks)

# tutaj ustawić czy może być skalowanie, czy tylko rotacja+translacja
# lmTransform.SetModeToSimilarity()
lmTransform.SetModeToRigidBody()


lmTransform.Update()

result = lmTransform.GetMatrix()

out_string = ''
for row in range(4):
    for col in range(4):
        out_string += str(result.GetElement(row, col)) + " "
    out_string += '\n'

# wyświetl  na ekran
print(out_string)
# zapisz do pliku
fout = open('wynik.txt', 'a')
fout.write(out_string + "\n")
fout.close()