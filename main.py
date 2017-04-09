import spotify
from flask import Flask, request
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse, Message, Media
from twilio.twiml.voice_response import VoiceResponse, Dial
import requests
import urllib


account_sid = 'ACed3705bc87e8cb98628f9e11c0aebbbd'
auth_token = '46ffeadcf6a318f6e14c9b653b3bb9ef'

client = Client(account_sid,auth_token)

app = Flask(__name__)

@app.route('/sms', methods=['GET','POST'])
def indbound_sms():
    response = MessagingResponse()
    song_title = urllib.parse.quote(request.form['Body'])
    from_number = request.form['From']
    to_number = request.form['To']
    response.message('Thanks for texting! Searching for your song now. '
                     'Wait to receive a phone call :)')
    client.calls.create(to=from_number, from_=to_number,
                        url='http://e2771f83.ngrok.io/call?track={}'
                        .format(song_title))
    return str(response)



@app.route('/call', methods=['POST'])
def outbound_call():
    song_title = request.args.get('track')
    track_url = spotify.get_track_url(song_title)
    response = VoiceResponse()
    response.play(track_url)
    return str(response)


if __name__ == '__main__':
	app.run(debug=True)