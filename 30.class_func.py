class Siswa:
    def __init__(self, nama, usia, ipk):
        self.nama = nama
        self.usia = usia
        self.ipk = ipk

    def cumlaude(self):
        if self.ipk >= 3.5:
            return True
        else:
            return False

andi = Siswa('Andi', 23, 3.6)
budi = Siswa('Budi', 23, 3.4)

print(andi.cumlaude())
print(budi.cumlaude())