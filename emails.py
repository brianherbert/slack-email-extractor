from slacker import Slacker

# https://api.slack.com/docs/oauth-test-tokens
slack = Slacker('TOKEN-HERE')

# Get users list
response = slack.users.list()
users = response.body['members']

for user in users:
    if "email" in user["profile"]:
        print '"'+user["profile"]["real_name"].encode('utf-8').strip()+'",'+user["profile"]["email"].encode('utf-8').strip()
