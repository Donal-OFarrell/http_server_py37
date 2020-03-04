import http.server 
import socketserver 

PORT = 8080
handler = http.server.SimpleHTTPRequestHandler # serves files from current directory and # any sub directories

with socketserver.TCPServer(("",PORT),handler) as httpd: # this is just file opening notation
    print("serving at port", PORT)
    httpd.serve_forever()

# it's tcpwhere you pass the ip and the port 
# you also have the handler 

# tutorial : https://www.afternerd.com/blog/python-http-server/

# now build one from scratch 
# made in c : https://medium.com/from-the-scratch/http-server-what-do-you-need-to-know-to-build-a-simple-http-server-from-scratch-d1ef8945e4fa