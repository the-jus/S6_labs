ASSUME CS: CODE, DS: DATA

DATA SEGMENT
ARR DW 0999H, 0101H, 0364H, 0FFEH
LEN DW 0004H
LAR DW 1 DUP(?)
SML DW 1 DUP(?)
DATA ENDS

CODE SEGMENT
START:  MOV AX, DATA
        MOV DS, AX

        MOV CX, LEN
        MOV AX, [SI]
        MOV BX, AX
        MOV DX, AX
        LEA SI, ARR

        LABEL1: MOV AX, [SI]
                CMP AX, BX
                JC SMALL
                MOV BX, AX

               SMALL:  CMP AX, DX
                       JNC LARGE
                       MOV DX, AX
               LARGE:  INC SI
                       INC SI
                       DEC CX
                       JNZ LABEL1

        MOV LAR, BX
        MOV SML, DX

        MOV AH, 4CH
        INT 21H
CODE ENDS
        END START
                
                


