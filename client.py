# -*- coding:utf-8 -*-
import sys
from cmd import Cmd
from random import choice
from string import ascii_lowercase
from threading import Thread
from time import sleep
from xmlrpc.client import ServerProxy, Fault
import logging
logfilename='logfile1.log'
logging.basicConfig(filename=logfilename,filemode='a',level=logging.INFO)
from server import Node, UNHANDLED

HEAD_START = 0.1  # 单位为秒 SECRET_LENGTH = 100
SECRET_LENGTH = 100

def random_string(length):
    """    返回一个指定长度的由字母组成的随机字符串    """
    chars = []
    letters = ascii_lowercase[:26]
    while length > 0:
        length -= 1
        chars.append(choice(letters))
    return ''.join(chars)


class Client(Cmd):
    """    一个基于文本的界面，用于访问Node类    """
    prompt = '> '

    def __init__(self, url, dirname, urlfile):
        """ 设置url、dirname和urlfile，并在一个独立的线程中启动Node服务器  """
        Cmd.__init__(self)
        self.secret = random_string(SECRET_LENGTH)
        n = Node(url, dirname, self.secret)
        t = Thread(target=n._start)
        t.setDaemon(1)
        t.start()
        # 让服务器先行一步：
        sleep(HEAD_START)
        logging.info("  start server  ")
        logging.info(url)
        self.server = ServerProxy(url)
        for line in open(urlfile):
            line = line.strip()
            self.server.hello(line)
            logging.info("  server.hello  ")
            logging.info(line)

    def do_fetch(self, arg):
        "调用服务器的方法fetch"
        try:
            self.server.fetch(arg, self.secret)
            logging.info("   fetch the file  ")
            logging.info(arg)
        except Fault as f:
            if f.faultCode != UNHANDLED: raise
            print("Couldn't find the file", arg)
            logging.info("   Couldn't find the file  ")
            logging.info(arg)

    def do_exit(self, arg):
        "退出程序"
        print("exit...")
        logging.info("...exit...")
        sys.exit()
        do_EOF = do_exit  # EOF与'exit'等价


def main():

    urlfile, directory, url = sys.argv[1:]
    logging.info("   start   ")
    logging.info(sys.argv)
    client = Client(url, directory, urlfile)
    client.cmdloop()
if __name__ == '__main__': main()
