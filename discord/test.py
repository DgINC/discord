from random import randrange

from oauthlib.oauth2 import WebApplicationClient

from core import OAUTH_AUTHORIZE

client = WebApplicationClient('987196221288501258')
fdfsd = client.create_code_verifier(randrange(43, 128))
fdf = client.create_code_challenge(fdfsd, code_challenge_method="S256")
fff = client.prepare_request_uri(OAUTH_AUTHORIZE,
                                 redirect_uri='http://127.0.0.1:8080/redirect',
                                 scope=['bot', 'identify'],
                                 code_challenge=fdf,
                                 code_challenge_method='S256',
                                 permissions=8,
                                 state='sdt45rdf63dsaget'
                                 )
print(fdfsd)
print(fdf)
print(fff)
