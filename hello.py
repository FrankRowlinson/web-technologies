def application(environ, start_response):
    status = '200 OK'
    query_string = environ['QUERY_STRING']
    response = '\n'.join(query_string.split('&')).encode('utf-8')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [response]
