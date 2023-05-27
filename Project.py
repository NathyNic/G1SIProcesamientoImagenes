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

# Dividir la imagen en 2 partes

partesuperior = imagen[:mitad_alto, :ancho]
parteinferior = imagen[mitad_alto:, :ancho]

# Divide la parte superior en dos partes
parte_superior_izquierda = partesuperior[:, :mitad_ancho]
parte_superior_derecha = partesuperior[:, mitad_ancho:]

# Realiza la traslación en x e y de las partes superiores
#traslacion_x = ancho - (mitad_ancho)
#traslacion_y = 0

#parte_superior_izquierda_traslada = np.roll(parte_superior_izquierda, traslacion_x, axis=1)
#parte_superior_derecha_traslada = np.roll(parte_superior_derecha, -traslacion_x, axis=1)

# Intercambia las partes superiores entre sí
parte_superior_izquierda, parte_superior_derecha = parte_superior_derecha, parte_superior_izquierda

# Voltea la mitad inferior vertical y horizontalmente
parte_inferior_volteada = cv2.flip(parteinferior, -1)

# Combina las dos partes de la imagen
#imagen_semifinal = np.concatenate((parte_superior_derecha_traslada, parte_superior_izquierda_traslada), axis=1)
imagen_semifinal = np.concatenate((parte_superior_izquierda, parte_superior_derecha), axis=1)
imagen_final = np.concatenate((imagen_semifinal, parte_inferior_volteada), axis=0)

# Muestra la imagen original y la imagen final
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Final", imagen_final)
cv2.waitKey(0)
cv2.destroyAllWindows()