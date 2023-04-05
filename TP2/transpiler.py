import joblib
import sklearn
#from ctypes import CDLL
import numpy as np


model_lin = joblib.load('regression_lineaire.joblib')



def get_coef_lin():
    temp = [coef for coef in model_lin.coef_]
    return temp


def generate_veg_function_RegLin(tab, deb):

    fct = f"""
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
    """
    nom = "module Regression_nV_py(c0,"
    for i in range (len(tab)):
        print(i)
        nom += f"c{(str(int(i)+1))},f{i},"
    nom += "Cin, y);"

    input = f"""
input [31:0] c0;"""
    for j in range(len(tab)):
        input += f"""
input [15:0] f{str(j)} ;
input [15:0] c{str(j+1)};
        """
    input += f"""
input Cin;
output [31:0] y;
    """
    wire = ""
    for k in range (len(tab)):
        wire += f"""
wire [31:0] r_mul{str(k)};
wire [31:0] r_add{str(k)};
wire Cout{str(k)};
        """


    op = f"""
mult8bit mod1(f0, c1, r_mul0);
adder8bit mod2(c0, r_mul0, Cin, r_add0, Cout0);"""
    compteur = 3

    if ((len(tab)) >= 2):
        for h in range (len(tab)-1):
            op += f"""
mult8bit mod{compteur}(f{str(h+1)}, c{str(h+2)}, r_mul{str(h+1)});
adder8bit mod{str(compteur+1)}(r_add{str(h)}, r_mul{str(h+1)}, Cout{str(h)}, r_add{str(h+1)}, Cout{str(h+1)});"""
            compteur += 2

    algo = fct + nom + input + wire + op + f"""
assign y = r_add{str(len(tab)-1)};

endmodule"""

    return algo

def generate_veg_function_RegLin_test(tab, deb, f):
    algo = f"""
`timescale 1ns / 1ps
module stimulus;
    // Inputs
    reg [31:0] c0;
    """
    for i in range (len(tab)):
        algo += f"""
	reg [15:0] c{i+1};
	reg [15:0] f{i};
	"""
    algo += f"""
    reg Cin;
    wire[31:0] y;
    Regression_nV_py uut(
        c0,"""
    for j in range (len(tab)):
        algo += f"""
        c{j+1},
        f{j},"""
    algo += f"""
       Cin, 
       y
    );

    initial begin
    $dumpfile("test_Transpiler_py.vcd");
    $dumpvars(0, stimulus);
    // Initialize Inputs
    c0 = 31
    'b0000000000000000;"""
    for k in range(len(tab)):
        algo += f"""
    f{k} = 16'b0000000000000000;
    c{k+1} = 16'b0000000000000000;"""

    algo += f"""
    Cin = 0;
#20 c0 = {deb};"""
    for h in range(len(tab)):
        algo += f"""
    c{h+1}=16'd{int(tab[h])};
	f{h} = 16'd{f[h]};"""
    algo += f"""
	end

        initial begin
        $monitor("c0=%d,"""
    for n in range(len(tab)):
        algo += f"""f{n}=%d, c{n+1}=%d"""
    algo += f"""result=%d", c0, """
    for m in range(len(tab)):
        algo += f"""c{m+1}, f{m}, """
    algo += f"""y);
    end

endmodule"""



    return algo




c = 1
while(c != 0) :
    print("1. Executer avec les prix des maisons\n2. Executer avec des features choisies\n0. Pour quitter\n")
    a = input()
    c = int(a)
    if (c == 1):
        tab = model_lin.coef_
        deb = model_lin.intercept_
        print("attention, ce programme donne des resultats errones car une feature depasse le nombre de bit requis")
        f_lin = generate_veg_function_RegLin(tab,deb)
        print("Entrez les caractéristiques souhaitées (Pour ce modèle, trois caratéristiques sont demandées)\n")
        print("Size : \n")
        f0 = input()

        print("Nb_room : \n")
        f1 = input()

        print("Garden : \n")
        f2 = input()
        f = np.array([int(f0), int(f1), int(f2)])
        print("Vous souhaitez donc exécutez ce programme avec les features suivantes :", tab)

        test_lin = generate_veg_function_RegLin_test(tab, deb, f)

        fichier = open("Regression_nV_py.v", "w")
        fichier.write(f_lin)
        fichier.close()
        fichier = open("Regression_nV_py_test.v", "w")
        fichier.write(test_lin)
        fichier.close()
        print("rentrez la commande suivante : \niverilog Regression_nV_py.v Regression_nV_py_test.v \nvvp a.out\n")

    if (c == 2):

        print("Combien souhaitez vous rentrer de features sans le intercept ?\n")
        nb = input()
        print("Entrez le intercept : \n")
        inter = input()
        deb = int(inter)
        tab=[]
        for i in range (int(nb)):
	    print("Entrez la valeur suivante : \n")
            a = input()
            tab.append(a)
        print("Vous souhaitez donc exécutez ce programme avec les features suivantes :", tab)
        print("Entrez les caractéristiques souhaitées \n")
        f=[]
        for i in range(int(nb)):
            a = input()
            f.append(a)
        print("Vous souhaitez donc exécutez ce programme avec les features suivantes :", tab)
        f_lin = generate_veg_function_RegLin(tab,deb)
        test_lin = generate_veg_function_RegLin_test(tab, deb, f)

        fichier = open("Regression_nV_py.v", "w")
        fichier.write(f_lin)
        fichier.close()
        fichier = open("Regression_nV_py_test.v", "w")
        fichier.write(test_lin)
        fichier.close()
        print("rentrez la commande suivante : \niverilog Regression_nV_py.v Regression_nV_py_test.v \nvvp a.out\n")



    elif (c == 0) :
        print("Vous allez nous quitter... A bientot")
    else:
        print("Votre saisie est incorrecte, merci d'entree une des saisies proposées\n")
        break






