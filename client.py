from socket import*
import sys
server_host= sys.argv[1]
server_port= int(sys.argv[2])
filename= sys.argv[3]

clientSocket= socket(AF_INET, SOCK_STREAM)

try:
	clientSocket.connect((server_host, server_port))
	
	request= f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
	clientSocket.send(request.encode())
	response= clientSocket.recv(4096).decode()
	
	
	print(response)

except error as e:
	print(f"Error al contactar con el server: {e}")
finally:
	clientSocket.close()
