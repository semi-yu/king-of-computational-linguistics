"""
    implementation; Computational languistics
"""
import sys
# fin = sys.stdin.read().split('\n')
fin = """1001""".split('\n')
signal = fin[0]

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
            
            # if is_accepted(signal, idx): return True
            
            while signal[idx] == '1':
                idx += 1
                if idx >= len(signal): break
                if is_accepted(signal, idx): return True

    return True

print('SUBMARINE' if is_accepted(signal) else 'NOISE')