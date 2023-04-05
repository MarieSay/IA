`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg [31:0] c0;
	reg [15:0] c1;
	reg [15:0] c2;
	reg [15:0] c3;
	reg [15:0] f0;
	reg [15:0] f1;
	reg [15:0] f2;
	reg Cin;
	//reg retenue_prec;
	// Outputs
	//wire retenue;
	reg [31:0] inter;
	wire [31:0] y;
	// Instantiate the Unit Under Test (UUT)
	
	Regression_nV uut (
		c0, 
		c1, 
		c2, 
		c3, 
		f0, 
		f1, 
		f2, 
		Cin, 
		y
	);
	

 
	initial begin
	$dumpfile("test_Transpiler.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		c0 = 32'b0000000000000000;
		c1 = 16'b0000000000000000;
		c2 = 16'b0000000000000000;
		c3 = 16'b0000000000000000;
		f0 = 16'b0000000000000000;
		f1 = 16'b0000000000000000;
		f2 = 16'b0000000000000000;
		Cin = 0;
 
	#20 c0 = 32'd50000;
	#20 f0 = 16'd1000;
	#20 f1 = 16'd30000;
		c1 = 16'd200;
		f2 = 16'd600;
		c2 = 16'd700;
		c3 = 16'd65;
	end  
 
		initial begin
		 $monitor("t=%3d c0 = %d, c1 = %d, c2 = %d, c3 = %d, f0 = %d, f1 = %d, f2 = %d, result=%d \n",$time,c0, c1, c2, c3, f0, f1, f2, y);
		 end
 
endmodule
 
