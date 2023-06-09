`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg [15:0] a;
	reg [15:0] b;
	//reg retenue_prec;
	// Outputs
	//wire retenue;
	wire [31:0] result;
	// Instantiate the Unit Under Test (UUT)
	mult8bit uut (
		a, 
		b, 
		result
	);

 
	initial begin
	$dumpfile("test_Mul8B.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		a = 16'b0000000000000000;
		b = 16'b0000000000000000;
 
	#20 a = 16'd01;
	#20 b = 16'd02;
	#20 b = 16'd65535;
	#20 a = 16'd255;		  
 
	end  
 
		initial begin
		 $monitor("t=%3d x=%d, y=%d, result=%d \n",$time,a,b,result);
		 end
 
endmodule
 
