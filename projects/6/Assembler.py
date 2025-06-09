from Parser import Parser
from Code import Code

A_INSTRUCTION = 0
C_INSTRUCTION = 1
L_INSTRUCTION = 2

class Assembler:
    def __init__(self, filename):
        self.parser = Parser(filename)
        self.code = Code()
        self.binary_code = ""

    
    def assemble(self):
        while self.parser.hasMoreLines():
            self.parser.advance()
            binary_instruction  = ""
            if (self.parser.instructionType() == A_INSTRUCTION or self.parser.instructionType() == L_INSTRUCTION):
                binary_instruction = format(int(self.parser.symbol()), '016b')
            elif (self.parser.instructionType() == C_INSTRUCTION):
                binary_instruction = "111" + self.code.comp(self.parser.comp()) + self.code.dest(self.parser.dest()) + self.code.jump(self.parser.jump())
            self.binary_code += binary_instruction + "\n"

