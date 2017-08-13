from flask import Flask, request
from pymessenger.bot import Bot
import nltk

app = Flask(__name__)

ACCESS_TOKEN = "EAAL6mll3TawBAH4yBoUhvwcNEwqBmrRF50ZBQPM7o2zSpQdA1m0Ww3o5Pcxo0j6ZC0GpXynbNGFGNhnk9iNZAcJBir2ZBw3CZCYaPNSU96YJ4nLsRKmVdZAoaKc7wbAyJODPlc7ZCWzhrT83aZAPUUV1KwonCpxfjTJcoP7hwjadMwZDZD"
VERIFY_TOKEN = "Danhth"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':

        if request.args.get("hub.verify_token") == VERIFY_TOKEN:

            return request.args.get("hub.challenge")
        else:

            return 'Invalid verification token'

    if request.method == 'POST':

        output = request.get_json()

        for event in output['entry']:

            messaging = event['messaging']

            for x in messaging:

                if x.get('message'):

                    recipient_id = x['sender']['id']

                    if x['message'].get('text'):
                        message = x['message']['text']

                        ## Handle 'message' to send user a response
                        bot.send_text_message(recipient_id, message)

                else:
                    pass

        return "Success", 200


if __name__ == "__main__":
    app.run()
