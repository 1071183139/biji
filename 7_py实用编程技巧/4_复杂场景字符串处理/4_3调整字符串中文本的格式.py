import re

log = "2016-05-21 10:39:26 statys unpacked python3-pip:all " \
      "2016-05-23 10:49:26 status half-configured python3"

res = re.sub('(?P<d>\d{4})-(?P<m>\d{2})-(?P<y>\d{2})', r'\g<m>/\g<d>/\g<y>', log)
print(res)