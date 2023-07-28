from bottle import route, run, request, HTTPResponse
from exception_decor import exception


@route('/')
@exception
def index():
    if request.headers.get('X-Header'):
        return 'hello world'
    raise HTTPResponse('Internal server error - X-Header is required', status=500, headers={})


run(host='localhost', port=8888)
