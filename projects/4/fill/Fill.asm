// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.


(INF)
@i
M=0
@KBD
D=M
@BLACKENS
D;JNE
@CLEAR
D;JEQ
@INF
0;JMP


(BLACKENS)
@8192
D=A
@i
D=D-M
@INF
D;JEQ

@SCREEN
D=A
@i
A=D+M
M=-1
@i
M=M+1
@BLACKENS
0;JMP


(CLEAR)
@8192
D=A
@i
D=D-M
@INF
D;JEQ

@SCREEN
D=A
@i
A=D+M
M=0
@i
M=M+1
@CLEAR
0;JMP