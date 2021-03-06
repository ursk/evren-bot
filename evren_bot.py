#!/usr/bin/env python

import time
import random
import requests
import os


def build_message(phrase_sets):
    message = ''
    for phrase_set in phrase_sets:
        message += random.choice(phrase_set)
    return message

PHRASE_SETS = [
    ['', "dont forget to "],
    ['order'],
    ['', ' your'],
    [' lunch', ' lunches'],
    ['', ' people', ' everyone'],
]


def wait_random_time_between(minutes_min, minutes_max):
    seconds_min = minutes_min * 60
    seconds_max = minutes_max * 60
    seconds = random.randrange(seconds_min, seconds_max)
    print 'waiting', seconds, 'seconds'
    time.sleep(seconds)


def main():
    wait_random_time_between(1, 9)

    message = build_message(PHRASE_SETS)

    print message

    os.system("""curl -X POST --data-urlencode 'payload={{"channel": "#sd", "username": "evren-bot", "text": "{message}", "icon_emoji": ":whale2:"}}' https://hooks.slack.com/services/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""".format(message=message))

if __name__ == '__main__':
    main()
