#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/8 16:25
# @Author : CT
# @Site : 
# @File : test11.py
# @Software: PyCharm


#判断token是否存在
import jsonpath

from common import configHttp
from testFile import readConfig
from testFile import getpathInfo
import json

import  requests
#实例化对象
Run_http = configHttp.Run_http()
readConfig = readConfig.ReadConfig()
#定义header头
headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'User-Agent': 'okhttp/3.8.1',
        'x-safe-key':''

    }

#登录获取token，将token写入headers中
# print( readConfig.get_http('baseurl'))

url_login = readConfig.get_http('scheme')+ "://" +readConfig.get_http('baseurl')+"/v1/auth/auth"   #登录接口
# print(url_login)
data = {
    "area_code":"+86",
    "tel":"18080836440",
    "code":"123456",
    "device":"",
    "device_type":"1" #1代表安卓手机

}



results = Run_http.run_http('post', url_login, data, headers)

def get_token():
    token=json.loads(results)["data"]["token"]
    if token in results:
        # headers.append(token)
        headers['x-safe-token']=token
        # print(headers)

    else:
        print("token不存在")
    return headers

#
# def get_headers():
#     if 'x-safe-token' not in headers:
#         headers = get_token()
#
#     else:
#         return headers
        # token = json.loads(results)["data"]["token"]


# results = requests.post(url=url_login,data=data,headers=headers)
# results=Run_http.run_http('post',url_login,data,headers)
# print(get_headers())
# print(json.loads(results)["data"]["token"])#输出是文本需要用json.loads加载才能取值成功


# {"data":{"id":88,"role":"1","token":"554eec6f45ded5f8acfa01242a959c54","nick_name":"flash_6440"