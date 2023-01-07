import http.client

conn = http.client.HTTPSConnection("anerox.au.auth0.com")

payload = "{\"client_id\":\"vDXSwmzWV6UQMgBSdl3fCjuIZi6rjlA5\",\"client_secret\":\"AGC2xMPg77V2LQRHa8mH9h4aHSSYp1xf3FyJRIeSyPJIZKdYKwPtrgkv49d90iem\",\"audience\":\"https://anerox.au.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
