"""充值接口测试"""

import pytest
import json
from decimal import Decimal
import requests
from middleware.handler import YZHandler

data = YZHandler.excel.read('recharge')

data_info = {"token": ''}


@pytest.mark.parametrize('info', data)
def test_recharge(info, login_investor, db):
    """充值"""
    # YZHandler.investor_user_id = login_investor['id']

    # 先要替换
    if "#member_id#" in info['data']:
        info["data"] = info["data"].replace('#member_id#', str(login_investor['id']))

    # token 组装方式 1：通过excel 替换
    # if "#token#" in info['headers']:
    #     info["headers"] = info["headers"].replace('#token#', login['token'])

    # token 组装2： 通过 headers 添加
    headers = json.loads(info["headers"])
    headers['Authorization'] = login_investor['token']

    # #beyond_balace#
    if "*wrong_member_id*" in info['data']:
        info["data"] = info["data"].replace('*wrong_member_id*', str(login_investor['id'] + 1))

    # 数据库访问，充值之前的余额
    # db = DBHandler()
    sql = 'select leave_amount from member where id={}'.format(login_investor['id'])
    result = db.query(sql)
    money_before = result['leave_amount']
    # db.close()

    data = json.loads(info['data'])

    resp = requests.request(url=YZHandler.yaml_config['host'] + info['url'],
                            method=info['method'],
                            headers=headers,
                            json=data)
    assert resp.json()['code'] == info['expected']

    # if info['interface'] == '登陆':
    #     data_info['token'] = resp.json()["token"]

    if resp.json()['code'] == 0:
        # db = DBHandler()
        sql = 'select leave_amount from member where id={}'.format(login_investor['id'])
        result = db.query(sql)
        money_after = result['leave_amount']
        # db.close()
        money = Decimal(str(data['amount']))
        assert money_before + money == money_after

    # except:
    #     print(info['json'])
