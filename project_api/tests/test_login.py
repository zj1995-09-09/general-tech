import pytest
import requests

from middleware.handler import YZHandler

data = YZHandler.excel.read('login')

@pytest.mark.parametrize('info', data)
def test_login(info):
    request_data = info['data']
    if '*phone*' in request_data:
        new_phone = YZHandler.help_funcs.generate_new_phone()
        request_data = request_data.replace('*phone*', new_phone)

    if '#phone#' in request_data:
        phone = YZHandler.user_config['investor_user']['phone']
        request_data = request_data.replace('#phone#', phone)

    if '#pwd#' in request_data:
        pwd = YZHandler.user_config['investor_user']['pwd']
        request_data = request_data.replace('#pwd#', pwd)

    # print(request_data)
    # print(info)

    resp = requests.request(method=info['method'],
                            url=YZHandler.yaml_config['host'] + info['url'],
                            headers=eval(info['headers']),
                            json=eval(request_data))
    try:
        assert resp.json()['msg'] == info['expected']
    except AssertionError as e:
        YZHandler.logger.error(e)
        YZHandler.logger.info("测试数据: {}".format(request_data))
        raise e
