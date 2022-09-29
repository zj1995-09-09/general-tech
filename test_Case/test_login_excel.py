# encoding: utf-8
# @author: MrZhou
# @file: test_login_excel.py
# @time: 2022/9/29 11:10
# @desc:
import openpyxl
from common import excel_handler
import pytest
from common.requests_handler import RequestsHandler

caseDir = 'E:\KT03\jiekou\data\APICase.xlsx'
data = excel_handler.ExcelHandler(caseDir).read('Sheet1')
print(data)


@pytest.mark.parametrize('info', data)
def test_login(info):
    req = RequestsHandler()
    res = req.visit(method=info['method'], url=info['url'], data=eval(info['params']))
    print(res)
    print(res['msg'])
    try:
        assert res['msg'] == eval(info['expect'])['msg']
        print("小可爱恭喜你成功了")
    except AssertionError as e:
        raise e
