import numpy as np

stari = ["dificil", "mediu", "usor"]
note = ["FB", "B", "S", "NS"]

matrice_tranzitie = np.array([
    [0.1, 0.2, 0.4],
    [0.25, 0.5, 0.25],
    [0.3, 0.4, 0.3]
])

matrice_emisie = np.array([
    [0.1, 0.2, 0.4, 0.3],
    [0.15, 0.25, 0.5, 0.1],
    [0.2, 0.3, 0.4, 0.1]
])

prob_initiere = np.array([1.0, 0.0, 0.0])

secventa_observata = [0, 1, 2, 1, 1, 2, 1, 2]

nr_stari = len(stari)
nr_observatii = len(secventa_observata)
viterbi = np.zeros((nr_stari, nr_observatii))
traseu = np.zeros((nr_stari, nr_observatii), dtype=int)

for s in range(nr_stari):
    viterbi[s, 0] = prob_initiere[s] * matrice_emisie[s, secventa_observata[0]]
    traseu[s, 0] = 0

for t in range(1, nr_observatii):
    for s in range(nr_stari):
        prob_stare = [
            viterbi[stare_anterioara, t - 1] * matrice_tranzitie[stare_anterioara, s] * matrice_emisie[s, secventa_observata[t]]
            for stare_anterioara in range(nr_stari)
        ]
        viterbi[s, t] = max(prob_stare)
        traseu[s, t] = np.argmax(prob_stare)

drum_final = np.zeros(nr_observatii, dtype=int)
drum_final[-1] = np.argmax(viterbi[:, -1])

for t in range(nr_observatii - 2, -1, -1):
    drum_final[t] = traseu[drum_final[t + 1], t + 1]

dificultati_probabile = [stari[stare] for stare in drum_final]
probabilitate = np.max(viterbi[:, -1])

print("Secventa observata de note:", [note[i] for i in secventa_observata])
print("Cea mai probabila secventa de dificultati ale testelor:", dificultati_probabile)
print("Probabilitatea secventei:", probabilitate)
