# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('https://www.python.org/jobs/').read()
soup = BeautifulSoup(text, 'html.parser')
jobs = set()
i=1
for job in soup.body.section('h2'):
    print(i,end=":  ")
    print(job)
    print('{} ({})'.format(job.a.string, job.a['href']))
    i=i+1
    #jobs.add('{} ({})'.format(job.a.string, job.a['href']))
#print('\n'.join(sorted(jobs, key=str.lower)))
