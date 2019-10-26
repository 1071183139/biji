#创建一个元素
from xml.etree.ElementTree import Element,ElementTree
e = Element("Data")   #创建一个元素，传入一个字符串 <Data>是head的名字
e.set('name','abc')   #设备这个元素的属性，get获取属性，set设置属性。属性为’name’值 是abc
from xml.etree.ElementTree import tostring #显示成为XML元素后转成了字符串
e.text = '123'
print(tostring(e))



#给一个元素添加子元素
from xml.etree.ElementTree import Element,ElementTree
e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
e2.append(e3)
from xml.etree.ElementTree import tostring #显示成为XML元素后转成了字符串
print(tostring(e2))



# 将一个已赋值的元素属性删除的方法
from xml.etree.ElementTree import Element,ElementTree
e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
e2.append(e3)
from xml.etree.ElementTree import tostring #显示成为XML元素后转成了字符串
print(tostring(e2))
e3.text = None # 删除 e3 中的内容
print(tostring(e2))



# 将XML格式的字符串写入文件中
from xml.etree.ElementTree import Element,ElementTree
e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
e2.append(e3)
e3.text = None # 删除 e3 中的内容
et = ElementTree(e2)
et.write('ha.xml')





