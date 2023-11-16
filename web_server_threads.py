from socket import *
import sys 
import threading

#Funcion que maneja las solicitudes en un hilo separado
def handle_request(connectionSocket):
	try:
		#Recibir mensaje de solicitud
		message= connectionSocket.recv(1024).decode()
		filename= message.split()[1]
		#Abrir el archivo solicitado
		with open(filename[1:],"rb") as f:
			outputdata= f.read()
		#Enviar la linea de encabezado HTTP al socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
		#Enviar contenido del archivo solicitado al cliente
		connectionSocket.sendall(outputdata)
		connectionSocket.close()
	except IOError:
		#Enviar un mensaje d archivo no encontrado
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
		connectionSocket.close()
#Funcion para aceptar  solicitudes y manejarlas en un hilo separado
def accept_and_handle_requests():
	while True:
		#Crear conexion
		connectionSocket,addr= serverSocket.accept()
		#Crear un nuevo hilo para manejar la solicitud
		request_Handler_thread= threading.Thread(target=handle_request,	args=(connectionSocket,))
		request_Handler_thread.start()
	#Crear un hilo para aceptar y manejar solicitudes
	main_thread= threading.Thread(target= accept_and_handle_requests)
	main_thread.start()

	
#Crear socket de server
serverSocket = socket(AF_INET,SOCK_STREAM)

serverPort=6789
serverSocket.bind(('',serverPort))

serverSocket.listen(1)
print('El servidor esta listo para recibir solicitudes')
accept_and_handle_requests()

