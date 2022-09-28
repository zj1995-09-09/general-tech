# encoding: utf-8
# @author: MrZhou
# @file: test_login_unittest.py
# @time: 2022/9/27 11:24
# @desc:
import token
import unittest
from common.requests_handler import RequestsHandler
import pytest

token = ''


class LoginTest(unittest.TestCase):
    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()

    def tearDown(self):
        self.req.close_session()

    def test_login_success(self):
        login_url = 'http://www.joysurvey.com:8089/survey/man/user/login'
        payload = {
            'phone': '18888888888', 'password': '123456789A!'
        }

        res = self.req.visit('post', login_url, data=payload)
        global token
        self.token = res['data']['token']
        token = self.token
        print("token打印为:" + token)
        self.assertEqual('0000', res['code'])
        return token

    def test_userinfo(self):
        userinfo_url = 'http://www.joysurvey.com:8089/survey/man/user/detail'
        global token
        headers_userinfo = {'token': token}

        payload = {
            'phone': '18888888888', 'password': '123456789A!'
        }
        resp_userinfo = self.req.visit('get', userinfo_url, data=payload, headers=headers_userinfo)
        self.assertEqual('0000', resp_userinfo['code'])

    # @pytest.mark.parametrize('a,b,c,d,e', [('zj01', '13075509378', '123456789A!', '123456789A!', '1'),
    #                                        ('zj02', '13075509379', '123456789A!', '123456789A!', '1')])
    # def test_useradd(self, a, b, c, d, e):
    #     useradd_url = 'http://www.joysurvey.com:8089/survey/man/user/add'
    #     headers_userinfo = {'token': "2fcbcb3369f2445590e6c27f432585ad"}
    #     payload = {
    #         'username': a,
    #         'phone': b,
    #         'password1': c,
    #         'password2': d,
    #         'status': e
    #     }
    #     resp_useradd = self.req.visit('post', userinfo_url, data=payload)
    #     print(resp_useradd)
    #     # self.assertEqual('0000', resp_userinfo['code'])


if __name__ == '__main__':
    unittest.main()
