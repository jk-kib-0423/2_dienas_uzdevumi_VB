# Darbs ar failiem

faila_nosaukums = "dati.txt"

# režīmi: r - lasīšana, w - rakstīšana (pārraksta izdzēšot saturu), a - pievieno faila galā
with open(faila_nosaukums, "w", encoding="utf-8") as fails:
    fails.write("Pirmā testa rindiņa.\n")
    fails.write("Otra testa rindiņa.\n")


with open(faila_nosaukums, "a", encoding="utf-8") as fails:
    fails.write("Trešā rindiņa, kā papildinājums.\n")
    fails.write("Ceturtā rindiņa, nu jau lēnām pietiek.\n")
