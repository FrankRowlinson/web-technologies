def application(environ, start_response):
    status = '200 OK'
    query_dict = environ['QUERY_STRING']
    response = '\n'.join([f'{k}={v}' for k, v in query_dict.items()])
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [response]