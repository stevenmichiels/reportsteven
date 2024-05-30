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

dir_datetime=datetime.now(timezone('UTC')).astimezone(timezone('US/Eastern'))
dir_name=str(dir_datetime.year)+'_'+str(dir_datetime.month).rjust(2,'0')+'_'+str(dir_datetime.day).rjust(2,'0')

url1 = "https://raw.githubusercontent.com/robcarver17/reports/master/Strategy_report"
url2="https://raw.githubusercontent.com/robcarver17/reports/master/Risk_report"
url3="https://raw.githubusercontent.com/robcarver17/reports/master/Trade_report"
file_name1 = dir_name+"_strategy_report.txt"
file_name2 = dir_name+"_risk_report.txt"
file_name3 = dir_name+"_trade_report.txt"

with urllib.request.urlopen(url1) as file:
    with open(file_name1, "wb") as f:
        f.write(file.read())
print(f"File '{file_name1}' downloaded successfully!")

with urllib.request.urlopen(url2) as file:
    with open(file_name2, "wb") as f:
        f.write(file.read())
print(f"File '{file_name2}' downloaded successfully!")

with urllib.request.urlopen(url3) as file:
    with open(file_name3, "wb") as f:
        f.write(file.read())
print(f"File '{file_name3}' downloaded successfully!")

