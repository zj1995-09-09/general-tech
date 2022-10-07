import pytest
import requests
import json
from jsonpath import jsonpath

from middleware.handler import YZHandler

data = YZHandler.excel.read('invest')


@pytest.mark.parametrize('info', data)
def test_audit(info):
    # 要保证替换成功，excel当中的 #investor_phone# 必须和属性名保持一致。
    # info转化成json字符串
    info = json.dumps(info)
    # 替换
    info = YZHandler.replace_data(info)
    # 转化成字典
    info = json.loads(info)

    resp = requests.request(url=YZHandler.yaml_config['host'] + info['url'],
                            method=info['method'],
                            headers=json.loads(info['headers']),
                            json=json.loads(info['json']))
    assert resp.json()['code'] == info['expected']

    # 设置YZHandler对应的属性。
    if info['extractor']:
        extrators = json.loads(info['extractor'])
        for yz_prop, jsonpath_exp in extrators.items():
            # value = 'token'
            value = jsonpath(resp.json(), jsonpath_exp)[0]
            # setastr(YZHandler, "loan_token", "yfowepfpwefwoefowf"
            setattr(YZHandler, yz_prop, value)
