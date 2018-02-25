#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
#now = time.time()
#result = time.localtime(now)
result = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(result)
