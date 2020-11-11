def aaa(*args):
    print('type:%s, value:%s' % (type(args), args))


def bbb(a, **kw):
    print(a)
    print('type:%s, value:%s' % (type(kw), kw))


def ccc(a, **kw):
    bbb(a, b=0, **kw)


aaa(1, 2, 3)
## type:<class 'tuple'>, value:(1, 2, 3)

ccc(1, c=1, d=2)
## 1
## type:<class 'dict'>, value:{'b': 0, 'c': 1, 'd': 2}

# ccc(1, a=1, b=2)
## TypeError: ccc() got multiple values for argument 'a'
