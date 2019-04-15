import partyparrot
import os
from flask import Flask, request, jsonify
app = Flask(__name__)

slack_team_token = os.environ.get('SLACK_TEAM_TOKEN')

EN_SPACE = '\u2002'


@app.route('/', methods=['POST'])
def slack():
    if slack_team_token and request.form.get('token') != slack_team_token:
        return 'Unauthorized', 401

    text = request.form.get('text')
    if not text:
        return 'I need some text.', 200

    try:
        out = partyparrot.convert_str_to_emoji(text, space=(EN_SPACE * 3))

        return jsonify(
            response_type='in_channel',
            text=partyparrot.make_slack_compatible(out)
        )
    except ValueError as e:
        return jsonify(text=str(e))

