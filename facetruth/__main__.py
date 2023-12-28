import os, sys
def interface():
    print("Selamat datang di FaceTruth")
    print("Cara penggunaan program ini : ")
    print("1. Masukkan path video yang ingin diuji")
    print("2. Akan muncul proses pengujian")
    print("3. Setelah selesai, akan muncul hasil pengujian")
    print("4. Jika ingin mengulang, tekan enter")
    print("5. Jika ingin keluar, ketik 'exit'")
  

def main():
    while True:
        interface()
        video = input("Masukkan path video: ")
        if video == "exit":
            sys.exit()
        else:
            video = video
        
        options = []
        options.append("-l")
        options.append("-r")
        os.system("python processing.py " + str(video) + " " + " ".join(options))
        print("Hasil pengujian dapat dilihat di folder facetruth")



if __name__ == "__main__":
    main()