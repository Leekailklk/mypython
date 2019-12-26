# -*- coding:utf-8 -*-
import logging
logfilename='logtest.log'
logging.basicConfig(filename=logfilename,filemode='w',level=logging.INFO)
logging.info("logtest ok easy?")