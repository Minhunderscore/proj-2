from datetime import datetime
from database.database import create_table, update_table, get_count
from http.server import SimpleHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8000

class handler(SimpleHTTPRequestHandler):
    def get_method(self):
        return self.command
    def get_ip_addr(self):
        return self.client_address[0]
    def get_time(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

    def get_user_info(self):
        user_info = dict({
            "method": self.get_method(),
            "ip": str(self.get_ip_addr()),
            "time": str(self.get_time())
        })
        return user_info

    def do_GET(self):
            create_table()
            update_table(data=self.get_user_info())
            num = get_count()
            html = f'This is access number: {num}'
            self.send_response(200, "OK")
            self.end_headers()
            self.wfile.write(bytes(html, 'utf-8'))

        
webServer = HTTPServer(('0.0.0.0', serverPort), handler)
print("Server started https://%s:%s" % (hostName, serverPort))
webServer.serve_forever()
