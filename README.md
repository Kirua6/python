# python network mapping 
## Scanner réseau
Ce programme permet de scanner un réseau pour trouver les adresses IP et MAC des hôtes connectés au réseau.

## Utilisation
Installez Python --> https://www.python.org/ --> Downloads --> Python 3.11.3 <br>
Cochez la case path lors de l'installation pour ajouter Python aux variables d'environnement<br>
Installez les dépendances requises en exécutant la commande suivante : pip install scapy<br>
Installez le fork de WinPcap --> Npcap: https://npcap.com/#download | petit rappel: Un fork de WinPcap est une version modifiée et indépendante du logiciel WinPcap.<br>
Exécutez le programme en entrant python mapp.py dans un terminal.<br>
Entrez l'adresse IP que vous souhaitez scanner, le délai d'expiration et le nombre de tentatives.<br>
Les adresses IP et MAC des hôtes connectés seront affichées dans un tableau.<br>
Si vous souhaitez enregistrer les résultats dans un fichier CSV, entrez "O" lorsque vous êtes invité à le faire, puis entrez le nom du fichier CSV.

## Exemple

$ python mapp.py<br>
Entrez une adresse IP pour numériser le réseau: 192.168.1.0/24<br>
Entrez un délai d'expiration (en secondes): 10<br>
Entrez un nombre de tentatives: 3<br>
Adresse IP      Adresse MAC<br>
==========      ============<br>
192.168.1.1     00:11:22:33:44:55<br>
192.168.1.2     11:22:33:44:55:66<br>
192.168.1.3     22:33:44:55:66:77<br>
Voulez-vous enregistrer les résultats dans un fichier CSV? (O/N): O<br>
Entrez le nom du fichier CSV: adresses.csv<br>
Les résultats ont été enregistrés dans le fichier adresses.csv.<br>
