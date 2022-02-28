import sipfullproxy as sfp
import socket
import socketserver
import re

hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)

print("Automaticky zistená IP adresa: %s\nAk si želáte použiť inú, napíšte ju. Inak stlačte ENTER." % ipaddress)
alternateip = input()
if re.search("^([0-9]{1,3}\.){3}[0-9]{1,3}$", alternateip) is not None:
    ipaddress = alternateip

print("Automatický port: 5060\nAk si želáte použiť iný, napíšte ho. Inak stlačte ENTER.")
port = input()
if re.search("^[0-9]{1,5}$", port) is None:
    port = 5060
port = int(port)

print("Spúšťam server na: %s:%d" % (ipaddress, port))
sfp.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, port)
sfp.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, port)
server = socketserver.UDPServer((sfp.HOST, port), sfp.UDPHandler)
server.serve_forever()
