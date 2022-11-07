.include "/home/aluru-ajay99/m328Pdef.inc"
ldi r30, 0b00100000 ;identifying output pin 13
out DDRB,r30
ldi r16, 0b11110011  ;identifying input pins 2,3
out DDRD,r16          ;declaring pins as input
ldi r16,0b11111011   ;giving input
out PortD,r16
ldi r17,0b00000001
ldi r18,0b00000001


AND r17,r16          ;r17=U
LSR  r16
AND r18,r16           ;r18=V
           

ldi r21,0b00000001 
eor r21,r17           ;r21=U'

ldi r22,0b00000001
eor r22,r18           ;r22=V'


mov r5,r21            ;r5=U'
OR r5,r18             ;r5= U'+V  (X)      


mov r0,r21            ;r0=U'
AND r0,r22            ;r0=U'V' 
mov r1,r21            ;r1=U'
AND r1,r18            ;r1=U'V
mov r6,r17            ;r5=U
AND r6,r18		    ;r5=uv
OR r6,r0              ;r5= UV+U'V'          
OR r6,r1              ;r5=U'V' + U'.V+U.V (Y)

lbl:
ldi r29,0b00000001


mov r30,r29            ;r30=0000000Y
LSL r30               ;r30=000000Y0
LSL r30               ;r30=00000Y00
LSL r30               ;r30=0000Y000
LSL r30               ;r30=000Y0000
LSL r30               ;r30=00Y00000
out PortB,r30

Start:
rjmp Start
