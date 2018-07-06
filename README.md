# Twitter Entropy Collector

Twitter is a great noise source: Russian bots, Trump rants, human interactions, malware traffic and so on. (Almost) random and unpredictable content.
This tool provides an extra entropy source (to be used on Linux) from the [Twitter random sample feed](https://developer.twitter.com/en/docs/tweets/sample-realtime/overview/GET_statuse_sample).

![Twitter noise](https://i.imgur.com/vLdn9Az.jpg)

*Twitter noise visualization*

### Installation

First, update your API keys in the *secrets.py* file. To get API keys go to https://apps.twitter.com/

The script should work fine using Python2 or Python3.

You will need the following python packages installed: tweepy & hexdump.

```sh
pip install -r requirements.txt
```


### Usage

```
# ./tweetentro.py
```

### Caveats

⚠️ **Do not use this for sensitive cryptographic operations!**
We can safely assume there will be repeating occurrences in the data (trending hashtags, links, ...), it isn't true random. Entropy is around 6.5 bits per byte. 
Only use this as an extra source of entropy if you wish.

License
----
GNU GPLv3

If this tool has been useful for you, feel free to thank me by buying me a coffee

[![Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoff.ee/x0rz)
