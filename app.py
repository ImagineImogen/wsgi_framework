from routing import Routing


app = Routing()


def handler():
    return {
        "text": "Hello from HOME page",
        "extra_headers": {'Content-Type': 'text/plain'}
    }


def handler2():
    return {
        "text": "Hello from ABOUT page",
    }

app.add_new_route("/home", handler)
app.add_new_route("/about", handler2)