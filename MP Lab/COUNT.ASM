ASSUME CS:CODE, DS:DATA

DATA SEGMENT
STR DB "(&tHEjuST%}"
LEN DW $-STR
UPP DB 1 DUP(?)
LW DB 1 DUP(?)
UPPMSG DB 0DH, 0AH, "Uppercase letters:","$"
LWMSG DB 0DH, 0AH, "Lowercase letters:","$"
DATA ENDS

CODE SEGMENT
START:  MOV AX, DATA
        MOV DS, AX
        MOV DX, 0000H
        MOV CX, LEN

        LEA SI, STR

       LOWER: MOV AL, [SI]
              CMP AL, "a"
              JC UPPER
              CMP AL, "z"
              JG LAST
              INC DL

        UPPER: CMP AL, "A"
               JC LAST
               CMP AL, "Z"
               JG LAST
               INC DH
        
        LAST: INC SI
              LOOP LOWER
              MOV UPP, DH
              MOV LW, DL

              MOV DX, OFFSET UPPMSG
              MOV AH, 09H
              INT 21H
              MOV DL, UPP
              MOV AH, 02H
              MOV BL, 30H
              ADD BL, DL
              MOV DL, BL
              INT 21H

              MOV DX, OFFSET LWMSG
              MOV AH, 09H
              INT 21H
              MOV DL, LW
              MOV AH, 02H
              MOV BL, 30H
              ADD BL, DL
              MOV DL, BL
              INT 21H

              MOV AH, 4CH
              INT 21H

CODE ENDS
        END START







