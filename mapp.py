import scapy.all as scapy
#possibilité de remplacer "import scapy.all as scapy" par "from scapy.arch import get_windows_if_list, get_if_raw_addr, pcap"
import csv
import socket
import re

# Vérifie si une adresse IP est valide
def est_ip_valide(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Vérifie si une adresse MAC est valide
def est_mac_valide(mac):
    pattern = re.compile("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")
    return pattern.match(mac) is not None

# Scanner le réseau pour trouver les adresses IP et MAC
def scanner_reseau(ip, timeout=1, retry=2):
    # Vérifie si l'adresse IP est valide
    if not est_ip_valide(ip):
        print("Adresse IP invalide.")
        return []

    # Crée un paquet ARP pour demander l'adresse MAC de chaque hôte dans le réseau
    arp_request = scapy.ARP(pdst=ip)
    # Crée un paquet Ethernet pour envoyer le paquet ARP à l'adresse de diffusion
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine les paquets ARP et Ethernet pour envoyer une demande de diffusion ARP
    arp_request_broadcast = broadcast/arp_request

    # Envoie la demande ARP et récupère les réponses des hôtes
    # Réponse est une liste de paquets envoyés et reçus, avec la réponse dans le deuxième élément
    # Timeout et retry sont utilisés pour définir le temps d'attente pour la réponse et le nombre de tentatives
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=timeout, retry=retry, verbose=False)

    # Analyse les réponses pour extraire les adresses IP et MAC
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list

# Affiche les adresses IP et MAC dans un tableau
def afficher_tableau(clients_list):
    print("Adresse IP\tAdresse MAC")
    print("==========\t============")
    for client in clients_list:
        print(f"{client['ip']}\t{client['mac']}")

# Enregistre les adresses IP et MAC dans un fichier CSV
def enregistrer_csv(clients_list, nom_fichier):
    # Vérifie si le nom du fichier se termine par l'extension .csv
    if not nom_fichier.endswith(".csv"):
        nom_fichier += ".csv"

    # Crée un fichier CSV et écrit les adresses IP et MAC dans le fichier
    with open(nom_fichier, mode='w', newline='') as fichier_csv:
        champnames = ['ip', 'mac']
        writer = csv.DictWriter(fichier_csv, fieldnames=champnames)

        writer.writeheader()
        for client in clients_list:
            writer.writerow(client)

# Point d'entrée principal du programme
if __name__ == "__main__":
    # Demande à l'utilisateur l'adresse IP à numériser et les paramètres de numérisation
    adresse_ip = input("Entrez une adresse IP pour numériser le réseau: ")
    timeout = int(input("Entrez un délai d'expiration (en secondes): "))
    retry = int(input("Entrez un nombre de tentatives: "))

# Scanner le réseau pour trouver les adresses IP et MAC
scan_result = scanner_reseau(adresse_ip, timeout, retry)

# Afficher le résultat de la numérisation
afficher_tableau(scan_result)

# Demander à l'utilisateur s'il souhaite enregistrer les adresses IP et MAC dans un fichier CSV
reponse = input("Voulez-vous enregistrer les résultats dans un fichier CSV? (O/N): ")
if reponse.lower() == "o":
    nom_fichier = input("Entrez le nom du fichier CSV: ")
    enregistrer_csv(scan_result, nom_fichier)
    print(f"Les résultats ont été enregistrés dans le fichier {nom_fichier}.")
else:
    print("Aucun fichier n'a été enregistré.")

