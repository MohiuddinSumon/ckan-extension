
def myext_hello():
    return "Hello, myext!"


def get_helpers():
    return {
        "myext_hello": myext_hello,
    }
