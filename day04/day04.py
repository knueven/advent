import hashlib, itertools, sys

key='yzbqklnj'

for target in ['0'*5, '0'*6]:
    for count in itertools.count():
        md = hashlib.md5()
        md.update(key + str(count))
        hd = md.hexdigest()
        if hd.startswith(target):
            print('Count {0}, hash {1}'.format(count, hd))
            break
