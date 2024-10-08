import random

bile_initiale = {'roșii': 3, 'albastre': 4, 'negre': 2}

def adauga_bila(zar, urna):
    if zar in [2, 3, 5]:
        urna['negre'] += 1
    elif zar == 6:
        urna['roșii'] += 1
    else:
        urna['albastre'] += 1
    return urna

def simulare_experiment():
    urna = bile_initiale.copy()
    zar = random.randint(1, 6)
    urna = adauga_bila(zar, urna)
    total_bile = sum(urna.values())
    extragere = random.choices(list(urna.keys()), weights=urna.values(), k=1)[0]
    return extragere

rezultate = [simulare_experiment() for _ in range(1000)]

numar_rosii = rezultate.count('roșii')
numar_albastre = rezultate.count('albastre')
numar_negre = rezultate.count('negre')

probabilitate_rosii = numar_rosii / len(rezultate)

total_initial = sum(bile_initiale.values())
probabilitate_prime = 3 / 6
probabilitate_6 = 1 / 6
probabilitate_rest = 2 / 6

total_prime = total_initial + 1
total_6 = total_initial + 1
total_rest = total_initial + 1

p_rosii_prime = bile_initiale['roșii'] / total_prime
p_rosii_6 = (bile_initiale['roșii'] + 1) / total_6
p_rosii_rest = bile_initiale['roșii'] / total_rest

probabilitate_teoretica = (probabilitate_prime * p_rosii_prime +
                           probabilitate_6 * p_rosii_6 +
                           probabilitate_rest * p_rosii_rest)

print(f"Bilele extrase în urma experimentului sunt: {rezultate[:10]}...")  
print(f"Număr bile roșii extrase: {numar_rosii}")
print(f"Număr bile albastre extrase: {numar_albastre}")
print(f"Număr bile negre extrase: {numar_negre}")
#b
print(f"Probabilitatea estimată de a extrage o bilă roșie: {probabilitate_rosii:.4f}")
#Bonus
print(f"Probabilitatea teoretică de a extrage o bilă roșie: {probabilitate_teoretica:.4f}")
print(f"Diferența dintre probabilitatea teoretică și cea estimată: {abs(probabilitate_teoretica - probabilitate_rosii):.4f}")
