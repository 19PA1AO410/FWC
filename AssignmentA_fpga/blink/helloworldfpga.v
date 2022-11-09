module boolean(

    input   U,
    input   V,
    
    output  A,
    output  B,
    );
   assign A=(!U|V);
   assign B=((!U&!V)|(!U&V)|(U&V));
    endmodule
