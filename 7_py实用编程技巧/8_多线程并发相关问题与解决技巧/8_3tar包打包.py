import tarfile
import os


def FunTarFile(tfname):
    tf = tarfile.open(tfname, 'w:gz')  # open打开一个tar包，‘w’打开模式为写 ‘:gz’压缩模式gzip

    for fname in os.listdir('.'):  # 遍历当前目录的文件
        if fname.endswith('.docx'):
            tf.add(fname)  # 将此文件加入tar包
            os.remove(fname)  # 移除此文件

    tf.close()
    print(tf.members)  # 打印tar包成员信息
    if not tf.members:  # 判断tar包是否为空
        os.remove(tfname)  # 如果tar包为空，删除此tar包


FunTarFile('DocxTar.tgz')