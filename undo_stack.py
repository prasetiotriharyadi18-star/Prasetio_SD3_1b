
from collections import deque
from datetime import datetime


class UndoStack:
    def __init__(self):
        self.aktivitas = deque()

    def push(self, deskripsi):
        aktivitas_baru = {
            "waktu": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            ),
            "deskripsi": deskripsi
        }
        self.aktivitas.append(aktivitas_baru)
        return aktivitas_baru

    def pop(self):
        if self.is_empty():
            return None
        return self.aktivitas.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.aktivitas[-1]

    def is_empty(self):
        return len(self.aktivitas) == 0

    def tampilkan(self):
        if self.is_empty():
            print("Belum ada aktivitas.")
            return

        print("\n=== RIWAYAT AKTIVITAS ===")
        for aktivitas in reversed(self.aktivitas):
            print(
                f"{aktivitas['waktu']} - "
                f"{aktivitas['deskripsi']}"
            )