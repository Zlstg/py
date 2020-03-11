#coding:utf-8
#BMI公式（体重除以身高的平方）
#根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
name = input('请输入你的名字：')
height = input('请输入你的身高(单位\米)：')
weight = input('请输入你的体重(单位\kg)：')
h = float(height)
w = float(weight)
bmi = w / h ** 2
if bmi < 18.5:
    print('你好',name,'你的身高(单位\米)是：',height,'你的体重(单位\kg)是：',weight,'---苗条过头了！')
elif bmi < 25:
    print('你好',name,'你的身高(单位\米)是：',height,'你的体重(单位\kg)是：',weight,'---刚刚好呢！')
elif bmi < 28:
    print('你好',name,'你的身高(单位\米)是：',height,'你的体重(单位\kg)是：',weight,'---微胖最好了！')
elif bmi < 32:
    print('你好',name,'你的身高(单位\米)是：',height,'你的体重(单位\kg)是：',weight,'---你太胖了哈！')
else:
    print('你好',name,'你的身高(单位\米)是：',height,'你的体重(单位\kg)是：',weight,'---你还敢吃饭啊！')
input('按任意键退出!')