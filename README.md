# Slack Email Extractor
Download a list of all users and their email addresses in a Slack group.

# Requirements
Python 2.7+

# Installation
```
pip install slacker
```

Enter your API key in the appropriate place in the script.

# Usage
From the command line, browse to the script directory and run:

```
python emails.py
```

The output is simply printed to stdout in CSV format. Future versions of the script could allow an option to output directly to a file.

# Notes
This will only return users who have their email address available in their profile.