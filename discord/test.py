from oauthlib.oauth2 import WebApplicationClient
client = WebApplicationClient('0123456789876543210')
fff = client.prepare_request_uri('https://example.com', redirect_uri='https://a.b/callback', scope=['profile', 'pictures'])
print(fff)
