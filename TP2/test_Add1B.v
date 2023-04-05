`timescale 1ns / 1ps
module stimulus;
	// Inputs
	reg x;
	reg y;
	// Outputs
	wire retenue;
	wire result;
	// Instantiate the Unit Under Test (UUT)
	Add1B uut (
		x, 
		y, 
		retenue,
		result
	);

 
	initial begin
	$dumpfile("test_Add1B.vcd");
    $dumpvars(0,stimulus);
		// Initialize Inputs
		x = 0;
		y = 0;
 
	#20 x = 1;
	#20 y = 1;
	#20 y = 1;	
	#20 x = 0;	  
	#40 ;
 
	end  
 
		initial begin
		 $monitor("t=%3d x=%d,y=%d, retenue=%d, result=%d \n",$time,x,y,retenue,result);
		 end
 
endmodule
 
