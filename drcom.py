#!/usr/bin/python2.7
# coding: UTF-8
# 登录校园网小脚本
# create date: 2013
import urllib
import urllib2
import sys

url = "http://192.168.168.168"
logouturl = url + "/" + "F.htm"

values = ({
            '0MKKey': '',
            'DDDDD': '110*****', # 校园卡号
            'upass': '******' # 上网密码，默认身份证后6位
        })

data = urllib.urlencode(values)
data = data.encode('utf-8')

req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
response_info = urllib2.urlopen(url)
html = response_info.read()

time_used = int(html[157:167])
flux_used = float(html[175:185])
money_left = float(html[200:210])

print """
        ######################################

        已使用时间 Used time: {0} Mins
        已使用流量 Used flux: {1:.3f} MBytes
        所剩余额   Balance:   {2:.2f} 元RMB

        ######################################
    """.format( time_used, (flux_used/1024.0), (money_left/10000.0))

print "\n\nEnter Off to log out....... "

choice = ''

while 1:
    choice = raw_input("")
    if (choice != "Off" and choice != "off"):
        print "Wrong choice" 
    else:
        #171-181time 189-199flow 214-224 money
        html = urllib2.urlopen(logouturl).read()

        time_used_o = int(html[171:181])
        time_s = time_used_o - time_used 

        flux_used_o = float(html[189:199])
        flux_s = flux_used_o - flux_used

        money_left_o = float(html[214:224])
        money_s = money_left - money_left_o
        

        print """
            ######################################

            本次使用时间 Used time: {0} Mins
            本次使用流量 Used flux: {1:.3f} MBytes
            本次消费  Balance:   {2:.2f} 元RMB


            总使用时间 Used time: {3} Mins 
            总使用流量 Used flux: {4:.3f} MBytes
            所剩余额   Balance:   {5:.2f} 元RMB

            ######################################
            """.format( time_s, (flux_s/1024.0), (money_s/10000.0), time_used_o, (flux_used_o/1024.0), (money_left_o/10000.0))
        sys.exit()
