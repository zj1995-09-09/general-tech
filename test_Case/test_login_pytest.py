# encoding: utf-8
# @author: MrZhou
# @file: test_loginpy.py
# @time: 2022/9/28 11:06
# @desc:

import pytest
from common.requests_handler import RequestsHandler
import allure_pytest

class TestLogin:
    # 2.4用户列表
    def test_userlist(self, f4):
        userlist_url = 'http://www.joysurvey.com:8089/survey/man/user/list?pageNo=1&pageSize=100'
        token = f4
        headers_userlist = {'token': token}
        # payload = {
        #     'pageNo': 1, 'pageSize': 100
        # }
        resp_userlist = RequestsHandler().visit('get', userlist_url, headers=headers_userlist)
        print(resp_userlist)
        assert '0000' == resp_userlist['code']

    # 2.5添加新用户
    @pytest.mark.parametrize('a,b,c,d,e', [('zj14', '13075509405', '123456789A!', '123456789A!', '1'),
                                           ('zj15', '13075509406', '123456789A!', '123456789A!', '1')])
    def test_useradd(self, a, b, c, d, e, f4):
        useradd_url = 'http://www.joysurvey.com:8089/survey/man/user/add'
        token = f4
        headers_add = {'token': token}
        payload = {
            'username': a,
            'phone': b,
            'password1': c,
            'password2': d,
            'status': e
        }
        resp_useradd = RequestsHandler().visit('post', useradd_url, data=payload, headers=headers_add)
        print(resp_useradd)
        assert '1001' == resp_useradd['code']

    # 2.6编辑用户信息
    def test_update(self, f4):
        update_url = 'http://www.joysurvey.com:8089/survey/man/user/update'
        token = f4
        headers_update = {'token': token}
        payload = {
            'id': '37',
            'username': 'zj11',
            'phone': '13075509402',
            'status': 1
        }
        resp_update = RequestsHandler().visit('post', update_url, data=payload, headers=headers_update)
        print(resp_update)
        assert '2001' == resp_update['code']

    # 2.7重置密码
    def test_resetPassword(self, f4):
        reset_url = 'http://www.joysurvey.com:8089/survey/man/user/resetPassword'
        token = f4
        headers_reset = {'token': token}
        payload = {
            'id': '37',
            'password1': '123456789A!',
            'password2': '123456789A!'
        }
        resp_reset = RequestsHandler().visit('post', reset_url, data=payload, headers=headers_reset)
        print(resp_reset)
        assert '1001' == resp_reset['code']

    # 2.9用户详情
    def test_userinfo(self, f4):
        userinfo_url = 'http://www.joysurvey.com:8089/survey/man/user/detail'
        # global token
        token = f4
        headers_userinfo = {'token': token}

        payload = {
            'phone': '18888888888', 'password': '123456789A!'
        }
        resp_userinfo = RequestsHandler().visit('get', userinfo_url, data=payload, headers=headers_userinfo)

        assert '0000' == resp_userinfo['code']

    # 2.8登出
    def test_logout(self, f4):
        logout_url = 'http://www.joysurvey.com:8089/survey/man/user/logout'
        token = f4
        headers_logout = {'token': token}
        payload = {
            'phone': '18888888888!',
            'password': '123456789A!'
        }
        resp_logout = RequestsHandler().visit('post', logout_url, data=payload, headers=headers_logout)
        print(resp_logout)
        assert '0000' == resp_logout['code']


if __name__ == '__main__':
    pytest.main(["-vs"])
