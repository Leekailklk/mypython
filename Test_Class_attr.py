# -*- coding:utf-8 -*-
class TestA:
    attrA=1
    def __init__(self):
        self.attrA=42
TestClassA=TestA()
TestClassA.attrA=42
Obj_B=TestA()
print(TestA.__dict__)
print(Obj_B.__dict__)