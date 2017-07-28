# -*- coding: utf-8 -*-
import json
import requests
import argparse
import itertools
import os
from all_characters import ALL_CHARACTERS

PARTY_PARROTS = [
    ':partyparrot:',
    ':rightparrot:',
    ':middleparrot:',
    ':boredparrot:',
    ':shuffleparrot:'
]

EN_SPACE = '\u2002'


def arr_to_str(c, s, space):
    if c == ' ':
        return '\n\n\n\n\n\n\n\n'
    if c in ALL_CHARACTERS:
        arr = ALL_CHARACTERS[c]
    else:
        raise ValueError(u"'{}' is not a supported character".format(c))
    output_string = ''
    for row in arr:
        for col in row:
            output_string += s if col else space
        output_string += '\n'

    return output_string


def post_text_to_slack(output_string):
    if 'SHITPOSTING_ENDPOINT' not in os.environ:
        print('SHITPOSTING_ENDPOINT is not in your environment. Fix that.')
        return

    payload = {
        'username': 'The Party Parrot',
        'icon_emoji': ':partyparrot:',
        'text': make_slack_compatible(output_string)
    }

    return requests.post(os.environ['SHITPOSTING_ENDPOINT'], data=json.dumps(payload))


def make_slack_compatible(partyparrot_string):
    # because slack trims the beginning of messages now,
    # and unicode spaces don't help,
    # replace the first character with a period.
    # ideally we find a better way to do this, but for now this works.
    # The shitposting must go on.
    out = partyparrot_string

    # if the first character is a space, it would normally get truncated so let's prefix
    if out[0] == EN_SPACE:
        out = '.\n' + EN_SPACE + out[1:]
    else:
        out = '.\n' + out

    return out


def convert_str_to_emoji(s, emojis=PARTY_PARROTS, space=' ', force=False):

    emoji_iterator = itertools.cycle(emojis)

    s = s.lower()
    output_string = ''
    for c in s:
        output_string += arr_to_str(c, next(emoji_iterator), space)
        output_string += '\n\n'
    if force:
        post_text_to_slack(output_string)
    return output_string


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='The text to emoji-fy')
    parser.add_argument('-e', '--emojis', nargs='+',
                        help='List of emojis to use.', default=PARTY_PARROTS)
    parser.add_argument('-f', '--force', action='store_true',
                        help='automatically post to the slack of your choosing', default=False)
    parser.add_argument('-s', '--space', default='        ')

    args = parser.parse_args()

    try:
        out_str = convert_str_to_emoji(args.text,
                                       emojis=args.emojis,
                                       space=args.space,
                                       force=args.force
                                       )
        print(out_str)
    except ValueError as e:
        print(str(e))
