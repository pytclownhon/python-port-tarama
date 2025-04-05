import socket
import threading

print("""     
██████╗ ██╗   ██╗████████╗ ██████╗██╗      ██████╗ ██╗    ██╗███╗   ██╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██║     ██╔═══██╗██║    ██║████╗  ██║██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ██║     ██║     ██║   ██║██║ █╗ ██║██╔██╗ ██║███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██║     ██║     ██║   ██║██║███╗██║██║╚██╗██║██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ╚██████╗███████╗╚██████╔╝╚███╔███╔╝██║ ╚████║██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝    ╚═════╝╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                                                                 
""")



# Fonksiyon, port taramak için kullanılacak

def tarama(ip, port):
    try:
        tara = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tara.settimeout(1)  # Bağlantı zaman aşımını 1 saniye olarak ayarlıyoruz
        tara.connect((ip, port))
        print(f"[+] {port} portu açık")
    except:
        pass

# Kullanıcıdan giriş alıyoruz
ip = input("[+] Bir IP adresi girin: ")
mininmum_port = int(input("[+] En düşük portu girin: "))
maxsimum_port = int(input("[+] En yüksek portu girin: "))

# Portları taramak için çoklu iş parçacıkları (threads) oluşturuyoruz
threads = []
for port in range(mininmum_port, maxsimum_port + 1):
    t = threading.Thread(target=tarama, args=(ip, port))
    threads.append(t)
    t.start()

# Bütün iş parçacıklarının bitmesini bekliyoruz
for t in threads:
    t.join()
