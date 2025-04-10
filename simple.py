from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!docttype html>
<html>
    <head>
        <title>TCP/IP</title>
    </head>
    <body bgcolor="pink">
        <H1>TCP/IP PROTOCOLS</H1><br>cd
            <br><center>
            1.Application Layer HTTP,FTP,SSH,Telnet & DNS <br>
            2.Transport Layer TCP,UDP<br>
            3.Internet Layer IP,ROUTING PROTOCOLS(RIP,OSDP)<br>
            4.Link Layer Ethernet(MAC)<br>R.JANANI<br>Reg Number:212224040126<br>
        </center>
           
    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()