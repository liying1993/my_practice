#!/usr/bin/python
#_*_ coding:utf-8 _*_
import argparse
import os
import json
import urllib2
# import urllib.request
import ssl
import sys
import re
import socket
from datetime import datetime


ADDR_CACHE_FILE = '.addr'
CITY_CACHE_FILE = '.cities'
CITY_CACHE = None
PURPOSE_CODES = ['ADULt', '0X00']
CITY_LIST_URL   = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
ACTION_URL      = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes={ticket_type}&queryDate={train_time}&from_station={from_city}&to_station={to_city}'
SSL_CTX = ssl.SSLContext(ssl.PROTOCOL_SSLv23)

def guide():
    import pdb
    pdb.set_trace()
    try:
        cities = load_cities()
        city = getaddr()
    except socket.timeout:
        print "请求超时"
        sys.exit(-1)

    if city and cities.has_key(city.decode('utf-8')):
        from_city = raw_input('请输入起始站点（输入回车为%s）:'%city)
        if not from_city:
            from_city = city
    else:
        from_city = raw_input('请输入起始站点：')
    while True:
        to_city = raw_input('请输入目的站点')
        if to_city:
            break
    dd = default_date()
    train_time = raw_input('请输入出发日期（输入回车为%s）:' %dd)
    train_time = date_format(train_time) if train_time else dd
    ticket_type = 'ADULT' if get_yn_input('是否成人票') else '0X00'
    print '正在查询。。。\n'
    search(from_city, to_city, train_time, ticket_type)
def get_yn_input(msg):
    import pdb
    pdb.set_trace()
    while True:
        res = raw_input('%s, 是请按回车，不是请输入n:'%msg)
        if res in ('', 'n'):
            break
    return True if res == None else False


def search(from_city, to_city, train_time, ticket_type='ADULT'):
    import pdb
    pdb.set_trace()
    cities = load_cities()
    try:
        from_code = cities[from_city.decode('utf-8')]
    except KeyError:
        print '指定起始站点%s不存在'%from_city
        sys.exit(-1)
    try:
        to_code = cities[to_city.decode('utf-8')]
    except KeyError:
        print '指定目标站点%s不存在'%to_city
        sys.exit(-1)
    url = ACTION_URL.format(from_city=from_code, to_city=to_code, train_time=train_time,ticket_type=ticket_type)
    ret = json.loads(urllib2.urlopen(url, context=SSL_CTX, timeout=10).read())
    if not ret or ret == -1 or not ret['data'].has_key('datas') or len(ret['data']['datas']) == 0:
        print '没查询到相关的车次信息'
        sys.exit(-1)
    print '车次序号        起始站   出发站   终点站   时间    一等座    二等座'
    for r in ret['data']['datas']:
        if (not r['zy_num'].encode('utf-8').isdigit()
            and not r['ze_num'].encode('utf-8').isdigit()
            or r['from_station_name'].encode('utf-8') != from_city):
            continue

        print u'%s  %s->%s->%s  %s   %s   %s' %(
            r['train_no'],
            r['start_station_name'],
            r['from_station_name'],
            r['to_station_name'],
            r['arrive_time'],
            r['zy_num'],
            r['ze_num']
        )


def date_format(input_date):
    import pdb
    pdb.set_trace()
    if not input_date:
        return default_date()
    res = re.match(r'(([0-9]{4})[-|\\|:])?([0-9]{1,2})[-|\\|:]([0-9]{2})', input_date)
    if res:
        year = res.group(2)
        month = res.group(3)
        day = res.group(4)
        now = datetime.now()
        if not year:
            year = now.year
        if not month:
            month = now.month
        if not day:
            day = now.day
        return '-'.join([str(year), add_zero(str(month)), str(day)])
    else:
        print '输入日期格式错误'
        sys.exit(-1)

def add_zero(month):
    import pdb
    pdb.set_trace()
    if int(month) < 10:
        month = '0'+str(int(month))
    return month


def default_date():
    import pdb
    pdb.set_trace()
    now = datetime.now()
    return '-'.join([str(now.year), str(add_zero(now.month)), str(add_zero(now.day))])

def getip():
    import pdb
    pdb.set_trace()
    url = "http://jsonip.com"

    res = re.search('\d+\.\d+\.\d+\.\d+', urllib2.urlopen(url, timeout=5).read())
    if res:
        return res.group(0)
    return None

def getaddr(fresh=False):
    import pdb
    pdb.set_trace()
    addr_cache_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ADDR_CACHE_FILE)
    if not fresh and os.path.exists(addr_cache_file):
        addr = None
        with open(addr_cache_file, 'rb') as fp:
            addr = fp.read()
        if addr:
            return addr
    ip = getip()

    if not ip:
        return None
    addr_info = urllib2.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip, timeout=5).read()
    city = None
    if addr_info:
        addr_info = json.loads(addr_info)
        city = addr_info['data']['city']
        city = city.encode('utf-8').replace('市', '')
        with open(addr_cache_file, 'w') as fp:
            fp.write(city)
    return city






def load_cities():
    import pdb
    pdb.set_trace()
    global CITY_CACHE
    if CITY_CACHE is not None:
        return CITY_CACHE
    cache_file  = os.path.join(os.path.dirname(os.path.abspath(__file__)), CITY_CACHE_FILE)
    need_reload = True
    cities      = {}
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as fp:
            cities = json.load(fp)
        if cities:
            need_reload = False

    if need_reload is True:
        city_info = urllib2.urlopen(CITY_LIST_URL, context=SSL_CTX).read()
        print "==========="
        print city_info
        for res in re.finditer(r'@[a-z]{3}\|(.+?)\|([A-Z]{3})\|[a-z]+?\|[a-z]+?\|', city_info):
            city         = res.group(1)
            code         = res.group(2)
            cities[city] = code
        with open(cache_file, 'w') as fp:
            json.dump(cities, fp)
    CITY_CACHE = cities
    print "++++"
    print cities
    return cities
# def load_cities():
#     global CITY_CACHE
#     if CITY_CACHE is not None:
#         return CITY_CACHE
#     cache_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), CITY_CACHE_FILE)
#     need_reload = True
#     cities = {}
#     if os.path.exists(cache_file):
#         with open(cache_file, 'rb') as fp:
#             cities =json.load(fp)
#         if cities:
#             need_reload = False
#     if need_reload is True:
#         city_info = urllib.request.urlopen(CITY_LIST_URL, context=SSL_CTX).read()
#         print(city_info)
#         for res in re.finditer(r'@[a-z]{3}\|(.+?)\|([A-Z]{3})\|[a-z]+?\|[a-z]+?\|', city_info):
#             city = res.group(1)
#             code = res.group(2)
#             cities[city] = code
#         with open(cache_file, 'w') as fp:
#             json.dump(cities, fp)
#     return cities

if __name__ == "__main__":
    guide()