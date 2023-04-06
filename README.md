# IA

Dans ce Git, vous trouverez 2 dossiers. 
Le premier correspondant aux exercices demandés lors du TP1 et le deuxième : au TP2.

## Licence :

Ces codes sont des fichiers réalisés dans le cadre éducatif. Ils peuvent être réutilisés et adaptés mais les sources ne doivent pas être modifié par un individu qui n'a pas les droits dessus.

# TP1 IA

Vous trouverez dans ce dossier les différents fichiers joblib nécessaire au bon fonctionnement du code, ainsi que le code lui-même permettant de tester plusieurs algorithmes tel que :
- La régression linéaire
- La régression logistique
- Les arbres de décision

En lançant le script Python, vous aurez le choix entre prendre les données sur les prix des maisons ou les données sur la maintenance des machines. Par la suite, en fonction du modèle choisi, vous pourrez exécuter un modèle selon les choix proposés. 

## Installation : 

Commencez par télécharger le dossier. Ouvrez ensuite un compilateur python et executez le fichier .py. Ensuite, vous serez ammené à faire certains choix comme celui du modèle, des features à prédire et d'autres. Par la suite, un script .c se forme avec lequel vous allez pouvoir obtenir la prédiction de votre modèle choisi lorsque vous allez executer ce fichier. Enfin, pour l'exécuter, il suffit de rentrer les commandes envoyées par python dans votre terminal.

## Utilisation :

Voilà un exemple d'utilisation :

Au lancement, on nous demande le script à executer :

![image](https://user-images.githubusercontent.com/66334739/230494779-dbdd38a6-808e-4b10-a1b1-8ed44c94c798.png)

Dans notre cas, nous avons choisi le prix des maisons.

Ensuite, nous allons devoir choisir le modèle :

![image](https://user-images.githubusercontent.com/66334739/230494941-a2167e12-245c-4dfe-b1bb-9370b9ae2e02.png)

Nous avons donc choisi la régression linaire.
Le code nous demande donc de choisir nos features pour la prédiction :

![image](https://user-images.githubusercontent.com/66334739/230495116-266ae0f7-7ed9-46ea-9c82-eba834c31484.png)

Enfin, il nous informe des données à entrer dans le terminal :

![image](https://user-images.githubusercontent.com/66334739/230495223-1d09cef4-9d6a-4442-a45b-1dea6186d40f.png)

Dans le terminal on a :

![image](https://user-images.githubusercontent.com/66334739/230495462-622db063-d309-49ef-a8ca-9f60d9f6e230.png)

Donc je vais dans le bon dossier à l'aide de la commande cd. Ensuite, je copie colle une à une les commandes. La première est pour vérifier la compilation, la deuxième est pour créer le script d'execution et la troisième est pour exécuter le code.

## Compatibilité :

Ces script ont été executés avec Python 3.10 et un compilateur gcc.


# IA TP2

Vous trouverez dans ce TP l'ensemble des fichiers générés par le TP.

Les tests bench sont les suivants :
L'exercice 1 : test_and_gate.v
L'exercice 2 : test_exercice2.v
L'exercice 3 : test_exercice3.v
L'additionneur 1 Bit : test_Add1B.v
L'additionneur 8 Bits : test_Add8B.v
Le multiplieur 8 Bits : test_Mul8B.v
La régression linéaire simple : test_Regression.v
Le transpileur dans python : Regression_nV_py_test.v

Egalement, vous trouverez un pdf (ReponseTP2.pdf) avec les réponses et les résultats trouvés.

Enfin, le transpiler.py correspond au script python demandé dans le dernier exercice.

Le transpiler est compatible avec c0 a 32 bits, et le reste des coefficients et des caractéristiques à 16 bits.

## Installation : 

Commencez par télécharger le dossier. Ensuite, si vous souhaitez executer du verilog alors vous pouvez directement vous rendre sur le terminal et executer les fonctions souhaitées.

Sinon, pour executer le code python, ouvrez un compilateur et executez le code. 

Plus de détails sont disponibles dans le pdf.

## Compatibilité :

La version python utilisée était la 3.10.
