import partyparrot
import os
from flask import Flask, request, jsonify
app = Flask(__name__)

slack_team_token = os.environ.get('SLACK_TEAM_TOKEN')

EN_SPACE = '\u2002'


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

    try:
        out = partyparrot.convert_str_to_emoji(text, space=(EN_SPACE * 3))
        # because slack trims the beginning of messages now,
        # and unicode spaces don't help,
        # replace the first character with a period.
        # ideally we find a better way to do this, but for now this works.
        # The shitposting must go on.

        if out[0] == EN_SPACE:
            out = '.' + out[2:]

        return jsonify(
            response_type='in_channel',
            text=out
        )
    except ValueError as e:
        return jsonify(text=str(e))

if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 5000))
