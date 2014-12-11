#!/usr/bin/env python

spacing = .1  # m
lines = []
for c in range(-3,4):
    for r in range(25):
        lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
                     (c*spacing,0,(r - 12)*spacing))
print '[\n' + ',\n'.join(lines) + '\n]'
