#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits)\
    	for _ in range(length))

print(generate_key(16))
