from routing import Routing


app = Routing()


def handler(req, resp):
    resp_text = "Hello from HOME page"
    #return iter([resp_text])
    return resp_text


def handler2(req, resp):
    resp_text = "Hello from ABOUT page"
    return resp_text

app.add_new_route("/home", handler)
app.add_new_route("/about", handler2)