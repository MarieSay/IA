`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg x;
	reg y;
	reg a;
	// Outputs
	wire z;
	// Instantiate the Unit Under Test (UUT)
	exercice3 uut (
		x, 
		y, 
		a,
		z
	);

 
	initial begin
	$dumpfile("test_exercice3.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		x = 0;
		y = 0;
		a = 0;
 
	#20 x = 1;
	#20 y = 1;
	#20 a = 1;
	#20 y = 0;	
	#20 x = 1;	  
	#20 a = 1;
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d x=%d,y=%d,a=%d,z=%d \n",$time,x,y,a,z, );
		 end
 
endmodule
 
 
