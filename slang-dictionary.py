meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL":"tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY" : "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah"
            }
            
print("selamat datang di aplikasi kamus kata gaul!")
print("masukan 5 kata yang kamu ingin ketahui")
for i in range(5):            
    word = input("\nKetik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    
    if word == "END":
        print("\nterimakasih telah menggunakan kamus")
        break

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("kata tidak ditemukan")
