# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)






FLAG = os.getenv('FLAG', 'landing')
SITEURL = os.getenv('SITEURL', 'https://2023.es.pycon.org/')

#from pelicanconf import *
from pelicanconf_landing import *



# If your site is available via HTTPS, make sure SITEURL begins with https://
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
