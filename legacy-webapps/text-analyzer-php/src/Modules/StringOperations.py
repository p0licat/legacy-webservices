#/!usr/env/bin python
def WhitelistStripping(i):
    e = "abcdefghijklmnopqrstuvwxyz-1234567890'"
    c = ""
    for k in range(len(i)):
        if i[k].lower() in e:
            c += i[k].lower()
    return c

