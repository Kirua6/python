# python network mapping 
## Scanner réseau
Ce programme permet de scanner un réseau pour trouver les adresses IP et MAC des hôtes connectés au réseau.

## Utilisation
Installez les dépendances requises en exécutant la commande suivante : pip install scapy
Installez le fork de WinPcap --> Npcap: https://npcap.com/#download | petit rappel: Un fork de WinPcap est une version modifiée et indépendante du logiciel WinPcap.
Exécutez le programme en entrant python mapp.py dans un terminal.
Entrez l'adresse IP que vous souhaitez scanner, le délai d'expiration et le nombre de tentatives.
Les adresses IP et MAC des hôtes connectés seront affichées dans un tableau.
Si vous souhaitez enregistrer les résultats dans un fichier CSV, entrez "O" lorsque vous êtes invité à le faire, puis entrez le nom du fichier CSV.

## Exemple

$ python scanner_reseau.py
Entrez une adresse IP pour numériser le réseau: 192.168.1.0/24
Entrez un délai d'expiration (en secondes): 10
Entrez un nombre de tentatives: 3
Adresse IP      Adresse MAC
==========      ============
192.168.1.1     00:11:22:33:44:55
192.168.1.2     11:22:33:44:55:66
192.168.1.3     22:33:44:55:66:77
Voulez-vous enregistrer les résultats dans un fichier CSV? (O/N): O
Entrez le nom du fichier CSV: adresses.csv
Les résultats ont été enregistrés dans le fichier adresses.csv.
