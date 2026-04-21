harga = float(input("Harga"))
jumlah = int(input("Jumlah"))

total = harga * jumlah

if total > 250000:
  diskon = total * 0.10 
  totalbayar = total - diskon
  print(f"Total: {total:,.0f}")
  print(f"Diskon 50%: {diskon:,.0f}")
  print(f"Total Bayar: {totalbayar:,.0f}")
else:
  print(f"Total bayar: {total:,.0f}")
  print("Gada diskon")