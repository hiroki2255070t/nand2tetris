from Parser import Parser
from Code import Code

A_INSTRUCTION = 0
C_INSTRUCTION = 1
L_INSTRUCTION = 2

class Assembler:
    def __init__(self, source_filepath):
        self.parser = Parser(source_filepath)
        self.code = Code()
        self.binary_code = ""

    
    def assemble(self, target_filepath):
        while self.parser.hasMoreLines():
            self.parser.advance()
            binary_instruction  = ""
            if (self.parser.instructionType() == A_INSTRUCTION or self.parser.instructionType() == L_INSTRUCTION):
                binary_instruction = format(int(self.parser.symbol()), '016b')
            elif (self.parser.instructionType() == C_INSTRUCTION):
                binary_instruction = "111" + self.code.comp(self.parser.comp()) + self.code.dest(self.parser.dest()) + self.code.jump(self.parser.jump())
            self.binary_code += binary_instruction + "\n"
        try:
            with open(target_filepath, 'w') as file:
                file.write(self.binary_code)
                print("success!")
        except IOError as e:
            print(f"ファイルの書き込み中にエラーが発生しました: {e}")

