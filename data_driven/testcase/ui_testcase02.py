from selenium import webdriver
import time
import xlrd  #判断元素可用不可用   unittest断言去判断 也可以异常处理判断try except else

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
#读取文件
data = xlrd.open_workbook("C:\\Users\A\pycharm1\data_driven\data\Testcase01.xls")
#读取第一个工作表
table = data.sheet_by_name('Sheet1')
#使用for循环输出所有数据
list=[]
for i in range (0,table.nrows):
    # 只读取其中一行
    list = table.row_values(i)
    break
print(list)
#判断是否有网址需要打开
if(str(list[0])!=''):
    driver.get(list[0])
#判断执行关键字
if(str(list[2])==u'输入'):
    if(list[1]=='id'):
        driver.find_element_by_id(list[3]).send_keys(list[4])
time.sleep(3)
if(str(list[6])==u'点击'):
    if(list[5]=='id'):
        driver.find_element_by_id(list[7]).click()
time.sleep(3)
driver.close()