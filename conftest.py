# -*- coding: utf-8 -*-
import logging
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s >>> %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=os.path.join(os.getcwd(), 'mylog.log'),
                    filemode='a')
'''
import pytest
import os
from guosong220124 import readConfig as readConfig
import pytest
import requests

from guosong220124.common import ConfigHttp as ConfigHttp
from guosong220124.common import CommonMethod as CommonMethod

localConfigHttp=ConfigHttp.ConfigHttp()
localreadConfig=readConfig.ReadConfig()

baseUrl=localreadConfig.get_http("baseurl")

@pytest.fixture()
def qi_Yong():
    headers = CommonMethod.get_Authorization()
    localConfigHttp.set_headers(headers)
    qiyongpath = "/rpo/job/batchReleaseJobs"
    url = baseUrl + qiyongpath
    localConfigHttp.set_url(url)

    data = {
        "rpoRootOrgId": localreadConfig.get_variable("rpoRootOrgId"),
        "list": [
            {
                "jobId":  localreadConfig.get_variable("jobId"),
                "rpoJobId": localreadConfig.get_variable("rpoJobId"),
                "jobNumber": "CCL1318355140J40233815403"
            }
        ],
        "projectId":  localreadConfig.get_variable("projectId"),
        "isProject": False,
        "rpoStaffId": localreadConfig.get_variable("rpoStaffId")
    }
    localConfigHttp.set_data(data)
    response=localConfigHttp.post().json()
    zpageTotal = CommonMethod.get_List(30, 13)   # 暂停状态职位记录条数
    return(zpageTotal)
    #print(headers)



#@pytest.mark.usefixtures("qi_Yong")


@pytest.fixture()
def test_Zanting(request):  # pytest 内 request 传参固定写法，用request.param 来接收传入的值并调用
    data=request.param
    rpoRootOrgId=data[0]
    jobId=data[1]
    rpoJobId=data[2]
    jobNumber=data[3]
    projectId=data[4]
    rpoStaffId=data[5]
    code=data[6]
    message=data[7]

    headers = CommonMethod.get_Authorization()
    zantingpath="/rpo/job/batchSuspendJobs"
    url=baseUrl+zantingpath
    localConfigHttp.set_url(url)
    localConfigHttp.set_headers(headers)

    data= {
    "rpoRootOrgId": rpoRootOrgId,
    "list": [
        {
            "jobId":  jobId,
            "rpoJobId": rpoJobId,
            "jobNumber": jobNumber
        }
    ],
    "projectId":  projectId,
    "isProject": False,
    "rpoStaffId": rpoStaffId
}
    localConfigHttp.set_data(data)

    response=localConfigHttp.post()
    r=response.json()

    print("\n")
    print({"code":    r["code"], "message": r["message"], "rpoRootOrgId": rpoRootOrgId, "jobId": jobId, "rpoJobId": rpoJobId,
    "jobNumber": jobNumber, "projectId": projectId, "rpoStaffId": rpoStaffId})

    return (response.json(), code, message)

    # 判断暂停职位接口code返回









'''