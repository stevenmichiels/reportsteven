import os
import pandas as pd
import re
import seaborn as sns
import matplotlib.pylab as plt
import numpy as np
import datetime

from dateutil.relativedelta import relativedelta, FR
from datetime import datetime, date, timedelta
from random import randint
from time import sleep
from pytz import timezone, utc
import urllib.request, json

ticker_list=['ARKK','AAPL','_SPX', '_VIX', 'QQQ','XLK','IWM', 'SMH', 'MSFT','AMD', 'NVDA','AVGO', 'TSLA', 'GOOG', 'GOOGL','META','GLD','XLE','XOM','OXY','MPC','USO','UUP']




dir_datetime=datetime.now(timezone('UTC')).astimezone(timezone('US/Eastern'))
##folder_appendix = '_Before' if datetime.now(timezone('UTC')).astimezone(timezone('US/Eastern')).hour in range(9) else ('_Open' if datetime.now(timezone('UTC')).astimezone(timezone('US/Eastern')).hour in range(9,11) else '_Post')
dir_name=str(dir_datetime.year)+str(dir_datetime.month).rjust(2,'0')+str(dir_datetime.day).rjust(2,'0')+'_'+str(dir_datetime.hour).rjust(2,'0')+str(dir_datetime.minute).rjust(2,'0')+'_'+'EST'
dir_name=str(dir_datetime.year)+str(dir_datetime.month).rjust(2,'0')+str(dir_datetime.day).rjust(2,'0')

current_dir=os.getcwd()
dest_dir=os.path.join(current_dir,dir_name)

isExist = os.path.exists(dest_dir)


if not isExist:
  os.makedirs(dest_dir)