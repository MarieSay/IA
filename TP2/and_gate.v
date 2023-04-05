module and_gate (e1, e2, s);
    input e1;
    input e2;
    output s;


    assign s = e1 & e2;

endmodule

module exercice2 (e1, e2, s);
    input e1;
    input e2;
    output s;

    assign s = e1 | e2; 

endmodule

module exercice3(e1, e2, e3, s);
    input e1;
    input e2;
    input e3; 
    output s;

    assign s = e1 & e2 & e3; // Exercice 3

endmodule

module Add1B(e1, e2, r, s);
    input e1;
    input e2;
    output r;
    output s;

    assign r = e1 & e2; 
    assign s = e1 ^ e2;

endmodule

module adder8bit(A, B, Cin, Sum, Cout);

input [31:0] A, B;
input Cin;
output [31:0] Sum;
output Cout;

wire [32:0] temp_sum;
wire carry;

assign temp_sum = A + B + Cin;
assign Sum = temp_sum[31:0];
assign Cout = temp_sum[32];

endmodule

module mult8bit(A, B, P);

input [15:0] A, B;
output reg [31:0] P;

integer i;

always @(*) begin
  P = 0;
  for (i = 0; i < 16; i = i + 1) begin
    if (B[i] == 1) begin
      P = P + (A << i);
    end
  end
end

endmodule

module Regression(f0, c1, c0, Cin, y);

input [15:0] f0;
input [15:0] c1;
input [31:0] c0;
input Cin;
output [31:0] y;

wire [31:0] r;
wire [31:0] rt;
wire Cout;

mult8bit mod1(f0, c1, r);
adder8bit mod2(c0, r, Cin, rt, Cout);

assign y = rt;

endmodule

module Regression_nV(c0, c1, c2, c3, f0, f1, f2, Cin, y);

input [31:0] c0;
input [15:0] f0;
input [15:0] c1;
input [15:0] f1;
input [15:0] c2;
input [15:0] f2;
input [15:0] c3;
input Cin;
output [31:0] y;


wire [31:0] r_mul0;
wire [31:0] r_add0;
wire [31:0] r_mul1;
wire [31:0] r_add1;
wire [31:0] r_mul2;
wire [31:0] r_add2;
wire Cout0;
wire Cout1;
wire Cout2;
//wire Cout3;

mult8bit mod1(f0, c1, r_mul0);
adder8bit mod2(c0, r_mul0, Cin, r_add0, Cout0);
mult8bit mod3(f1, c2, r_mul1);
adder8bit mod4(r_add0, r_mul1, Cout0, r_add1, Cout1);
mult8bit mod5(f2, c3, r_mul2);
adder8bit mod6(r_add1, r_mul2, Cout1, r_add2, Cout2);


assign y = r_add2;

endmodule