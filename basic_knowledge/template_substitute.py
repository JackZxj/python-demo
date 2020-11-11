from string import Template

s = Template('My name is $name, I am $age years old.')

print(s.substitute(name='jack', age=18))
# My name is jack, I am 18 years old.

print(s.substitute(name='jack', age=18, food='apple'))
# My name is jack, I am 18 years old.

# print(s.substitute(name='jack'))
# ERROR

print(s.safe_substitute(name='jack'))
# My name is jack, I am ${age} years old.

print(s.safe_substitute(name='jack', age=18, food='apple'))
# My name is jack, I am 18 years old.

# $identifier 变量由一个占位符替换(key)，key去匹配变量 "identifier"
# ${identifier}相当于 $identifier. 它被用于当占位符后直接跟随一个不属于占位符的字符，列如 "${noun}ification"
ss = Template('${name}_is_a_student, he_like_${fruit}juice')
print(ss.substitute(name='jack', fruit='apple'))
# jack_is_a_student, he_like_applejuice

# $$ 是转义输出$
sss = Template('$$who is a $job')
print(sss.substitute(who='jack', job='student'))
# $who is a student
