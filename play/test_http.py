import request

res = request.get(
    url='https://blog.csdn.net/weixin_44513945'    #wode CSDN博客
)

print(res.url)

print(res.text)
