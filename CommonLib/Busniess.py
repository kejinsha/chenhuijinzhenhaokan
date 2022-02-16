# 导入已经封装好selenium的CommonShare类
from CommonLib.Commonlib import Commonshare

# 继承CommonShare，继承之后Commonshare中的方法都能使用
class Login(Commonshare):#子类  子继承父，所以可以用父的方法
    def login_yhd(self, user, pwd):
        self.open_url('http://www.yhd.com')
        # 点击登陆
        self.click('class', 'hd_login_link')
        # 输入账号
        self.input_data('id', 'un', user)
        # 输入密码
        self.input_data('id', 'pwd', pwd)
        # 点击登陆
        self.click('id', 'login_button')

if __name__ == '__main__':
    login = Login()
    login.login_yhd('xxxxxxx','xxxxxx')