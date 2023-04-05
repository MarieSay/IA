`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg [15:0] f0;
	reg [15:0] c1;
	reg [31:0] c0;
	reg Cin;
	//reg retenue_prec;
	// Outputs
	//wire retenue;
	reg [31:0] inter;
	wire [31:0] y;
	// Instantiate the Unit Under Test (UUT)
	
	Regression uut (
		f0, c1, c0, Cin, y
	);
	

 
	initial begin
	$dumpfile("test_Regression.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		f0 = 16'b0000000000000000;
		c0 = 31'b0000000000000000;
		c1 = 16'b0000000000000000;
		Cin = 0;
 
	#20 f0 = 16'd5000;
	#20 c0 = 31'd10000;
	#20 c1 = 16'd100;
	end  
 
		initial begin
		 $monitor("t=%3d c0=%d, f0=%d, c1=%d, result=%d \n",$time,c0,f0,c1,y);
		 end
 
endmodule
 
