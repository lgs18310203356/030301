import pytest
import allure
import os
from guosong220124 import readConfig as readConfig
from guosong220124.common.Log import MyLog as Log
import subprocess

proDir=readConfig.proDir
#print(proDir)
reportPath = os.path.join(proDir,"allure-report")
resultPath= os.path.join (proDir,"allure-result")

#创建报告地址
'''if not os.path.exists(reportPath):
    os.mkdir(reportPath)
if not os.path.exists(resultPath):
    os.mkdir(resultPath)'''

if __name__ == '__main__':
    log=Log.get_log()
    logger=log.get_logger()
    logger.info("----测试开始----")

    # "--alluredir","./allure-result"  生成测试数据的json文件 保存到 allure-result文件中
    # --clean-alluredir 清除掉之前生成的json 文件
    pytest.main(["-s","D:\测试资料\pycharm-project\myproject\guosong220124\\testcase","--alluredir","./allure-result","--clean-alluredir"])
    # print(os.getcwd())
    os.system("allure generate --clean  ./allure-result -o ./allure-report/")
    os.system("allure serve D:\测试资料\pycharm-project\myproject\guosong220124\\allure-result")
    # os.system("allure open D:\测试资料\pycharm-project\myproject\guosong220124\\allure-report")
    '''allure使用了两种方式来渲染页面。
    分别是 allure open 和 allure serve。
    前者用于在本地渲染和查看结果，后者用于在本地渲染后对外展示结果。这里我们使用allure open。运行命令'''

