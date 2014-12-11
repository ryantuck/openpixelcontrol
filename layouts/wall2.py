#!/usr/bin/env python

spacing = .1  # m
lines = []
for c in range(-3,4):
    for r in range(25):
        lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
                     (c*spacing,(r - 12)*spacing,0))
print '[\n' + ',\n'.join(lines) + '\n]'
