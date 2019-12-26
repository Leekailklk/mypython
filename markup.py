# -*- coding:utf-8 -*-
import re
import sys

from handlers import *
from rules import *
from util import *


class Parser:
    """
    Parser读取文本文件，应用规则并控制处理程序
    """

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)

        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
                #print(block,"aaa")
            for rule in self.rules:
                #print(block,'bbb')
                if rule.condition(block):
                  last = rule.action(block, self.handler)
                if last: break
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    在构造函数中添加规则和过滤器的Parser子类
    """

    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


handler = HTMLRenderer()
parser = BasicTextParser(handler)
#parser.parse("test")
parser.parse(sys.stdin)
