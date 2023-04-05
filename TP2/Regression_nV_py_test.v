
`timescale 1ns / 1ps
module stimulus;
    // Inputs
    reg [31:0] c0;
    
	reg [15:0] c1;
	reg [15:0] f0;
	
	reg [15:0] c2;
	reg [15:0] f1;
	
	reg [15:0] c3;
	reg [15:0] f2;
	
    reg Cin;
    wire[31:0] y;
    Regression_nV_py uut(
        c0,
        c1,
        f0,
        c2,
        f1,
        c3,
        f2,
       Cin, 
       y
    );

    initial begin
    $dumpfile("test_Transpiler_py.vcd");
    $dumpvars(0, stimulus);
    // Initialize Inputs
    c0 = 31
    'b0000000000000000;
    f0 = 16'b0000000000000000;
    c1 = 16'b0000000000000000;
    f1 = 16'b0000000000000000;
    c2 = 16'b0000000000000000;
    f2 = 16'b0000000000000000;
    c3 = 16'b0000000000000000;
    Cin = 0;
#20 c0 = 2;
    c1=16'd3;
	f0 = 16'd1;
    c2=16'd4;
	f1 = 16'd1;
    c3=16'd5;
	f2 = 16'd1;
	end

        initial begin
        $monitor("c0=%d,f0=%d, c1=%df1=%d, c2=%df2=%d, c3=%dresult=%d", c0, c1, f0, c2, f1, c3, f2, y);
    end

endmodule