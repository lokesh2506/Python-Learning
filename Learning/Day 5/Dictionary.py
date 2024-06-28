'''
1.Insertion order not preserved
2.Duplicate keys or not allowed
3.Hetrogeneous datatypes are allowed
4.mutable
'''
import math

d={100:"loki",101:"kumar",102:"adam",103:"john"}

print(d)

for i in d.keys():
    print(i)

for i in d.values():
    print(i)

for k,v in d.items():
    print(k," => ",v)

print(len(d))

print(d.get(100))

d.popitem()

print(d)

d[103]="john"
print(d)

