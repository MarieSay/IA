import joblib
import numpy
import numpy as np
import sklearn
#from ctypes import CDLL


model_lin = joblib.load('regression_lineaire.joblib')
model_log = joblib.load('regression_logistic.joblib')
tree = joblib.load('regression_tree.joblib')


def get_coef_lin():
    tab = "{"
    temp = [coef for coef in model_lin.coef_]
    for i in range (len(temp)-1) :
        tab = tab + str(temp[i]) + ','
    tab += str(temp[(len(temp) - 1)]) +"}"
    return tab

def get_coef_log():
    tab = "{"
    temp = [coef for coef in model_log.coef_[0]]
    for i in range (len(temp)-1) :
        tab = tab + str(temp[i]) + ','
    tab += str(temp[(len(temp) - 1)]) +"}"
    return tab



def get_features():
    tab = "{"
    temp = [coef for coef in tree.tree_.feature]
    for i in range (len(temp)-1) :
        tab = tab + str(temp[i]) + ','
    tab += str(temp[(len(temp) - 1)]) +"}"
    return tab

def get_threshold():
    tab = "{"
    temp = [coef for coef in tree.tree_.threshold]
    for i in range (len(temp)-1) :
        tab = tab + str(temp[i]) + ','
    tab += str(temp[(len(temp) - 1)]) +"}"
    return tab

def get_children_left():
    tab = "{"
    temp = [coef for coef in tree.tree_.children_left]
    for i in range (len(temp)-1) :
        tab = tab + str(temp[i]) + ','
    tab += str(temp[(len(temp) - 1)]) +"}"
    return tab

def get_children_right():
    tab = "{"
    temp = [coef for coef in tree.tree_.children_right]
    for i in range (len(temp)-1) :
        tab = tab + str(temp[i]) + ','
    tab += str(temp[(len(temp) - 1)]) +"}"
    return tab

def get_values():
    tab = "{"
    temp = [coef for coef in tree.tree_.value]

    for i in range (len(temp)-1) :
        tab = tab + str(temp[i][0][0]) + ','
    tab += str(temp[(len(temp) - 1)][0][0]) +"}"
    return tab



def generate_c_function_RegLin(model, dem):
    tab = get_coef_lin()
    deb = model_lin.intercept_
    coef = f"""
    #include <stdio.h>
    float linear_regression_prediction(float* features, int n_parameters)
    {{
        float result;
        float tab[] = {tab};
        result = {deb};
    for(int i=0;i<n_parameters;i++)
    {{
        result = result + tab[i] * features[i];
    }}
    return result;
    }}
    int main() 
    {{
        float a[]={{{dem[0]},{dem[1]},{dem[2]}}};
        float result = linear_regression_prediction(a, 3);
        printf("result = %f", result);
        return 0;
    }}
    """
    return coef


def generate_c_function_LogReg(model, dem):
    tab = get_coef_log()
    deb = model_log.intercept_[0]
    print(deb)
    coef = f"""
    #include <stdio.h>
    float exp_approx(float x, int n_term)
    {{
      float exp = 1;
      float f = 1;
      float p = 1;
      for(int i=1;i<=n_term;i++)
      {{
          f *= i;
          p *= x;
          exp += (p/f);
      }}
      printf("exp = %f",exp); 

    return exp;
    }}

    float sigmoid(float x)
    {{
        float sig = (1 / (1+(exp_approx(-x, 33))));
        return sig;
    }}

    int logistic_regression_prediction(float* features, int n_parameters)
    {{
    float result;
    float tab[] = {tab};
    result = {deb};
    float sig;
    int res;
    for(int i=0;i<n_parameters;i++)
    {{
        result += tab[i] * features[i];
    }}
    sig = sigmoid((result));
    printf("sig = %f",sig); 
    if(sig>0.5)
    {{
        res = 1;
    }}
    else
    {{
        res = 0;
    }}
    return res;
    }}

    int main() 
    {{
        float a[]={{{dem[0]},{dem[1]},{dem[2]},{dem[3]}}};
        int result = logistic_regression_prediction(a, 4);
        printf("result = %d", result);
        return 0;
    }}
    """
    print(coef)
    return coef

def generate_c_function_Arbre(tree, dem):
    features = get_features()
    threshold = get_threshold()
    children_left = get_children_left()
    children_right = get_children_right()
    values = get_values()

    value = f"""
        #include <stdio.h>
        float arbre(float* feat, int n_parameters)
        {{
            int features[] = {features};
            float threshold[] = {threshold};
            int children_left[] = {children_left};
            int children_right[] = {children_right};
            float values[] = {values};
            int new_node_a = 0;
            int new_node = 0;
            int a;
        while(features[new_node]>=0)
        {{
            new_node = new_node_a;
            a = features[new_node];
            if(feat[a] <= threshold[new_node])
            {{
                new_node_a = children_left[new_node];
            }}
            else
            {{
                new_node_a = children_right[new_node];
            }}
        }}
        printf("node = %d",new_node);
        return (values[new_node]);
        }}
        int main() 
        {{
            float a[]={{{dem[0]},{dem[1]},{dem[2]}}};
            float result = arbre(a, 3);
            printf("result = %f", result);
            return 0;
        }}
        """
    return value


c = 1
while(c != 0) :
    print("Quelles données voulez-vous étudier ?\n1. Le prix des maisons\n2. Les pannes de machines\n0. Pour quitter\n")
    a = input()
    c = int(a)
    if (c == 1):
        print("\nQuel algorithme voulez-vous utiliser ?\n1. La regression Lineaire\n2. L'arbre de décision\n0. Pour quitter")
        a = input()
        c = int(a)
        if(c == 1):
            print("Entrez les caractéristiques souhaitées (Pour ce modèle, trois caratéristiques sont demandées)\n")
            print("Size : \n")
            f0 = input()

            print("Nb_room : \n")
            f1 = input()

            print("Garden : \n")
            f2 = input()
            tab = np.array([int(f0), int(f1), int(f2)])
            print("Vous souhaitez donc exécutez ce programme avec les features suivantes :", tab)
            test_lin = generate_c_function_RegLin(model_lin, tab)
            fichier = open("main.c", "w")
            fichier.write(test_lin)
            fichier.close()
            print("rentrez la commande suivante : \ngcc main.c \ngcc -o output_file main.c\noutput_file.exe\n")

        if(c == 2):
            print("Entrez les caractéristiques souhaitées (Pour ce modèle, trois caratéristiques sont demandées)\n")
            print("Size : \n")
            f0 = input()

            print("Nb_room : \n")
            f1 = input()

            print("Garden : \n")
            f2 = input()
            tab = np.array([int(f0), int(f1), int(f2)])
            print("Vous souhaitez donc exécutez ce programme avec les features suivantes :", tab)
            tree = generate_c_function_Arbre(tree, tab)
            fichier = open("main.c", "w")
            fichier.write(tree)
            fichier.close()
            print("rentrez la commande suivante : \ngcc main.c \ngcc -o output_file main.c\noutput_file.exe\n")

    elif (c == 2) :
        print("Ces données sont uniquement disponibles avec la regression logistique\n")
        print("Entrez les caractéristiques souhaitées (Pour ce modèle, quatre caratéristiques sont demandées)\n")
        print("Vibration : \n")
        f0 = input()

        print("avg_speed : \n")
        f1 = input()

        print("age : \n")
        f2 = input()
        print("last revision : \n")
        f3 = input()

        tab = np.array([int(f0), int(f1), int(f2), int(f3)])
        test_log = generate_c_function_LogReg(model_log, tab)
        fichier = open("main.c", "w")
        fichier.write(test_log)
        fichier.close()
        print("rentrez la commande suivante : \ngcc main.c \ngcc -o output_file main.c\noutput_file.exe\n")
    elif (c == 0) :
        print("Vous allez nous quitter... A bientot")
    else:
        print("Votre saisie est incorrecte, merci d'entree une des saisies proposées\n")
        break






