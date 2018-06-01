#!/usr/bin/env python
# -*- coding:utf-8 -*-
import netifaces as ni
ni.ifaddresses('wlp3s0')
#ip = ni.ifaddresses('wlp3s0')[ni.AF_INET][0]['addr']
ip = ni.ifaddresses('wlp3s0')[ni.AF_LINK][0]['addr']
print(str(ip))
