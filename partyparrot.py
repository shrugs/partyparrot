import json
import random
import requests
import sys
from secrets import SHITPOSTING_ENDPOINT

ALPHABET = {
    'a': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'b': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
    ],
    'c': [
        [0,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [0,1,1,1,1],
    ],
    'd': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,0],
    ],
    'e': [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    'f': [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
    ],
    'g': [
        [0,1,1,1,1],
        [1,0,0,0,0],
        [1,0,1,1,1],
        [1,0,0,0,1],
        [0,1,1,1,1],
    ],
    'h': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'i': [
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
    ],
    'j': [
        [0,0,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'k': [
        [1,0,0,1,0],
        [1,0,1,0,0],
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'l': [
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    'm': [
        [1,0,0,0,1],
        [1,1,0,1,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'n': [
        [1,1,0,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,1,1],
    ],
    'o': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'p': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
    ],
    'q': [
        [0,1,1,0,0],
        [1,0,0,1,0],
        [1,0,0,1,0],
        [1,0,0,1,0],
        [0,1,1,1,1],
    ],
    'r': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,1,0],
        [1,0,0,0,1],
    ],
    's': [
        [0,1,1,1,1],
        [1,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,1],
        [1,1,1,1,0],
    ],
    't': [
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    'u': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'v': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,0,1,0,0],
    ],
    'w': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,1,0,1,1],
        [1,0,0,0,1],
    ],
    'x': [
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,1,0,1,0],
        [1,0,0,0,1],
    ],
    'y': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    'z': [
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,1,1,1,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ]
}

PARTY_PARROTS = [
    ':partyparrot:',
    ':partyparrot2:',
    ':partyparrot3:',
    ':partyparrot4:'
]


def arr_to_str(c, s, space='        '):
    if c == ' ':
        return '\n\n\n\n\n\n\n\n'
    arr = ALPHABET[c]
    output_string = ''
    for row in arr:
        for col in row:
            output_string += s if col else space
        output_string += '\n'

    return output_string


def post_text_to_slack(output_string):
    payload = {
        'username': 'Someone fun',
        'icon_emoji': ':partyparrot:',
        'text': output_string
    }

    return requests.post(SHITPOSTING_ENDPOINT, data=json.dumps(payload))


def convert_str_to_emoji(s, emojis=PARTY_PARROTS, force=False):
    s = s.lower()
    output_string = ''
    for c in s:
        output_string += arr_to_str(c, random.choice(emojis))
        output_string += '\n\n'
    if force:
        post_text_to_slack(output_string)
    return output_string

if __name__ == '__main__':
    # Handles -f force-to-Slack flag
    force = False
    if sys.argv[1] == '-f':
        force = True
        sys.argv.remove(sys.argv[1])

    input_str = sys.argv[1]
    if len(sys.argv) > 2:
        emojis = sys.argv[2:]
        print convert_str_to_emoji(input_str, emojis=emojis, force=force)
    else:
        print convert_str_to_emoji(input_str, force=force)
