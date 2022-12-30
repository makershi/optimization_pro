name = '小红'
sex = '男'
age = 18
money = 20.56
#正确拼接
print('你是'+ name +'性别为' + sex)   
#错误拼接（报错显示：TypeError: must be str（字符串）, not int（整型））
#print('你是'+ name +',性别为' + sex + ',年龄' + age)  
#使用强制类型转换，进行拼接
print('你是'+ name +',性别为' + sex + ',年龄' + str(age) + '，有' + str(money) + '钱')  
