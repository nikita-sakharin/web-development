from datetime import datetime


def app(environ, start_response):
    data = bytes(F'Local datetime: {str(datetime.now())}', 'UTF-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
