from flask import Flask, redirect, request, render_template
from uber_rides.auth import AuthorizationCodeGrant

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URL = "http://127.0.0.1:8000"


auth_flow = AuthorizationCodeGrant(
    CLIENT_ID,
    {'profile'},
    CLIENT_SECRET,
    REDIRECT_URL,
)
auth_url = auth_flow.get_authorization_url()

print(auth_url)

session = auth_flow.get_session(request.url)
client = UberRidesClient(session)
credentials = session.oauth2credential

response = client.get_price_estimates(
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405,
    seat_count=2
)

estimate = response.json.get('prices')
