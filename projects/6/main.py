from Parser import Parser
from Code import Code 
from SymbolTable import SymbolTable
from Assembler import Assembler



# assembler = Assembler("/Users/hiroki/Desktop/app/myapp/nand2tetris/projects/6/rect/Rect.asm")
# assembler.assemble("/Users/hiroki/Desktop/app/myapp/nand2tetris/projects/6/rect/Rect.hack")

assembler = Assembler("/Users/hiroki/Desktop/app/myapp/nand2tetris/projects/6/pong/Pong.asm")
assembler.assemble("/Users/hiroki/Desktop/app/myapp/nand2tetris/projects/6/pong/Pong.hack")
print(assembler.binary_code)