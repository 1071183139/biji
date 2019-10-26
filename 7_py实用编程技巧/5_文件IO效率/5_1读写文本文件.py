import struct


def find_subchunk(f, chunk_name):
    f.seek(12)  # 从头 跳过12个字节
    while True:
        name = f.read(4)  # 读取4个字节
        chunk_size, = struct.unpack('i', f.read(4))  # i 即int 解析4个字节     h 解析两个字节
        print(name)

        if name == chunk_name:
            return f.tell(), chunk_size  # f.tell当前文件的指针位置

        f.seek(chunk_size, 1)  # 1 表示当前    0 表示从头 为默认


f = open('demo.wav', 'rb')  # 二进制文件  带b

offset, size = find_subchunk(f, b'data')

import numpy as np

buf = np.zeros(size // 2, dtype=np.short)  # array([0,0,0,0,...0], dtype=int16)

f.readinto(buf)

buf //= 8  # 除8  获得整数结果   获取声音小的声音

f2 = open('out.wav', 'wb')
f.seek(0)
info = f.read(offset)
f2.write(info)

buf.tofile(f2)
f2.clode()