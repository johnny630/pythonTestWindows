#!E:/Python27/python.exe
# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import re
from datetime import datetime , timedelta , date
# import datetime
import inspect

def base():
    #設定基本時間
    d1 = datetime(2016, 1, 5)
    d2 = datetime(2016, 5 ,6 , 14 ,30 ,12)
    now = datetime.now()

    #字串與時間互轉
    print datetime.strftime(d1, '%Y-%m-%d %H:%M:%S')
    print datetime.strptime("2015-01-12", '%Y-%m-%d')

    #日期時間加減
    # datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
    d3 = d2 + timedelta(days=1 , hours = 1 , minutes = 1 , seconds=1)


if __name__ == "__main__":
    base()