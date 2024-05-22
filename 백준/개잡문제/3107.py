ip = input()

ip_list = ip.split(':')

for idx, value in enumerate(ip_list):
    if value == '':
        ip_list.pop(idx)
        while len(ip_list) != 8:
            ip_list.insert(idx, '0000')

for idx, value in enumerate(ip_list):
    ip_list[idx] = value.zfill(4)

print(':'.join(ip_list))
