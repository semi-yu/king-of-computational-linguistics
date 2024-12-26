"""
    Implementation; Computational linguistics
"""
import sys
# fin = sys.stdin.read().split('\n')
fin = """3
10010111
011000100110001
0110001011001""".split('\n')

T = int(fin[0])
queries = []
for i in range(1,1+T):
    queries.append(fin[i])

def is_accepted(signal, init=0):
    idx = init

    while idx < len(signal):
        if signal[idx] == '0':
            idx += 1
            if idx >= len(signal): return False

            if signal[idx] == '1':
                idx += 1
                return is_accepted(signal, idx)
            else:
                return False
        elif signal[idx] == '1':
            idx += 1
            if idx >= len(signal): return False

            if signal[idx] == '1': return False

            idx += 1
            if idx >= len(signal): return False

            if signal[idx] == '0':
                idx += 1
                if idx >= len(signal): return False

                while signal[idx] == '0':
                    idx += 1
                    if idx >= len(signal): return False
            else:
                return False
            
            while signal[idx] == '1':
                idx += 1
                if idx >= len(signal): break
                if is_accepted(signal, idx): return True

    return True

for q in queries:
    print('YES' if is_accepted(q) else 'NO')