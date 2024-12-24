"""
    Implementation; Computational Language
"""
import sys
# fin = sys.stdin.read().split('\n')
fin = """1
(-2)+3
(1-(2+3))
(1-2+3)
(1-(+(2-3)))
""".split('\n')

class Parser:
    def parse(self, string):
        self.buffer = ['\0' for _ in range(200)]
        self.idx = 0
        
        for i in range(len(string)):
            self.buffer[i] = string[i]

        return self.parse_expr()

    def parse_expr(self):
        """
        <expr> := <term> ( ('+'|'-') <term> )*
        """
        result = self.parse_term()
        chr = self.buffer[self.idx]

        while chr == '+' or chr == '-':
            if chr == '+':
                self.idx += 1
                result += self.parse_term()
            elif chr == '-':
                self.idx += 1
                result -= self.parse_term()
            chr = self.buffer[self.idx]

        return result

    def parse_term(self):
        """
        <term> ::= '(' <expr> ')'
                 | '(' ('+' | '-') <term> ')'
                 | <literal>
        """
        result = None
        chr = self.buffer[self.idx]

        if chr == '(':
            nxt = self.buffer[self.idx+1]

            if nxt == '+':
                self.idx += 1
                result = self.parse_unary_op()
            elif nxt == '-':
                self.idx += 1
                result = self.parse_unary_op()
            else:
                self.idx += 1
                result = self.parse_expr()

            if self.buffer[self.idx] == ')':
                self.idx += 1
        elif '0' <= chr <= '9':
            result = self.parse_literal()

        return result

    def parse_unary_op(self):
        """
        <unary_op> := '+' <term>
                    | '-' <term>
        """
        result = None

        chr = self.buffer[self.idx]

        if chr == '+':
            self.idx += 1
            result = self.parse_term()
        elif chr == '-':
            self.idx += 1
            result = -self.parse_term()

        return result

    def parse_literal(self):
        result = int(self.buffer[self.idx])
        self.idx += 1
        return result

prsr = Parser()

N, seq = len(fin), []
for i in range(N):
    seq.append(fin[i])

for i in range(N):
    if seq[i] == '': continue
    print(prsr.parse(seq[i]))