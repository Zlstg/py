#coding:utf-8
user_name = "xiaoming"
user_age = 18
print("name:",user_name,"age",user_age)
#用 sep 指定分隔符
print("name:",user_name,"age:",user_age,sep='|')
#设置end参数，指定输出以后不再换行
print("沧海月明珠有泪",'\t',end='')
print("蓝田日暖玉生烟",'\t',end='')
#打开文件写入
f = open('gushi.txt','w')
print("沧海月明珠有泪",file=f)
print("蓝田日暖玉生烟",file=f)
