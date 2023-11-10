names, fees = ["Monnei", "Fjee", "Dolladollabilljoll"], []
for _ in range(3):
    fees.append(int(input()))
print(names[fees.index(min(fees))])
