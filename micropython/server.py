from microWebSrv import MicroWebSrv


@MicroWebSrv.route('/hello', method='GET')
def testGET(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok', 'route': 'hello'})


@MicroWebSrv.route('/hello', method='POST')
def testGET(httpClient: MicroWebSrv._client, httpResponse: MicroWebSrv._response):
    httpResponse.WriteResponseJSONOk({'status': 'ok', 'route': 'hello'})


def start():
    srv = MicroWebSrv(webPath='www')
    srv.Start(threaded=True)
