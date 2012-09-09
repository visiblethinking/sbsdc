# Echo server program
import socket
import sys
import datetime
   
def get_location(location):
    geo_lat="37.7750 N"
    geo_long = "122.4183 W"  
    return(geo_lat,geo_long)    

HOST = 'visiblethinking.com'                 # Symbolic name meaning the local host
PORT = 13208               # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
	s = socket.socket(af, socktype, proto)
    except socket.error, msg:
	s = None
	continue
    try:
	s.bind(sa)
	s.listen(1)
    except socket.error, msg:
	s.close()
	s = None
	continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    references = data.split('&')
    message = ""
    sender = ""
    for x in references:
	if "body=" in x.lower():
	    message = x[5:]
	if "from=" in x.lower():
	    sender = x[8:]
    geo = message.split("+")[0]
    geo = get_location(message.split(" ")[0])
    message = " ".join(message.split("+")[1:])
    open("sbsdc.log", "w").write("%s: %s | %s\n" % (datetime.datetime.now(), sender, message))
conn.close()