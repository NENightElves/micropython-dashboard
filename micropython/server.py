import json
from microWebSrv import MicroWebSrv

AUTHORIZATION = None


def require_authorize(func):
    def wrapper(*args, **kwargs):
        global AUTHORIZATION
        keys = args[0].GetRequestHeaders()
        if 'authorization' not in keys or keys['authorization'] != AUTHORIZATION:
            args[1].WriteResponseJSONOk({'status': 'err_auth'})
            return
        else:
            return func(*args, **kwargs)
    return wrapper


@MicroWebSrv.route('/hello', method='GET')
def testGET(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok', 'route': 'hello'})


@MicroWebSrv.route('/hello', method='POST')
def testGET(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok', 'route': 'hello'})


@MicroWebSrv.route('/test', method='GET')
def test(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok'})


@MicroWebSrv.route('/api/systemconfig/essid', method='POST')
@require_authorize
def getwifiessid(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    r = None
    with open('wifi_config.json', 'r') as f:
        r = json.loads(f.read())['essid']
    if r:
        httpResponse.WriteResponseJSONOk({'essid': r, 'status': 'ok'})
        return
    httpResponse.WriteResponseJSONOk({'status': 'err'})


def start():
    global AUTHORIZATION
    with open('server_config.json') as f:
        AUTHORIZATION = json.loads(f.read())['Authorization']
    srv = MicroWebSrv(webPath='www')
    srv.Start(threaded=True)
