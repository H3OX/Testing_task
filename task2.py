TODO = """
Нужно вывести 5 айпи-адресов, которые встречаются чаще других.
"""
from collections import Counter

file = open('hits.txt', 'r')
contents = file.read().split('\t')
IPs = [contents[x] for x in range(len(contents)) if x%2 != 0]

common = Counter(IPs).most_common(5)
for x, y in common:
    print(x)