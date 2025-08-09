while True:
    text = input("Ketik sesuatu (stop untuk berhenti): ")
    if text == "stop":
        print("Loop dihentikan.")
        break
    print(f"Kamu mengetik: {text}")