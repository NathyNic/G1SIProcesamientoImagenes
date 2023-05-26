import cv2 ## Importamos la librería OPENCV

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

# Dividir la imagen en 4 partes
parte1 = imagen[:mitad_alto, :mitad_ancho]
parte2 = imagen[:mitad_alto, mitad_ancho:]
parte3 = imagen[mitad_alto:, :mitad_ancho]
parte4 = imagen[mitad_alto:, mitad_ancho:]