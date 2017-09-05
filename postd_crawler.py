#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.insert(0, 'libs')
from bs4 import BeautifulSoup
import urllib2

def extract_postd_origin(html):
    soup = BeautifulSoup(html, 'html.parser')
    origin = soup.find('div', { 'class' : 'block-text-original-text' })
    urls = origin.findAll('a', { 'class' : 'ext-link' })
    return urls[0]['href'].rstrip('/')

def get_postd_origin(postd_url):
    response = urllib2.urlopen(postd_url)
    return extract_postd_origin(response.read())


