
from queue_mahasiswa import QueueMahasiswa
from undo_stack import UndoStack


def menu_antrean(queue):
    while True:
        print("\n=== MENU ANTREAN MAHASISWA ===")
        print("1. Tambah mahasiswa")
        print("2. Layani mahasiswa")
        print("3. Lihat mahasiswa terdepan")
        print("4. Periksa antrean kosong")
        print("5. Tampilkan seluruh antrean")
        print("0. Kembali")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            nama = input("Nama mahasiswa: ").strip()
            if not nama:
                print("Nama tidak boleh kosong.")
                continue

            nomor = input("Nomor antrean: ").strip()
            if not nomor:
                print("Nomor antrean tidak boleh kosong.")
                continue

            mahasiswa = queue.enqueue(nomor, nama)
            print(
                f"Mahasiswa {mahasiswa['nama']} "
                "berhasil ditambahkan."
            )

        elif pilihan == "2":
            mahasiswa = queue.dequeue()
            if mahasiswa is None:
                print("Antrean kosong, tidak ada yang dilayani.")
            else:
                print(
                    f"Mahasiswa {mahasiswa['nama']} "
                    "sedang dilayani."
                )

        elif pilihan == "3":
            mahasiswa = queue.front()
            if mahasiswa is None:
                print("Antrean masih kosong.")
            else:
                print(
                    f"Mahasiswa terdepan: "
                    f"{mahasiswa['nama']} "
                    f"(No. {mahasiswa['nomor']})"
                )

        elif pilihan == "4":
            if queue.is_empty():
                print("Antrean kosong.")
            else:
                print("Antrean masih berisi mahasiswa.")

        elif pilihan == "5":
            queue.tampilkan()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid.")


def menu_undo(undo):
    while True:
        print("\n=== MENU UNDO AKTIVITAS ===")
        print("1. Tambah aktivitas")
        print("2. Undo aktivitas terakhir")
        print("3. Lihat aktivitas terakhir")
        print("4. Periksa tumpukan kosong")
        print("5. Tampilkan riwayat aktivitas")
        print("0. Kembali")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            deskripsi = input(
                "Masukkan aktivitas petugas: "
            ).strip()

            if not deskripsi:
                print("Aktivitas tidak boleh kosong.")
                continue

            aktivitas = undo.push(deskripsi)
            print(
                "Aktivitas berhasil disimpan pada "
                f"{aktivitas['waktu']}."
            )

        elif pilihan == "2":
            aktivitas = undo.pop()
            if aktivitas is None:
                print("Tidak ada aktivitas untuk di-Undo.")
            else:
                print(
                    "Aktivitas terakhir dibatalkan: "
                    f"{aktivitas['deskripsi']}"
                )

        elif pilihan == "3":
            aktivitas = undo.peek()
            if aktivitas is None:
                print("Belum ada aktivitas.")
            else:
                print(
                    f"Aktivitas terakhir: "
                    f"{aktivitas['deskripsi']}"
                )
                print(f"Waktu: {aktivitas['waktu']}")

        elif pilihan == "4":
            if undo.is_empty():
                print("Tumpukan aktivitas kosong.")
            else:
                print("Masih ada aktivitas tersimpan.")

        elif pilihan == "5":
            undo.tampilkan()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid.")


def main():
    queue = QueueMahasiswa()
    undo = UndoStack()

    while True:
        print("\n================================")
        print(" SISTEM LAYANAN ADMINISTRASI")
        print("       MAHASISWA")
        print("================================")
        print("1. Sistem antrean mahasiswa")
        print("2. Fitur Undo aktivitas")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            menu_antrean(queue)
        elif pilihan == "2":
            menu_undo(undo)
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()