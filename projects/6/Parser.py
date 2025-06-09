A_INSTRUCTION = 0
C_INSTRUCTION = 1
L_INSTRUCTION = 2

class Parser:
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            asm_file = file.read()
            self.assembly_program = asm_file.splitlines()
        # 次に処理する、現在の命令のindex
        self.current_instruction_index = 0
        # 現在の命令
        self.current_instruction: str = None 


    # 次の命令が存在するか否か
    def hasMoreLines(self):
        return self.current_instruction_index < len(self.assembly_program)


    # 次に処理する、現在の命令を選択
    def advance(self):
        def is_blank_or_comment(instruction: str):
            # 文字列の両端の空白を取り除く
            stripped_s = instruction.strip()

            # stripped_s が空文字列（つまり元の文字列が空白のみ）の場合
            if not stripped_s:
                return True
            
            # stripped_s が "//" で始まる場合
            if stripped_s.startswith('//'):
                return True
            
            # どちらでもない場合
            return False
        
        if (self.hasMoreLines()):
            self.current_instruction = self.assembly_program[self.current_instruction_index].strip()
            while is_blank_or_comment(self.current_instruction):
                self.current_instruction_index += 1
                if (not(self.hasMoreLines())):
                    self.current_instruction_index = None
                self.current_instruction = self.assembly_program[self.current_instruction_index].strip()
            self.current_instruction_index += 1


    def instructionType(self):
        if (self.current_instruction.startswith("@")):
            return A_INSTRUCTION
        elif (self.current_instruction.startswith("(")):
            return L_INSTRUCTION
        else: return C_INSTRUCTION

    
    def symbol(self):
        if (self.instructionType() == A_INSTRUCTION):
            return self.current_instruction.strip("@")
        elif (self.instructionType() == L_INSTRUCTION):
            return self.current_instruction.strip("(").strip(")")
        
    
    def dest(self):
        if (self.instructionType() == C_INSTRUCTION):
            if "=" in self.current_instruction:
                return self.current_instruction.split('=')[0]
            else:
                return ""


    def comp(self):
        if (self.instructionType() == C_INSTRUCTION):
            # ";jump"部分が存在する場合、その部分を取り除く
            if ";" in self.current_instruction:
                instruction_without_jump = self.current_instruction.split(';')[0]
            else: instruction_without_jump = self.current_instruction

            # "dest="部分が存在する場合、その部分を取り除く
            if "=" in instruction_without_jump:
                comp = instruction_without_jump.split('=')[1]
            else: comp = instruction_without_jump

            return comp
        
    
    def jump(self):
        if (self.instructionType() == C_INSTRUCTION):
            if ";" in self.current_instruction:
                return self.current_instruction.split(';')[1]
            else:
                return ""
            