#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/8 16:25
# @Author : CT
# @Site : 
# @File : test11.py
# @Software: PyCharm

#这个文件主要来通过get、post等方法来进行http请求，并拿到请求响应。

import requests
import json
#
# headers = {
#         'content-type': 'application/x-www-form-urlencoded',
#         'User-Agent': 'okhttp/3.8.1'
#     }

#,headers=headers

class Run_http():


    #定义post请求方法.参数url和data
    def post_method(self,url,data,headers):
        # print(url, data,headers)
        response = requests.post(url=url,data=data,headers=headers).json()
        # print(response.text)
        # res=response.text
        res = json.dumps(response, ensure_ascii=False, sort_keys=True, indent=2)
        # print(res)
        return res


    def get_method(self,url,data,headers):
        response = requests.get(url= url,params=data,headers=headers).json()
        res = json.dumps(response, ensure_ascii=False, sort_keys=True, indent=2)
        return res


    def run_http(self,method, url, data,headers):
        # print(url, data)
        result = None
        if method =="post":
            # print(url,data)
            result=self.post_method(url,data,headers)

        elif method=="get":
            result = self.get_method(url,data,headers)

        else:
            print("method值错误")

        return result



