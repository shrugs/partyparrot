import partyparrot
import os
from flask import Flask, request, jsonify
app = Flask(__name__)

slack_team_token = os.environ.get('SLACK_TEAM_TOKEN')


@app.route('/', methods=['GET'])
def index():
    return 'OK'


@app.route('/', methods=['POST'])
def slack():
    if slack_team_token and request.form.get('token') != slack_team_token:
        return 'Unauthorized', 401

    text = request.form.get('text')
    if not text:
        return 'I need some text.', 200

    out = partyparrot.convert_str_to_emoji(text, space='        ')
    return jsonify(
        response_type='in_channel',
        text=out
    )

if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 5000))
