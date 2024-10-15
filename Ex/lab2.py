# # Definim nodurile și structura rețelei bayesiene
# nodes = ['S', 'O', 'L', 'M']

# # Reprezentăm graful ca un dicționar, unde fiecare cheie este un nod,
# # iar valoarea este o listă de noduri către care există arce (nodurile copil)
# edges = {
#     'S': ['O', 'L', 'M'],  # S influențează direct O, L și M
#     'O': [],               # O nu influențează alte variabile
#     'L': ['M'],            # L influențează direct M
#     'M': []                # M nu influențează alte variabile
# }

# # Funcție pentru a identifica independențele din rețea
# def independencies():
#     # O și L sunt independente condiționat de S
#     # Explicație:
#     # - O și L sunt ambele influențate direct de S
#     # - Nu există o legătură directă între O și L
#     # - Odată ce cunoaștem valoarea lui S, informația despre O nu ne oferă
#     #   informații suplimentare despre L, și viceversa
#     print('1. O este independent de L condiționat de S')
    
#     # O și M sunt independente condiționat de S și L
#     # Explicație:
#     # - O depinde doar de S
#     # - M depinde de S și L
#     # - Nu există o cale de influență de la O la M care să nu treacă prin S sau L
#     # - Cunoscând S și L, O și M devin independente
#     print('2. O este independent de M condiționat de S și L')
    
#     # O și L sunt dependente marginal (fără a condiționa pe S)
#     # Explicație:
#     # - Ambele variabile sunt influențate de S
#     # - Fără a cunoaște valoarea lui S, O și L par dependente deoarece
#     #   variază în funcție de S (efect de cauză comună)
#     print('3. O și L sunt dependente marginal')
    
#     # L și M sunt dependente chiar și condiționat de S
#     # Explicație:
#     # - L influențează direct M
#     # - Chiar dacă cunoaștem valoarea lui S, L are un efect direct asupra lui M
#     # - Deci L și M nu sunt independente condiționat de S
#     print('4. L și M sunt dependente chiar și condiționat de S')
    
#     # O și M sunt dependente marginal (fără a condiționa pe S și L)
#     # Explicație:
#     # - O depinde de S, iar M depinde de S și L
#     # - Fără a cunoaște valorile lui S și L, există o dependență aparentă între O și M
#     print('5. O și M sunt dependente marginal')
    
#     # S și M sunt dependente
#     # Explicație:
#     # - S influențează direct M
#     # - Există o legătură directă între S și M
#     print('6. S și M sunt dependente')

# # Apelăm funcția pentru a afișa independențele identificate
# independencies()




















# B
# Definim probabilitățile a priori pentru S
P_S = {
    1: 0.4,  # P(S=1): Probabilitatea ca un e-mail să fie spam
    0: 0.6   # P(S=0): Probabilitatea ca un e-mail să nu fie spam
}

# Definim probabilitățile condiționate P(O|S)
P_O_given_S = {
    (1, 1): 0.7,  # P(O=1 | S=1): Probabilitatea ca e-mail-ul să conțină "ofertă" dacă este spam
    (1, 0): 0.3,  # P(O=0 | S=1): Probabilitatea ca e-mail-ul să nu conțină "ofertă" dacă este spam
    (0, 1): 0.4,  # P(O=1 | S=0): Probabilitatea ca e-mail-ul să conțină "ofertă" dacă nu este spam
    (0, 0): 0.6   # P(O=0 | S=0): Probabilitatea ca e-mail-ul să nu conțină "ofertă" dacă nu este spam
}

# Definim probabilitățile condiționate P(L|S)
P_L_given_S = {
    (1, 1): 0.8,  # P(L=1 | S=1): Probabilitatea ca e-mail-ul să conțină link-uri dacă este spam
    (1, 0): 0.2,  # P(L=0 | S=1): Probabilitatea ca e-mail-ul să nu conțină link-uri dacă este spam
    (0, 1): 0.3,  # P(L=1 | S=0): Probabilitatea ca e-mail-ul să conțină link-uri dacă nu este spam
    (0, 0): 0.7   # P(L=0 | S=0): Probabilitatea ca e-mail-ul să nu conțină link-uri dacă nu este spam
}

# Definim probabilitățile condiționate P(M|S,L)
P_M_given_S_L = {
    (1, 1, 1): 0.9,  # P(M=1 | S=1, L=1): Probabilitatea ca e-mail-ul să aibă lungime mare dacă este spam și conține link-uri
    (1, 1, 0): 0.1,  # P(M=0 | S=1, L=1)
    (1, 0, 1): 0.5,  # P(M=1 | S=1, L=0)
    (1, 0, 0): 0.5,  # P(M=0 | S=1, L=0)
    (0, 1, 1): 0.6,  # P(M=1 | S=0, L=1)
    (0, 1, 0): 0.4,  # P(M=0 | S=0, L=1)
    (0, 0, 1): 0.2,  # P(M=1 | S=0, L=0)
    (0, 0, 0): 0.8   # P(M=0 | S=0, L=0)
}

# Funcție pentru a calcula și a afișa clasificarea e-mail-ului
def classify_email(O, L, M):
    # Calculăm probabilitatea comună pentru S=1
    # P(S=1, O, L, M) = P(S=1) * P(O|S=1) * P(L|S=1) * P(M|S=1, L)
    joint_prob_S1 = (
        P_S[1] *
        P_O_given_S[(1, O)] *
        P_L_given_S[(1, L)] *
        P_M_given_S_L[(1, L, M)]
    )

    # Calculăm probabilitatea comună pentru S=0
    # P(S=0, O, L, M) = P(S=0) * P(O|S=0) * P(L|S=0) * P(M|S=0, L)
    joint_prob_S0 = (
        P_S[0] *
        P_O_given_S[(0, O)] *
        P_L_given_S[(0, L)] *
        P_M_given_S_L[(0, L, M)]
    )

    # Calculăm probabilitățile a posteriori prin normalizare
    total_prob = joint_prob_S1 + joint_prob_S0
    P_S1_given_OLM = joint_prob_S1 / total_prob
    P_S0_given_OLM = joint_prob_S0 / total_prob

    # Determinăm clasificarea
    if P_S1_given_OLM > P_S0_given_OLM:
        classification = 'Spam'
    else:
        classification = 'Non-Spam'

    # Afișăm rezultatele
    print(f"Probabilitatea ca e-mail-ul să fie Spam (S=1): {P_S1_given_OLM:.4f}")
    print(f"Probabilitatea ca e-mail-ul să fie Non-Spam (S=0): {P_S0_given_OLM:.4f}")
    print(f"Clasificare: {classification}\n")

# Exemple de clasificare
# Exemplul 1: O=1 (conține "ofertă"), L=1 (conține link-uri), M=1 (lungime mare)
print("Exemplul 1: O=1, L=1, M=1")
classify_email(O=1, L=1, M=1)

# Exemplul 2: O=0 (nu conține "ofertă"), L=1 (conține link-uri), M=0 (lungime mică)
print("Exemplul 2: O=0, L=1, M=0")
classify_email(O=0, L=1, M=0)

# Exemplul 3: O=1 (conține "ofertă"), L=0 (nu conține link-uri), M=1 (lungime mare)
print("Exemplul 3: O=1, L=0, M=1")
classify_email(O=1, L=0, M=1)
