#!/usr/bin/env python3
'''
generate frequency tuning words for midi notes
'''
BITS_PER_SEC = 500000


s = """\
// frequency tuning words for all 128 midi notes
// generated by midi_ftws.py
static unsigned const midi_ftws[128] = {"""
for m in range(0, 128):
    f = 440 * 2**((m - 69) / 12)
    ftw = int(0x100000000 * f / BITS_PER_SEC / 2)
#     print(m, f, ftw)
    if (m % 4 == 0):
        s += '\n\t'
    s += '0x{:08x}, '.format(ftw)
s = s[:-1] + "\n};"
print(s)
