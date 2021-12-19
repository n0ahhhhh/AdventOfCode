#!/usr/bin/env python
# coding: utf-8

import os
import sys
import re
from datetime import datetime, timedelta
from importlib.util  import find_spec
from bs4 import BeautifulSoup

def log(s, *a):
    sys.stderr.write('[advent] ' + s.format(*a))
    sys.stderr.flush()
    
def logcont(s, *a):
    sys.stderr.write(s.format(*a))
    sys.stderr.flush()

def check_or_die(resp):
    if resp.status_code != 200:
        logcont('\n')
        log('ERROR: response {}, url: {}\n', resp.status_code, resp.url)
        log('Did you log in and update your session cookie?\n')
        sys.exit(1)

    if 'please identify yourself' in resp.text.lower():
        logcont('\n')
        log('ERROR: Server returned 200, but is asking for identification.\n')
        log('Did you log in and update your session cookie?\n')
        sys.exit(1)

def check_setup_once():
    if YEAR == -1 and DAY == -1:
        now = datetime.utcnow() + timedelta(hours=-8)
        y, m, d = now.year, now.month, now.day

        if m != 12 or (m == 12 and d > 25):
            log('ERROR: year and day not set, and no event currently running!\n')
            sys.exit(1)

        log('Year and day not set, assuming today: Dec {}, {}.\n', d, y)
        setup(y, d)

def setup(year, day):
    global YEAR
    global DAY
    global SESSION
        
    if not (year >= 2015 and 1 <= day <= 25):
        log('ERROR: invalid year and/or day set!\n')
        sys.exit(1)

    YEAR = year
    DAY  = day

    if REQUESTS and os.path.isfile('..\secret_session_cookie'):
        with open('..\secret_session_cookie') as f:
            SESSION = f.read().rstrip()
            S.cookies.set('session', SESSION)

def get_input(fname=None, mode='r'):
    global CACHE_DIR
    
    check_setup_once()
    
    #gets the title of the puzzle
    pr = S.get(URL.format(YEAR,DAY,''))
    check_or_die(pr)
    soup = BeautifulSoup(pr.text, 'html.parser')
    title = re.findall('(?<=:\s).*(?=\s-)', soup.h2.text)[0]
    title = ' - ' + title

    CACHE_DIR = CACHE_DIR.format(YEAR,DAY,title)

    if fname is not None:
        return open(fname, mode)
    
    if not os.path.isdir(CACHE_DIR):
        try:            
            os.makedirs(CACHE_DIR)
            log("Created cache directory '{}' since it did not exist.\n", CACHE_DIR)
        except Exception as e:
            log("ERROR: could not create cache directory '{}'.\n", CACHE_DIR)
            log('{}\n', str(e))
            sys.exit(1)

    log('Getting input for year {} day {}... ', YEAR, DAY)
    fname = os.path.join(CACHE_DIR, 'day_{:02d}.txt'.format(DAY))

    try:
        file = open(fname, mode)
        logcont('done (from disk).\n')
        return file
    except FileNotFoundError:
        pass

    if not REQUESTS:
        logcont('err!\n')
        log('ERROR: cannot download input, no requests module installed!\n')
        sys.exit(1)
    elif not SESSION:
        logcont('err!\n')
        log('ERROR: cannot download input file without session cookie!\n')
        sys.exit(1)

    logcont('downloading... ')

#     testurl = URL.format(YEAR, DAY, '/input')
#     print('input:',testurl)
    r = S.get(URL.format(YEAR, DAY, '/input'))
    check_or_die(r)

    with open(fname, 'wb') as f:
        f.write(r.content)

    file = open(fname, mode)
    logcont('done.\n')

    return file

# constants
URL       = 'https://adventofcode.com/{:d}/day/{:d}{:s}'
SESSION   = ''
YEAR      = -1
DAY       = -1
CACHE_DIR = r'..\{:d}\Day {:02d}{:s}'
REQUESTS  = find_spec('requests')

if REQUESTS:
    import requests
    S = requests.Session()