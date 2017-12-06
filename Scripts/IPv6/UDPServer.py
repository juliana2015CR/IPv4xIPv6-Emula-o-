import socket
import sys
class UDPServer():
	def __init__(self):
		self.HOST = '2001:72::10'              # Endereco IP do Servidor
		self.PORT = 5000            # Porta que o Servidor esta
		self.udp = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
		self.orig = (self.HOST, self.PORT)
		self.udp.bind(self.orig)
		self.loop()
	def getRequest(self):
		msg, self.cliente = self.udp.recvfrom(2048)
		#print self.cliente, msg
		#return 
		return msg
	def sendReply(self, resposta):
		self.udp.sendto(resposta,self.cliente)
	def loop(self):	
		while True:
			requisicao = self.getRequest();
			
			self.sendReply(requisicao)
		    
		self.udp.close()
UDPServer()
