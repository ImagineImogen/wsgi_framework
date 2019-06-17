import server
from http.client import responses


class Routing:
    try:
        a = server.WSGIServer(('', 0000))
    except OSError:
        a = server.WSGIServer(('', 9000))
    env = a.get_environ

    def __init__(self):
        self.routes = {}


    def __call__(self, env, start_response):
        response_headers = {'Content-Type': 'text/html'}
        path = env.get('PATH_INFO')
        status_code = 200

        response = self.handle_request(path)


        status_code = response.get('status_code', 200)
        extra_header = response.get('extra_headers', {})

        response_headers.update(extra_header)

        start_response(
            '{} {}'.format(
                status_code,
                responses[status_code]
            ),
            list(response_headers.items())
        )

        return iter([response])

    def handle_request(self, request):


        if request in self.routes.keys():
            return self.routes[request]()
        else:
            return self.not_found_handler()

    def add_new_route(self, path, handler):
        if path not in self.routes:
            self.routes[path] = handler


    #def default_response(self):
        #text = "Not found."
        #status = '404'
        #return text, status

    @staticmethod
    def not_found_handler():
        return {
            "text": "Not found",
            "status_code": 404
        }
    def status_code_checker (self, path):
        if path not in self.routes.keys():
            status = '404'
        else:
            status = '200 OK'
        return status

