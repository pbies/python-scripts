#!/usr/bin/python3
# YouTube downloader
# pip install httplib2
import argparse

import httplib2
import json
import urllib
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.request import Request
import shutil

def dl_youtube(url, outfile):
	h = httplib2.Http()
	resp, content = h.request(url, "GET", headers={'content-type': 'text/html'})
	
	print("Reading movie data...")
	# parsing config string
	config = json.loads(str(content, "iso-8859-1").split("yt.playerConfig = ")[1].split("</script>")[0].strip()[:-1])
	
	# gathering data
	yt_args = urllib.parse.parse_qs(config['args']['url_encoded_fmt_stream_map'])
	
	realurl = yt_args['url'][0].split(',')[0] + '&signature='+yt_args['sig'][0].split(',')[0]
	
	print("Downloading...")
	
	# downloading file at index 0 (0 is the best available quality)
	with open(outfile, 'wb') as dst:
		shutil.copyfileobj(urlopen(Request(realurl, headers={ 'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11' })), dst)

parser = argparse.ArgumentParser(description="Downloads a movie")
parser.add_argument("url")
parser.add_argument("outfile")

args = parser.parse_args()

dl_youtube(args.url, args.outfile)