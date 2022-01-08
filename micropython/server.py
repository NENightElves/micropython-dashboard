import json
from microWebSrv import MicroWebSrv
import machine
import utime
import os

AUTHORIZATION = None


def require_authorization(func):
    def wrapper(*args, **kwargs):
        global AUTHORIZATION
        keys = args[0].GetRequestHeaders()
        if 'authorization' not in keys or keys['authorization'] != AUTHORIZATION:
            args[1].WriteResponseJSONOk({'status': 'err_auth'})
            utime.sleep(0.2)
            return
        else:
            return func(*args, **kwargs)
    return wrapper


def _deletefile(path):
    try:
        os.remove(path)
    except OSError:
        for _ in os.listdir(path):
            _deletefile(_)
        os.remove(path)


@MicroWebSrv.route('/hello', method='GET')
def testHelloGET(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok', 'route': 'hello'})


@MicroWebSrv.route('/hello', method='POST')
def testHelloPOST(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok', 'route': 'hello'})


@MicroWebSrv.route('/test', method='GET')
def testGET(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok'})


@MicroWebSrv.route('/test', method='POST')
def testPOST(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok'})


@MicroWebSrv.route('/api/reboot', method='POST')
@require_authorization
def reboot(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok'})
    utime.sleep(1)
    machine.reset()


@MicroWebSrv.route('/api/systemconfig/syspwd', method='POST')
@require_authorization
def setsyspwd(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    global AUTHORIZATION
    j = httpClient.ReadRequestContentAsJSON()
    with open('server_config.json', 'r') as f:
        o = json.loads(f.read())
    if j['Authorization']:
        o['Authorization'] = j['Authorization']
        AUTHORIZATION = o['Authorization']
        with open('server_config.json', 'w') as f:
            f.write(json.dumps(o))
        httpResponse.WriteResponseJSONOk({'status': 'ok'})
    else:
        httpResponse.WriteResponseJSONOk({'status': 'err'})


@MicroWebSrv.route('/api/systemconfig/essid', method='POST')
@require_authorization
def getwifiessid(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    r = None
    with open('wifi_config.json', 'r') as f:
        r = json.loads(f.read())['essid']
    if r:
        httpResponse.WriteResponseJSONOk({'essid': r, 'status': 'ok'})
        return
    httpResponse.WriteResponseJSONOk({'status': 'err'})


@MicroWebSrv.route('/api/systemconfig/changewifi', method='POST')
@require_authorization
def changewifi(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    j = httpClient.ReadRequestContentAsJSON()
    if 'essid' not in j or 'password' not in j:
        httpResponse.WriteResponseJSONOk({'status': 'err', 'msg': 'essid or password missing'})
        return
    jwificonfig = None
    with open('wifi_config.json', 'r') as f:
        jwificonfig = json.loads(f.read())
        jwificonfig['essid'] = j['essid']
        jwificonfig['password'] = j['password']
        if 'static' in j and j['static']:
            if 'ip' in j['static'] and j['static']['ip'] and 'subnet' in j['static'] and j['static']['subnet'] and 'gateway' in j['static'] and j['static']['gateway'] and 'dns' in j['static'] and j['static']['dns']:
                jwificonfig['static']['ip'] = j['static']['ip']
                jwificonfig['static']['subnet'] = j['static']['subnet']
                jwificonfig['static']['gateway'] = j['static']['gateway']
                jwificonfig['static']['dns'] = j['static']['dns']
            else:
                httpResponse.WriteResponseJSONOk({'status': 'err', 'msg': 'static missing'})
                return
    with open('wifi_config.json', 'w') as f:
        f.write(json.dumps(jwificonfig))
    httpResponse.WriteResponseJSONOk({'status': 'ok'})
    utime.sleep(1)
    machine.reset()


@MicroWebSrv.route('/api/files/list', method='POST')
@require_authorization
def getfilelist(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    j = httpClient.ReadRequestContentAsJSON()
    r = []
    for _ in os.ilistdir(j['dir']):
        if _[1] == 32768:
            r.append({'name': _[0], 'type': 'f'})
        elif _[1] == 16384:
            r.append({'name': _[0], 'type': 'd'})
    httpResponse.WriteResponseJSONOk({'files': r, 'status': 'ok'})


@MicroWebSrv.route('/api/files/create', method='POST')
@require_authorization
def createfile(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    j = httpClient.ReadRequestContentAsJSON()
    r = []
    for _ in j['files']:
        if _['type'] == 'd':
            os.mkdir(_['name'])
        elif _['type'] == 'f':
            f = open(_['name'], 'w')
            f.close()
    httpResponse.WriteResponseJSONOk({'status': 'ok'})


@MicroWebSrv.route('/api/files/delete', method='POST')
@require_authorization
def deletefile(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    j = httpClient.ReadRequestContentAsJSON()
    r = []
    for _ in j['files']:
        _deletefile(_)
    httpResponse.WriteResponseJSONOk({'status': 'ok'})


@MicroWebSrv.route('/api/files/get', method='POST')
@require_authorization
def getfile(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    j = httpClient.ReadRequestContentAsJSON()
    content = None
    with open(j['file'], 'r') as f:
        content = f.read()
    httpResponse.WriteResponseJSONOk({'content': content, 'status': 'ok'})


@MicroWebSrv.route('/api/files/modify', method='POST')
@require_authorization
def modifyfile(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    j = httpClient.ReadRequestContentAsJSON()
    content = None
    with open(j['file'], 'w') as f:
        f.write(j['content'])
    httpResponse.WriteResponseJSONOk({'status': 'ok'})


def start():
    global AUTHORIZATION
    with open('server_config.json') as f:
        AUTHORIZATION = json.loads(f.read())['Authorization']
    srv = MicroWebSrv(webPath='/www')
    srv.Start(threaded=True)
