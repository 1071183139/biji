from time import sleep
import fcntl
with open('text.txt', 'w') as fd:
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    fd.write('coco')
    sleep(10)
