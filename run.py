import unittest
from xml.etree import ElementTree as ET
import HTMLTestReportCN
from BeautifulReport import BeautifulReport

if __name__ == '__main__':

    et = ET.parse('/Users/air/Documents/bill/config.xml')
    # print(len(et.findall('./cases/*')))       #  查询节点下测试用例的数量是否正确
    li = et.findall('./cases/*')
    suite = unittest.TestSuite()
    for i in li:
        # print(i.tag)
        # 如何动态引入包，可以选择spit切割，如下：
        class_name = i.tag.split('-')[0]
        # print(class_name)    #验证一下切割的对不对
        method_name = i.tag.split('-')[1]
        exec('import %s' % class_name)    # 导入包
        exec("suite.addTest(%s.%s('%s'))" % (class_name, class_name, method_name))
        # unittest.TextTestRunner().run(suite)

    result = BeautifulReport(suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='/Users/air/Documents/bill/测试报告')
    # HTMLTestReportCN.HTMLTestRunner(stream=open('./report.html', 'wb')).run(suite)

