# -*- coding:utf-8 -*-
import sys
from os.path import join, abspath, isfile
from urllib.parse import urlparse
from xmlrpc.client import ServerProxy, Fault
from xmlrpc.server import SimpleXMLRPCServer

SimpleXMLRPCServer.allow_reuse_address = 1
MAX_HISTORY_LENGTH = 6
UNHANDLED = 100
ACCESS_DENIED = 200


class UnhandledQuery(Fault):
    """    表示查询未得到处理的异常    """

    def __init__(self, message="Couldn't handle the query"):
        super().__init__(UNHANDLED, message)


class AccessDenied(Fault):
    """    用户试图访问未获得授权的资源时将引发的异常    """

    def __init__(self, message="Access denied"):
        super().__init__(ACCESS_DENIED, message)


def inside(dir, name):
    """    检查指定的目录是否包含指定的文件    """
    dir = abspath(dir)
    name = abspath(name)
    return name.startswith(join(dir, ''))


def get_port(url):
    """    从URL中提取端口号    """
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])


class Node:
    """    P2P网络中的节点    """

    def __init__(self, url, dirname, secret):
        self.url = url
        self.dirname = dirname
        self.secret = secret
        self.known = set()

    def query(self, query, history=[]):
        """  查询文件（可能向已知节点寻求帮助），并以字符串的方式返回它  """
        try:
            return self._handle(query)
        except UnhandledQuery:
            history = history + [self.url]
            if len(history) >= MAX_HISTORY_LENGTH: raise
            return self._broadcast(query, history)

    def hello(self, other):
        """    用于向其他节点介绍当前节点    """
        self.known.add(other)
        return 0

    def fetch(self, query, secret):
        """    用于让节点查找并下载文件    """
        if secret != self.secret:
            raise AccessDenied
        result = self.query(query)
        f = open(join(self.dirname, query), 'w')
        f.write(result)
        f.close()
        return 0

    def _start(self):
        """    供内部用来启动XML-RPC服务器    """
        s = SimpleXMLRPCServer(("", get_port(self.url)), logRequests=False)
        s.register_instance(self)
        s.serve_forever()

    def _handle(self, query):
        """  供内部用来处理查询  """
        dir = self.dirname
        name = join(dir, query)
        if not isfile(name): raise UnhandledQuery
        if not inside(dir, name): raise AccessDenied
        return open(name).read()

    def _broadcast(self, query, history):
        """  供内部用来向所有已知节点广播查询  """
        for other in self.known.copy():
            if other in history: continue
            try:
                s = ServerProxy(other)
                return s.query(query, history)
            except Fault as f:
                if f.faultCode == UNHANDLED:
                    pass
                else:
                    self.known.remove(other)
            except:
                self.known.remove(other)
        raise UnhandledQuery


def main():
    url, directory, secret = sys.argv[1:]
    n = Node(url, directory, secret)
