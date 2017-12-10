from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import scrapy
import json
import textwrap
import lxml.html


def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

HOMEPAGE = 'http://truyentranh.net'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
MAX_MANGA = 2

root_url = set(['http://truyentranh.net', 'http://truyentranh.net/blog'])
image_format = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp']

def is_manga_url(url):
	
	return ('html' not in url) and ('chap' not in url.lower()) and (url not in root_url) and (url.count('/') == 3)

def is_chapter_url(url):

	return ('html' not in url) and ('chap' in url.lower()) and (url not in root_url) and (url.count('/') == 4)
	
def is_sub_url(chapter_url, manga_url):

	return manga_url.lower() in chapter_url.lower()

def is_content_url(content_url):

	for x in image_format:
		if x in content_url:
			return True

	return False

def clean(str):
	return " ".join(str.split())


def intersect(s1, s2):
    for length in range(len(s2) - 1, -1, -1):
        for i in range(0, len(s2) - length + 1):
            if s2[i:i + length] in s1:
                return s2[i:i + length]