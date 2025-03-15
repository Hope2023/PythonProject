def say_hello(name):
    """
    自动返回姓名say hello
    :param name:姓名
    :return:say Hello XXX or None
    """
    if len(name)>0:
       return "Hello %s!" % name
    else:
        return None

print(say_hello("Allen"))
print(say_hello(""))



def sayHi(name):
    print( "Hello %s!" % name)

print(sayHi('Allen'))
print(type(sayHi('Allen')))



if not say_hello('Allen'):
    print('true')
else:
    print('false')