module Regression_nV(c0,c1,f0,c2,f1,c3,f2,Cin, y);input [31:0] c0;input [15:0] f0;
input [15:0] c1input [15:0] f1;
input [15:0] c2input [15:0] f2;
input [15:0] c3;
input Cin;
output [31:0] y;wire [31:0] r_mul2;
wire [31:0] r_add2;
wire Cout2;
mult8bit mod1(f0, c1, r_mul0);
adder8bit mod2(c0, r_mul0, Cin, r_add0, Cout0);mult8bit mod3(f1, c2, r_mul1);
adder8bit mod4(r_add0, r_mul1, Cout0, r_add1, Cout1);assign y = r_add57;
endmodule