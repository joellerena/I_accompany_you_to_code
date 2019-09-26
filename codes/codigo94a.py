# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:00:41 2019
"""
from multiprocessing.dummy import Pool as ThreadPool
import urllib3
pool = ThreadPool(4) 
urls = [
'https://www.ups.edu.ec', 'https://joellerena.info',
'https://www.google.com', 'http://www.youtube.com'
]
results = pool.map(urllib3.connection_from_url, urls)
for re in results:
    print(re)
pool.close() 
pool.join()

