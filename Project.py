import cv2 ## Importamos la librería OPENCV
import numpy as np

##Utilizando el comando imread de opencv, leeremos la imagen 1.jpeg y la guardaremos en la variable img
imagen = cv2.imread("imagen1.jpg")
## Utilizando el comando imshow de opencv, mostraremos la imagen en una ventana llamada ventana1
#cv2.imshow("ventana1", img)
##Controla el tiempo de muestreo de la señal de entrada por teclado
#cv2.waitKey()
## destruye o cierra las ventanas creadas por opencv
#cv2.destroyAllWindows()
# ##Guardamos la imagen contenida en la variable img en el archivo imagenGuardada1.jpeg
# cv2.imwrite("imagenGuardada1.jpeg", img)

# Obtener las dimensiones de la imagen
alto, ancho = imagen.shape[:2]

# Calcular las coordenadas de los puntos de división
mitad_alto = int(alto / 2)
mitad_ancho = int(ancho / 2)

print(mitad_alto)
print(mitad_ancho)

# Dividir la imagen en 4 partes
#parte1 = imagen[:mitad_alto, :mitad_ancho]
#parte2 = imagen[:mitad_alto, mitad_ancho:]
#parte3 = imagen[mitad_alto:, :mitad_ancho]
#parte4 = imagen[mitad_alto:, mitad_ancho:]

parte1 = imagen[:mitad_alto, :ancho]
parte2 = imagen[mitad_alto:, :ancho]

# Voltea la mitad inferior vertical y horizontalmente
parte_inferior_volteada = cv2.flip(parte2, -1)

# Combina las dos partes de la imagen
imagen_final = np.concatenate((parte1, parte_inferior_volteada), axis=0)

# Muestra la imagen original y la imagen final
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Final", imagen_final)
cv2.waitKey(0)
cv2.destroyAllWindows()