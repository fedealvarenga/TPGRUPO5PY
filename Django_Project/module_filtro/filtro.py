import cv2
import imutils

# Videostreaming o video de entrada
captura_video = cv2.VideoCapture(0)
#leo la imagen
imagen = cv2.imread("d:/Curso python/filtro/minnie.png", cv2.IMREAD_UNCHANGED)# me da 4 canales y el 4to es el fondo transparente del png

# Detector de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:

	bol, frame = captura_video.read()
	frame = imutils.resize(frame, width=640) #para que no me ocupe toda la pantalla
	# Detecto las caras del video
	rostros = faceClassif.detectMultiScale(frame, 1.3, 5)

	for (x, y, w, h) in rostros:
		#redimenciono la imagen para que se adepte al rectangulo creado pro el rostro detectado
		imagen_redimensionada = imutils.resize(imagen, width=w)
		filas_image = imagen_redimensionada.shape[0]#shape me da una tupla con el tamaño del array
		col_image = w
		# Agarro una parte de la cara para que la imagen no quede muy arriba
		porcion_alto = filas_image // 4
		dif = 0
		#Me fijo si la imagen entra en el video
		if y + porcion_alto - filas_image >= 0:
			pos_imagen = frame[y + porcion_alto - filas_image : y + porcion_alto,
				x : x + col_image]
		else:
			#Calculo lo que sobrepasa la imagen el recuadro de la camara
			dif = abs(y + porcion_alto - filas_image) 
			pos_imagen = frame[0 : y + porcion_alto,
				x : x + col_image]
		#Hago que la imagen no muestre el fondo blanco del png
		#Solo agarro el fondo de la imagen (lo pone en negro)
		fondo_imagen = imagen_redimensionada[:, :, 3]
		#invierto por lo tanto solo tomo la imagen que me interesa (en negro)
		fondo_imagen_inv = cv2.bitwise_not(fondo_imagen)
		#uno las 2 imagenes anteriores para formar la imagen pero con fondo negro y color
		fondo_negro = cv2.bitwise_and(imagen_redimensionada, imagen_redimensionada, mask=fondo_imagen)
		fondo_negro = fondo_negro[dif:, :, 0:3] #no tomo todos los canales de la imagen porq osino rompe
		#hago que el fondo negro sea transparente
		fondo_transparente = cv2.bitwise_and(pos_imagen,pos_imagen, mask=fondo_imagen_inv[dif:,:])
		# Sumamos las dos imágenes obtenidas
		imagen_filtro = cv2.add(fondo_negro, fondo_transparente)
		if y + porcion_alto - filas_image >= 0:
			frame[y + porcion_alto - filas_image : y + porcion_alto, x : x + col_image] = imagen_filtro

		else:
			frame[0 : y + porcion_alto, x : x + col_image] = imagen_filtro
		
	cv2.imshow('frame',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
captura_video.release()
cv2.destroyAllWindows()