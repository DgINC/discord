from oauthlib.oauth2 import BackendApplicationClient
client = BackendApplicationClient('your_id')
client.prepare_request_body(scope=['hello', 'world'])