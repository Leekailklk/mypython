# encoding:UTF-8
def yield_test(n):
    for j in range(n):
        yield call(j)
        print("j=", j)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2


# 使用for循环
for i in yield_test(5):
    print(i, ",")
    #print("i,=", i)