ASSUME DS:DATA, CS:CODE

DATA SEGMENT
INVAL   DB 1 DUP(?)
STR1 DB 10 DUP('$')
MS1   DB 0DH, 0AH, "PALINDROME","$"
MS2   DB 0DH, 0AH, "NOT PALINDROME $"
MS3   DB 0DH, 0AH, "ENTER STRING: $"

DATA ENDS

CODE SEGMENT
START:  MOV AX, DATA
        MOV DS, AX
        MOV DX, OFFSET MS3
        MOV AH, 9H
        INT 21H
        MOV SI,OFFSET STR1
INPUT:  MOV AH,1
        INT 21H
        CMP AL,13
        JE LABEL1
        MOV [SI], AL
        INC SI
        JMP INPUT
 LABEL1 :
    MOV DI,OFFSET STR1
    DEC SI
    LOOP2 :
     CMP SI, DI
     JL PALN
     MOV AX,[SI]
     MOV BX, [DI]
     CMP AL, BL
     JNE NPALN
    DEC SI
    INC DI
    JMP LOOP2
 PALN:LEA DX,MS1
    MOV AH, 09H
    INT 21H
    JMP FLABEL
NPALN:LEA DX,MS2
    MOV AH,09H
    INT 21H
FLABEL:MOV AH, 4CH
    INT 21H
CODE ENDS
        END START

  
