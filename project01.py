# =====================================
# SISTEM RESERVASI KURSI BIOSKOP
# =====================================

HARGA_TIKET = 50000

# DATA FILM DAN JAM TAYANG
films = {
    "1": {
        "judul": "Avengers",
        "jam": ["12:00", "15:00", "18:00"],
        "seats": {jam: {f"{chr(65+r)}{c+1}": "O" for r in range(5) for c in range(5)} for jam in ["12:00", "15:00", "18:00"]}
    },
    "2": {
        "judul": "Interstellar",
        "jam": ["13:00", "16:00", "19:00"],
        "seats": {jam: {f"{chr(65+r)}{c+1}": "O" for r in range(5) for c in range(5)} for jam in ["13:00", "16:00", "19:00"]}
    },
    "3": {
        "judul": "Spiderman",
        "jam": ["11:00", "14:00", "17:00"],
        "seats": {jam: {f"{chr(65+r)}{c+1}": "O" for r in range(5) for c in range(5)} for jam in ["11:00", "14:00", "17:00"]}
    }
}

reservations = []

# =====================================
# VISUAL KURSI
# =====================================
def tampilkan_kursi(film_id, jam):
    print(f"\nDenah Kursi - {films[film_id]['judul']} | Jam {jam}")
    seats = films[film_id]["seats"][jam]
    for r in range(5):
        for c in range(5):
            print(seats[f"{chr(65+r)}{c+1}"], end=" ")
        print()

# =====================================
# PILIH FILM & JAM
# =====================================
def pilih_film_dan_jam():
    print("\nDaftar Film:")
    for k, f in films.items():
        print(f"{k}. {f['judul']}")

    film_id = input("Pilih film: ")
    print("\nJam Tayang:")
    for i, j in enumerate(films[film_id]["jam"], 1):
        print(f"{i}. {j}")

    jam = films[film_id]["jam"][int(input("Pilih jam: ")) - 1]
    return film_id, jam

# =====================================
# STRUK PEMBELIAN
# =====================================
def cetak_struk(data):
    print("\n======= STRUK PEMBELIAN =======")
    print(f"Nama Pemesan : {data['nama']}")
    print(f"Film         : {data['film']}")
    print(f"Jam Tayang   : {data['jam']}")
    print(f"Kursi        : {data['kursi']}")
    print(f"Harga Tiket  : Rp{HARGA_TIKET:,}")
    print("================================")

# =====================================
# CREATE
# =====================================
def create_reservation():
    film_id, jam = pilih_film_dan_jam()
    tampilkan_kursi(film_id, jam)

    nama = input("Nama Pemesan: ")
    kursi = input("Pilih Kursi (A1-E5): ").upper()

    seats = films[film_id]["seats"][jam]
    if kursi in seats and seats[kursi] == "O":
        seats[kursi] = "X"
        data = {
            "nama": nama,
            "film": films[film_id]["judul"],
            "jam": jam,
            "kursi": kursi,
            "harga": HARGA_TIKET
        }
        reservations.append(data)
        print("Reservasi berhasil!")
        cetak_struk(data)
    else:
        print("Kursi tidak tersedia!")

# =====================================
# READ
# =====================================
def read_reservation():
    if not reservations:
        print("Belum ada reservasi.")
    for r in reservations:
        print(f"{r['nama']} | {r['film']} | {r['jam']} | {r['kursi']}")

# =====================================
# UPDATE
# =====================================
def update_reservation():
    nama = input("Nama pemesan: ")
    for r in reservations:
        if r["nama"].lower() == nama.lower():
            film_id, jam = pilih_film_dan_jam()
            tampilkan_kursi(film_id, jam)

            kursi_baru = input("Kursi baru: ").upper()
            seats = films[film_id]["seats"][jam]

            if kursi_baru in seats and seats[kursi_baru] == "O":
                seats[kursi_baru] = "X"
                r["film"] = films[film_id]["judul"]
                r["jam"] = jam
                r["kursi"] = kursi_baru
                print("Reservasi berhasil diubah!")
                return
    print("Data tidak ditemukan.")

# =====================================
# DELETE
# =====================================
def delete_reservation():
    nama = input("Nama pemesan: ")
    for r in reservations:
        if r["nama"].lower() == nama.lower():
            for f in films.values():
                for jam in f["jam"]:
                    if r["kursi"] in f["seats"][jam]:
                        f["seats"][jam][r["kursi"]] = "O"
            reservations.remove(r)
            print("Reservasi berhasil dihapus.")
            return
    print("Data tidak ditemukan.")

# =====================================
# SEARCHING
# =====================================
def search_reservation():
    keyword = input("Cari (nama/film/jam/kursi): ").lower()
    for r in reservations:
        if any(keyword in str(v).lower() for v in r.values()):
            print(r)

# =====================================
# SORTING
# =====================================
def sort_reservation():
    k = input("Urutkan berdasarkan (nama/film/jam/kursi): ")
    reservations.sort(key=lambda x: x[k])
    print("Data berhasil diurutkan.")

# =====================================
# MENU UTAMA
# =====================================
def menu():
    while True:
        print("\n=== SISTEM RESERVASI BIOSKOP ===")
        print("1. Lihat Kursi")
        print("2. Pesan Tiket")
        print("3. Lihat Reservasi")
        print("4. Ubah Reservasi")
        print("5. Hapus Reservasi")
        print("6. Cari Reservasi")
        print("7. Urutkan Reservasi")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            film_id, jam = pilih_film_dan_jam()
            tampilkan_kursi(film_id, jam)
        elif pilih == "2":
            create_reservation()
        elif pilih == "3":
            read_reservation()
        elif pilih == "4":
            update_reservation()
        elif pilih == "5":
            delete_reservation()
        elif pilih == "6":
            search_reservation()
        elif pilih == "7":
            sort_reservation()
        elif pilih == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

menu()