import server



class Routing:
    try:
        a = server.WSGIServer(('', 0000))
    except OSError:
        a = server.WSGIServer(('', 9000))
    env = a.get_environ

    def __init__(self):
        self.routes = {}


    def __call__(self, env, start_response):
        response_headers = [('Content-Type', 'text/plain')]
        path = env.get('PATH_INFO')

        response = self.handle_request(path)
        status = list(response)[1]
        #status = self.status_code_checker(path)

        start_response(status, response_headers)

        return iter([response])

    def handle_request(self, request):

        if request in self.routes.keys():
            return self.routes[request]()
        else:
            return self.default_response()

    def add_new_route(self, path, handler):
        if path not in self.routes:
            self.routes[path] = handler


    def default_response(self):
        text = "Not found."
        status = '404'
        return text, status

    def status_code_checker (self, path):
        if path not in self.routes.keys():
            status = '404'
        else:
            status = '200 OK'
        return status

