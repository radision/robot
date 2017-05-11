""" 心跳客户端,周期性的发送 UDP包 """
import socket, time
SERVER_IP = '139.162.84.223'; SERVER_PORT = 40206; BEAT_PERIOD = 5

print 'Sending heartbeat to IP %s , port %d' % (SERVER_IP, SERVER_PORT)
print 'press Ctrl-C to stop'
while True:
    hbSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hbSocket.sendto('PyHB', (SERVER_IP, SERVER_PORT))
    time.sleep(BEAT_PERIOD)
