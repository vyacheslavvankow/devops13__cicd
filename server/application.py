'''Devops2025'''
import http.server
import socketserver

PORT = 8000

class TestMe():
    '''For me'''
    def take_five(self):
        return 5

    def port(self):
        '''port'''
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
