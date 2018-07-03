#coding=utf-8
import unittest

def div(a,b):
	return a/b

#新建测试用例必须先定义一个类，而且这个类继承unittest.TestCase类
class TestDiv(unittest.TestCase):
	#在类中以test开头的才是测试用例
	#不以test开头的叫钩子方法 如setUp  tearDown 

	def setUp(self):
		print("在每个测试用例执行前执行，用来准备测试数据")

	def tearDown(self):
		print("在每个测试用例执行后执行，测试结束后需要执行的工作，如关闭浏览器")


	def test_1_div_1(self):
		self.assertEqual(div(1,1),1/1)

	def test_4_div_4(self):
		self.assertEqual(div(3,4),3/4)

	def test_3_div_0(self):
		self.assertRaises(ZeroDivisionError,div,3,0)

	
#使用如下的语句才能执行测试用例
if __name__ == '__main__':
	unittest.main()