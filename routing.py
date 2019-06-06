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
        status = self.status_code_checker(path)

        start_response(status, response_headers)

        return iter([response])

    def handle_request(self, request):
        response = self.good_response()
        if request in self.routes.keys():
            return self.routes[request](request, response)
        else:
            return self.default_response(response)

    def add_new_route(self, path, handler):
        if path not in self.routes:
            self.routes[path] = handler


    def default_response(self, response):
        text = "Not found."
        return text

    def status_code_checker (self, path):
        if path not in self.routes.keys():
            status = '404'
        else:
            status = '200 OK'
        return status

    def good_response(self):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        return status, response_headers