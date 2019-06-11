from routing import Routing


app = Routing()


def handler(status = '401'):
    resp_text = "Hello from HOME page"
    return resp_text, status


def handler2(status = '200 OK'):
    resp_text = "Hello from ABOUT page"
    return resp_text, status

app.add_new_route("/home", handler)
app.add_new_route("/about", handler2)