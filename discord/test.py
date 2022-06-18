from oauthlib.oauth2 import WebApplicationClient

client = WebApplicationClient('0123456789876543210')
fff = client.prepare_request_uri('https://discord.com/api/v10/api/oauth2/token',
                                 redirect_uri='https://a.b/callback',
                                 scope=['bot', 'identify'],
                                 code_challenge='kjasBS523KdkAILD2k78NdcJSk2k3KHG6',
                                 code_challenge_method='S256',
                                 state='ffff'
                                 )
print(fff)
