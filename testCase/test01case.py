#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/8 16:25
# @Author : CT
# @Site : 
# @File : test11.py
# @Software: PyCharm

#读取caselist.xlsx中的用例，使用unittest来进行断言校验
#unittest断言测试case了
import json
import unittest

import paramunittest
from common import configHttp
# from testFile import get_token
from testFile import geturlParams
from testFile import readConfig
from testFile import readExcel
import urllib.parse
from testFile import get_token

#paramunittest是unittest实现参数化的一个专门的模块，可以传入多组参数，自动生成多个用例
# import paramunittest
from ddt import ddt,data,unpack


url = geturlParams.geturl_Now().get_url() #调用我们的geturlParams获取我们拼接的URL
get_token=get_token.get_token()#实例化获取登录凭证
print(url)
#读取Excel中的内容。获得列表数据,列表里的每一组就是一个用例
caselist_xls = readExcel.readExcel().get_xls('caselist.xlsx','Flash')
# print(caselist_xls)

#参数化获取的Excel数据
@paramunittest.parametrized(*caselist_xls) #列表里的每一组就是一个用例
class testFlash(unittest.TestCase):
    def setParameters(self, case_name, method,path, data): #初始化参数
        """
        set params
        :param case_name:
        :param path
        :param data
        :param method
        :return:
        """
        self.case_name = case_name
        self.path = path
        self.data= data
        self.method=method

    def description(self):
        self.case_name


    def setUp(self):
        print(self.case_name+"测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test01case(self):
        self.checkResult()

    def checkResult(self):#断言
         """
        check test result
        :return:

        """
         new_url = url+ self.path
         # print(new_url)
         # print(self.method)
         # print(self.data)
         # print(self.get)
         info = configHttp.Run_http().run_http(self.method, new_url, self.data,get_token)
         # print(info)
         ss=json.loads(info)## 将响应转换为json字典格式
         if self.case_name is not None:
             self.assertEqual(ss['msg'], "成功")  # 返回的msg应该是成功就合法。也可以用code状态码判断
             print(self.case_name + "接口请求执行成功")
         else:
             print(self.case_name + "接口请求执行失败")









