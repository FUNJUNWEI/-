# -*- coding: utf-8 -*-
import requests
import datetime  # 获取日期
import json
import webbrowser

# 定义请求的url
url = 'http://xff.iot688.com/Api/flowsearch?cardno=8986112025003******'

# 定义求请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Cookie': '******************cookie**********************************'}


# 取时间 格式为202001/202112
def nowtime():
    datetime.datetime.now().year
    datetime.datetime.now().month
    datetime.datetime.now().day
    if len(str(datetime.datetime.now().month)) == 1:
        month = '0' + str(datetime.datetime.now().month)
        return 'used' + str(datetime.datetime.now().year) + month
    else:
        return 'used' + str(datetime.datetime.now().year) + str(datetime.datetime.now().month)

def makeHTML(argtime,argsurplus,arguseddata,argtotal,argbalance):
    # 命名生成的html
    GEN_HTML = "/www/wwwroot/jfun.ltd/python/data.html"
    # 打开文件，准备写入
    f = open(GEN_HTML, 'w')
    # 准备相关变量
    str1 = argtime
    str2 = argsurplus
    str3 = arguseddata
    str4 = argtotal
    str5 = argbalance

    # 写入HTML界面中
    message = """
    <html>
    <head></head>
    <body>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    </body>
    </html>
    """ % (str1, str2,str3,str4,str5)
    # 写入文件
    f.write(message)
    # 关闭文件
    f.close()
    print('makehtml:ok')

    # 运行完自动在网页中显示
 #   webbrowser.open(GEN_HTML, new=1)
    '''
    webbrowser.open(url, new=0, autoraise=True) 
    Display url using the default browser. If new is 0, the url is opened in the same browser window if possible. If new is 1, a new browser window is opened if possible. If new is 2, a new browser page (“tab”) is opened if possible. If autoraise is True, the window is raised if possible (note that under many window managers this will occur regardless of the setting of this variable).
    '''
    


# request.get获取数据
res = requests.get(url)
code = res.status_code  # 获取相应状态码
data = res.json()  # 获取数据列表
time = str(datetime.datetime.now())[:-7]

# if code ==200:
#    with open('./test.json','w',encoding='utf-8')as  fp:
#        fp.write(res.text)
# print(data)

if code == 200:
    surplus = '\n剩余流量：' + str(data['data']['surplus'])+ 'MB' + '\n'   # 套餐剩余量

    # autoname = data['data']['autoname'] #套餐名

    useddata = '已用流量：' + str(data['data'][nowtime()])  + 'MB'  # 套餐使用量
    totaldata ='\n总流量：' + str(int(float(data['data'][nowtime()]) + float(data['data']['surplus']))) + 'MB' # 套餐总量
    balance = '\n\n余额：'+ str(data['data']['balance'])+ '元'  # 余额

    print(time + surplus + useddata + totaldata + balance)

#json
    data_dict = {'surplus': data['data']['surplus'],
                 'useddata': float(data['data'][nowtime()]),
                 'totaldata ': (float(data['data'][nowtime()]) + float(data['data']['surplus'])),
                 'balance': data['data']['balance']
                 }


    with open('/www/wwwroot/jfun.ltd/python/data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data_dict, ensure_ascii=False))
    f.close()

#text
    with open('/www/wwwroot/jfun.ltd/python/data.text', 'w')as fp:
        fp.write(time + surplus + useddata + totaldata + balance)
    print('maketext:ok')

#makeHTML 【argtime,argsurplus,arguseddata,argtotal,argbalance】
    makeHTML(time,surplus,useddata,totaldata,balance)
    print('makejson:ok')
else:
    print('Error , 连接服务器失败！')

