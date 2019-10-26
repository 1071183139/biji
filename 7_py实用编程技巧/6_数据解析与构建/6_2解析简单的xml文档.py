from xml.etree import ElementTree

# 从字符串中解析
ElementTree.fromstring('相应字符串')

# 从文件中解析
et = ElementTree.parse('demo.xml')

root = et.getroot()  # 获取根元素  data

root.tag  # 当前tag    data

c1 = list(root)[0]  # 获取子元素列表   c1为列表中第一个 country

c1.attrib  # {'name': "Liechtenstein"}   attrib获取属性字典
c1.get('name')  # Liechtenstein

year = list(c1)[1]
year.text  # 得到year标签里的 2008

year.tail  # '\n\t\t'  即  year标签与下一个标签 之间的 字符

c1.find('neighbor')  # 在子元素中 找到 第一个neighbor标签
c1.findall('neighbor')  # 在子元素中 找到 所有neighbor标签 得到 列表

list(root.iter('neighbor'))  # 找到所有neighbor
# root.iter()  没有传入参数  则返回所有 元素


list[root.iterfind('./*/*[@name]')]  # 使用xpath 表达式  查找

list(c1.itertext())  # 获取所有 text文本   包括  \n\t

# 过滤掉\n\t
' '.join(t for t in c1.itertext() if not t.isspace())