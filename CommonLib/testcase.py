import unittest
# 从Business组件中导入我们定义的测试登录的类
from CommonLib.Busniess import Login

class Test(unittest.TestCase):
    def setUp(self):
        print ("开始进行测试")

    def tearDown(self):
        print('测试结束')

    # 正确登录的测试用例
    def test_001(self):
        login = Login()
        login.login_yhd('xxxxx','xxxxx')
        data = login.get_text('class','hd_login_name')
        self.assertEqual('hack_ai_buster',data)

    # 没有输账号密码直接点击登录的测试用例
    def test_002(self):
        login = Login()
        login.login_yhd('','')
        data = login.get_text('id','error_tips')
        self.assertEqual('请输入账号和密码',data)

    # 随意输入账号，不输入密码的测试用例
    def test_003(self):
        login = Login()
        login.login_yhd('hgvjchgc','')
        data = login.get_text('id','error_tips')
        self.assertEqual('请输入密码',data)

    # 用于演示出bug的测试用例
    def test_004(self):
        login = Login()
        login.login_yhd('hgvjchgc','')
        data = login.get_text('id','error_tips')
        # 我们故意写错预期结果，让这个断言抛出
        self.assertEqual('请输入密码itcast',data)

if __name__ == '__main__':
    unittest.main()