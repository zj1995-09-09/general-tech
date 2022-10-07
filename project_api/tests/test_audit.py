"""审核项目"""
import pytest
import requests
import json
from jsonpath import jsonpath

from middleware.handler import YZHandler

data = YZHandler.excel.read('audit')

@pytest.mark.parametrize('info', data)
def test_audit(info, admin_login, add_loan):
    """审核接口"""
    # 数据替换
    if "#loan_id#" in info['json']:
        info['json'] = info['json'].replace("#loan_id#", str(add_loan))
    json_data = json.loads(info['json'])

    # 添加 admin token 放到 headers
    headers = json.loads(info['headers'])
    headers['Authorization'] = admin_login['token']

    resp = requests.request(url=YZHandler.yaml_config['host'] + info['url'],
                            method=info['method'],
                            headers=headers,
                            json=json_data)
    print(resp.json())
    expected = json.loads(info['expected'])

    # 第一版多值断言
    # assert resp.json()['code'] == expected["code"]
    # assert resp.json()['msg'] == expected['msg']

    # 第二版多值断言
    # for key, value in expected.items():
    #     # ("code", 0)
    #     # ("msg", "OK")
    #     # try:
    #     assert resp.json()[key] == value

    # 第三版多值断言
    for key, value in expected.items():
        # 实际结果的value 怎么获取
        assert jsonpath(resp.json(), key)[0] == value




