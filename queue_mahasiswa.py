
from collections import deque


class QueueMahasiswa:
    def __init__(self):
        self.antrean = deque()

    def enqueue(self, nomor, nama):
        mahasiswa = {
            "nomor": nomor,
            "nama": nama
        }
        self.antrean.append(mahasiswa)
        return mahasiswa

    def dequeue(self):
        if self.is_empty():
            return None
        return self.antrean.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self.antrean[0]

    def is_empty(self):
        return len(self.antrean) == 0

    def tampilkan(self):
        if self.is_empty():
            print("Antrean masih kosong.")
            return

        print("\n=== DAFTAR ANTREAN ===")
        for mahasiswa in self.antrean:
            print(
                f"No. {mahasiswa['nomor']} - "
                f"{mahasiswa['nama']}"
            )