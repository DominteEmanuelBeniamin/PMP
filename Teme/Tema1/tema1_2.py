#Numărul de pași NN urmează o distribuție geometrică,
# pentru că jocul se termină la prima apariție a stemei.
# Probabilitatea să ajungem la pasul n este (1−p)n−1⋅p(1−p)n−1⋅p,
# unde pp e șansa de a obține stema,
#  iar (1−p)(1−p) e șansa de a obține banul la fiecare pas anterior.


import random
import matplotlib.pyplot as plt


def simulare_joc(prob_stema=0.5):
    N = 0  
    S = 0  
    while True:
        N += 1
        if random.random() < prob_stema:
            zar = random.randint(1, 6)  
            S += (zar - 3)  
            break
        else:
            S -= 0.5  
    return N, S


N, S = simulare_joc()
print(f"Numărul de pași: {N}, Suma totală: {S} $")





numar_jocuri = 10000
rezultate_S = []


for _ in range(numar_jocuri):
    _, S = simulare_joc()
    rezultate_S.append(S)

media_S = sum(rezultate_S) / numar_jocuri
print(f"Media sumei totale S: {media_S} $")

plt.hist(rezultate_S, bins=20, edgecolor='black')
plt.title("Distribuția sumei totale S")
plt.xlabel("Suma totală S ($)")
plt.ylabel("Frecvența")
plt.show()



rezultate_S_03 = []
for _ in range(numar_jocuri):
    _, S = simulare_joc(prob_stema=0.3)
    rezultate_S_03.append(S)

media_S_03 = sum(rezultate_S_03) / numar_jocuri
print(f"Media sumei totale S pentru p = 0.3: {media_S_03} $")

plt.hist(rezultate_S_03, bins=20, edgecolor='black')
plt.title("Distribuția sumei totale S pentru p = 0.3")
plt.xlabel("Suma totală S ($)")
plt.ylabel("Frecvența")
plt.show()

rezultate_S_07 = []
for _ in range(numar_jocuri):
    _, S = simulare_joc(prob_stema=0.7)
    rezultate_S_07.append(S)

media_S_07 = sum(rezultate_S_07) / numar_jocuri
print(f"Media sumei totale S pentru p = 0.7: {media_S_07} $")

plt.hist(rezultate_S_07, bins=20, edgecolor='black')
plt.title("Distribuția sumei totale S pentru p = 0.7")
plt.xlabel("Suma totală S ($)")
plt.ylabel("Frecvența")
plt.show()
