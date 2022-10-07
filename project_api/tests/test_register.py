"""测试注册功能。

"""
import requests
import pytest
from middleware.handler import YZHandler

data = YZHandler.excel.read('register')


@pytest.mark.parametrize("test_info", data)
def test_register_01(test_info):
    """注册用例。"""
    # YZHandler.new_phone = YZHandler.generate_new_phone()


    actual_url = test_info['url']
    actual_method = test_info['method']
    actual_json = test_info['json']
    actual_headers = test_info['headers']
    expected = test_info['expected']

    # 读取 test_info['json']
    # 如果存在#new_phone#
    if '#new_phone#' in actual_json:
        # 生成手机号码 generate_new_phone
        # 13789456789 替换 #new_phone#
        phone = YZHandler.generate_new_phone()
        actual_json = actual_json.replace('#new_phone#', phone)

    if '#exist_phone#' in actual_json:
        pass

    resp = requests.request(method=actual_method,
                            url=YZHandler.yaml_config['host'] + actual_url,
                            headers=eval(actual_headers),
                            json=eval(actual_json))
    print(actual_json)
    resp_body = resp.json()

    try:
        assert resp_body['code'] == expected

    except AssertionError as e:
        YZHandler.logger.error("用例失败:{}".format(e))
        # 一定要记得抛出
        raise e
    # 写入excel
    # finally:
    #     excel = ExcelHandler(excel_file)
    #     excel.write('register',
    #                 str(resp_body),
    #                 row=int(test_info['case_id']) + 1,
    #                 column=9
    #                 )
