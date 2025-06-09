from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

A_INSTRUCTION = 0
C_INSTRUCTION = 1
L_INSTRUCTION = 2

class Assembler:
    def __init__(self, source_filepath):
        self.parser = Parser(source_filepath)
        self.code = Code()
        self.line_index = 0
        self.binary_code = ""
        self.symbol_table = SymbolTable()
        self.val_symbol_index = 16

    
    def first_pass(self):
        while self.parser.hasMoreLines():
            self.parser.advance()
            if (self.parser.instructionType() == A_INSTRUCTION or self.parser.instructionType() == C_INSTRUCTION):
                self.line_index += 1
            elif (self.parser.instructionType() == L_INSTRUCTION):
                self.symbol_table.addEntry(self.parser.symbol(), self.line_index)
        self.parser.current_instruction_index = 0
            


    
    def second_pass(self, target_filepath):
        while self.parser.hasMoreLines():
            self.parser.advance()
            binary_instruction  = ""
            print("now = ", self.parser.current_instruction_index)
            print("current = ", self.parser.current_instruction)
            if (self.parser.instructionType() == A_INSTRUCTION):
                # シンボルが数字の場合
                if (self.parser.symbol().isdigit()):
                    binary_instruction = format(int(self.parser.symbol()), '016b')
                else:
                    if (not(self.symbol_table.contains(self.parser.symbol())) and not(self.parser.symbol().isupper())):
                        self.symbol_table.addEntry(self.parser.symbol(), self.val_symbol_index)
                        self.val_symbol_index += 1
                    binary_instruction = format(self.symbol_table.getAddress(self.parser.symbol()), '016b')
            elif (self.parser.instructionType() == L_INSTRUCTION):
                continue
            elif (self.parser.instructionType() == C_INSTRUCTION):
                binary_instruction = "111" + self.code.comp(self.parser.comp()) + self.code.dest(self.parser.dest()) + self.code.jump(self.parser.jump())
            print("binary = ", binary_instruction)
            self.binary_code += binary_instruction + "\n"


    def assemble(self, target_filepath):
        self.first_pass()
        self.second_pass(target_filepath)
        print(self.symbol_table.symbol_table)
        # ファイルへの書き込み
        try:
            with open(target_filepath, 'w') as file:
                file.write(self.binary_code)
                print("success!")
        except IOError as e:
            print(f"ファイルの書き込み中にエラーが発生しました: {e}")
