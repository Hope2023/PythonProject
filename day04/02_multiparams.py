#位置参数
def user_info(name,age,gender):
    print(f'name={name},age={age},gender={gender}')

user_info('Allen',35,'male')


#关键字参数

def user_info2(name,age,gender):
    print(f'name={name},age={age},gender={gender}')

user_info2(name='Allen',age=35,gender='male')
#无序
user_info2(age=35,name='Allen',gender='male')
#混用
user_info2('Allen',age=35,gender='male')

#   缺省参数

#默认参数必须放到最后一个
def user_info3(name,age,gender='male'):
    print(f'name={name},age={age},gender={gender}')

user_info3('Allen', age=35)
user_info3('Allen', age=35, gender='female')


#不定长参数 位置不定长参数 *args  args 是元祖类型
def user_info4(*args):
    print(args)

user_info4('Allen')
user_info4('Allen', 35)


#不定长参数 关键字不定长参数 **kwargs  是字典类型  k-v  形式传参
def user_info5(**kwargs):
    print(f'argcs参数类型是：{type(kwargs)},内容是{kwargs}')

user_info5(name='Allen', age=35)






