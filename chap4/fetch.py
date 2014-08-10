# -*- coding: utf-8 -*-

import urllib.request as request

baseurl = 'http://www.e-stat.go.jp/SG1/estat/Xlsdl.do'
ids = {
    'pop':   '000009849932',
    'unemp':   '000009849937',
    'crime': '000009849942',
}

for name, sinfid in ids.items():
    url = baseurl + '?sinfid=' + sinfid
    request.urlretrieve(url, name + '.xls')

