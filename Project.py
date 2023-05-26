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

# Rotación
grados = 180  # Ángulo de rotación

# Calcular el centro de rotación
centro_rotacion = (mitad_ancho, mitad_alto)

# Realizar rotación en la parte 3
M = cv2.getRotationMatrix2D(centro_rotacion, grados, 1)
parte2_rotacion = cv2.warpAffine(parte2, M, (mitad_ancho, mitad_alto))

# Traslación
#dx = 50  # Desplazamiento horizontal
#dy = 50  # Desplazamiento vertical

# Realizar traslación en la parte 1
#parte1_traslacion = cv2.warpAffine(parte1, np.float32([[1, 0, dx], [0, 1, dy]]), (mitad_ancho, mitad_alto))

# Supongamos que ya tienes las partes modificadas: parte1_traslacion, parte2, parte3_rotacion, parte4

# Obtener las dimensiones de las partes modificadas
alto_parte = parte2_rotacion.shape[0]
ancho_parte = parte2_rotacion.shape[1]

# Crear una imagen vacía del tamaño total
imagen_resultante = np.zeros((alto_parte * 2, 1001, 3), dtype=np.uint8)

# Copiar las partes modificadas en la imagen resultante
imagen_resultante[:alto_parte, :ancho_parte] = parte1
imagen_resultante[:alto_parte, ancho_parte:] = parte2_rotacion


# Mostrar la imagen resultante
cv2.imshow('Imagen resultante', imagen_resultante)
cv2.waitKey(0)
cv2.destroyAllWindows()