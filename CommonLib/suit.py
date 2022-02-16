import unittest
from CommonLib.testcase import Test

class Suit(unittest.TestCase):
    def test_suit(self):
        # 定义要是用的测试用例列表
        case_list = ['test_002','test_003','test_004']
        # 创建测试套件
        mysuit = unittest.TestSuite()
        # 遍历测试用例列表
        for case in case_list:
            # 将测试用例添加到测试套件中
            mysuit.addTest(Test(case))
        # 运行Runner执行测试，verbosity=2指定为每个测试用例生成报告，run中传入要执行的测试套件
        unittest.TextTestRunner(verbosity=2).run(mysuit)


if __name__ == '__main__':
    unittest.main()