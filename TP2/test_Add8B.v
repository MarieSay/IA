`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg [31:0] a;
	reg [31:0] b;
	reg retenue_prec;
	// Outputs
	wire retenue;
	wire [31:0] result;
	// Instantiate the Unit Under Test (UUT)
	adder8bit uut (
		a, 
		b, 
		retenue_prec,
		result,
		retenue
	);

 
	initial begin
	$dumpfile("test_Add8B.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		a = 32'b0000000000000000;
		b = 32'b0000000000000000;
		retenue_prec = 0;
 
	#20 a = 32'd01;
	#20 b = 32'd02;
	#20 b = 32'd65535;
	#20 a = 32'd255;	  
 
	end  
 
		initial begin
		 $monitor("t=%3d x=%d,y=%d, retenue=%d, result=%d \n",$time,a,b,retenue,result);
		 end
 
endmodule
 
