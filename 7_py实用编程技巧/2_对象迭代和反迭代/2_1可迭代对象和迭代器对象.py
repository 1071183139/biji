import requests
from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    '''实现一个迭代器对象WeatherIterator'''

    def __init__(self, cities):
        self.cities = cities
        # 记录迭代位置
        self.index = 0

    def getWeather(self, city):
        '''获取单个城市气温数据'''
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city, data['low'], data['high'])

    def __next__(self):
        '''__next__方法每次返回一个城市气温'''
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    '''实现一个可迭代对象WeatherIterable'''

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        '''__iter__方法返回一个迭代器对象'''
        return WeatherIterator(self.cities)


if __name__ == '__main__':
    for city in WeatherIterable(['北京', '上海', '广州', '深圳']):
        print(city)