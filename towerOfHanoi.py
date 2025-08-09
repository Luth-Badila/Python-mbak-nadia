def hanoi(n, asal, bantu, tujuan):
    if n == 1:
        print(f"Pindah cakram dari {asal} ke {tujuan}")
        return
    hanoi(n-1, asal, tujuan, bantu)
    print(f"Pindah cakram dari {asal} ke {tujuan}")
    hanoi(n-1, bantu, asal, tujuan)

hanoi(3, "A", "B", "C")
