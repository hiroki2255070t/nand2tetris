from Parser import Parser
from Code import Code 
from Assembler import Assembler


assembler = Assembler("/Users/hiroki/Desktop/app/myapp/nand2tetris/projects/6/add/Add.asm")
assembler.assemble("/Users/hiroki/Desktop/app/myapp/nand2tetris/projects/6/add/Add.hack")
print(assembler.binary_code)