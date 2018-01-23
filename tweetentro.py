#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import hexdump
import os
import sys
import fcntl
import struct

from secrets import consumer_key, consumer_secret, access_token, access_token_secret

BUF_MIN_SIZE = 512 # tweet buffer to limit frequent ioctl() calls
BUF = ""

def add_entropy(rnd):
    """ Add data to the entropy pool """
    """ From https://github.com/netom/onetimepad/blob/master/rndaddentropy.py """
    fd = os.open("/dev/random", os.O_WRONLY)
    # struct rand_pool_info {
    # int entropy_count;
    # int buf_size;
    # __u32 buf[0];
    # };
    fmt = 'ii%is' % len(rnd)
    # Here we set 6*len(rnd) entropy bits (instead of 8 because tweet data does not have perfect randomness)
    rand_pool_info = struct.pack(fmt, 6 * len(rnd), len(rnd), rnd)
    fcntl.ioctl(fd, 1074287107, rand_pool_info)
    os.close(fd)

class SampleStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global BUF

        BUF += status.text.encode('utf-8')
        if len(BUF) > BUF_MIN_SIZE:
            hexdump.hexdump(BUF)
            add_entropy(BUF)
            BUF = ""

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    sl = SampleStreamListener()
    stream = tweepy.Stream(auth = api.auth, listener=sl)

    # Using statuses/sample API to get random tweets
    # Cf. https://developer.twitter.com/en/docs/tweets/sample-realtime/overview/GET_statuse_sample
    stream.sample()
