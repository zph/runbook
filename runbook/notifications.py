import logging

logging.basicConfig(level=logging.DEBUG)

import os
from functools import partial

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# Usage
# r = thread_post_message = start_thread('CCCCC', 'Topic For Discussion')
# r2 = r.thread_post_message('A threaded message about gritty')
# r2.react_to_message(emoji='gritty')
def start_thread(channel, message):
    return post_message(channel, "🧵 " + message + " 🧵")


def thread_fn(channel, thread):
    return partial(post_message, channel=channel, thread=thread)


def react_to_message(channel, emoji, timestamp):
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    client = WebClient(token=slack_token)

    arg = dict(
        channel=channel,
        timestamp=timestamp,
        name=emoji,
    )

    try:
        r = client.reactions_add(**arg)
        # On first post treat response as thread id
        ts = r["ts"]
        if not thread:
            thread = ts

        return dict(
            ts=ts,
            thread=thread,
            thread_post_message=partial(post_message, channel=channel, thread=thread),
            react_to_message=partial(react_to_message, channel=channel, timestamp=ts),
        )

    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]


def post_message(channel, message, thread=None):
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    client = WebClient(token=slack_token)

    arg = dict(
        channel=channel,
        thread_ts=thread,
        blocks=[{"type": "section", "fields": [{"type": "mrkdwn", "text": message}]}],
    )
    if not thread:
        del arg["thread_ts"]

    try:
        # TODO: return fns to keep interacting instead of data?
        return client.chat_postMessage(**arg)

    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]
