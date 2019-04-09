import os
import datetime
import logging


try:
    os.chdir('/Users/lichuang.lc/Documents/git/koushao/koushao')
    os.system('sh buildAndUpload.sh')
except Exception as e:
    logging.exception(e)