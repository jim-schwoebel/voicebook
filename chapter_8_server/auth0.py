'''
Auth0.py

Taken from the docs:
https://github.com/auth0/auth0-python
'''
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0

# obtain a management token 
domain = 'myaccount.auth0.com'
non_interactive_client_id = 'exampleid'
non_interactive_client_secret = 'examplesecret'

get_token = GetToken(domain)
token = get_token.client_credentials(non_interactive_client_id,
    non_interactive_client_secret, 'https://{}/api/v2/'.format(domain))
mgmt_api_token = token['access_token']

# use your management token 
auth0 = Auth0(domain, mgmt_api_token)

#The Auth0() object is now ready to take orders! Let's see how we can use this to get all available connections. (this action requires the token to have the following scope: read:connections)
print(auth0.connections.all())