# :partyparrot:

![partyparrot](example.gif)

# Usage

## With the Party Parrot (:partyparrot:)

Just pass the script a string of your choosing.

```bash
python partyparrot.py "HELLO" | pbcopy
```

## Custom Emoji List

Use the `-e` or `--emojis` flag to use a custom list of emojis.

```bash
python partyparrot.py "something stupid" -e ":emoji1:" ":emoji2:" ":emoji3:" ":emoji4:" | pbcopy
```

## Auto-Post to Slack

Use the `-f` or `--force` flag to auto-post to your favorite Slack channel (configure URL in the "Incoming Webhooks" section of the "Integrations" page).

```bash
SHITPOSTING_ENDPOINT="<YOUR_SLACK_INCOMING_WEBHOOK_URL>" python partyparrot.py "something stupid" -f
```

## Tests

`python test_partyparrot.py`

