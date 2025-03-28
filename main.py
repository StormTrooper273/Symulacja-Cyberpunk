
import random

# Parametry:
Obrazenia_poczatkowe_L = 7
Wb_L = 11
# Pt rzutu na trafienie
Pt = 15
Refeleks_W = 7
Umiejetnosc_W = 4
inne_modyfikatory = 1
Bc_L = -2
Ilosc_obliczen = 10000000
i= 0
liczba_trafien = 0
liczba_trafionych_serii = 0
liczba_kulek =0
lokacja_trafienia = 0
liczba_trafien_w_glowe = 0
liczba_penetracji =0
suma_obrazen = 0
liczba_natychmiastowych_smierci = 0
suma_serii =0
natymchamistowa_smierc = False
rana_smiertelna = False
liczba_ran_smiertelnych = 0
trafiona_seria = False
Penetracja = False
trafinienie_w_glowe = False

# Kod:
for proba in range(Ilosc_obliczen):
    inne_modyfikatory = 1
    Wb_L=11
    suma_serii = 0
    natymchamistowa_smierc = False
    rana_smiertelna = False
    trafiona_seria = False
    Penetracja = False
    trafinienie_w_glowe = False
    if (random.randrange(1,11)+Umiejetnosc_W+Refeleks_W+inne_modyfikatory)>Pt:
        liczba_trafien+=1
        trafiona_seria = True
        liczba_trafionych_serii+=1
        liczba_kulek = random.randrange(1,7)
        if liczba_kulek == 6:
            liczba_kulek = 3
            liczba_trafien+=2
        elif liczba_kulek >3:
            liczba_kulek = 2
            liczba_trafien+=1
        else:
            liczba_kulek = 1
        for kula in range(liczba_kulek):
            lokacja_trafienia = random.randrange(1,11)
            if lokacja_trafienia == 1:
                if trafinienie_w_glowe == False:
                    liczba_trafien_w_glowe+=1
                Penetracja = True
            suma_kosci = (random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7))
            obrazenia = suma_kosci - Wb_L
            if obrazenia > 0:
                if Penetracja == False:
                    liczba_penetracji+=1
                Penetracja = True
                obrazenia = obrazenia+Bc_L
                Wb_L-=1
                if obrazenia < 1:
                    obrazenia = 1
                if lokacja_trafienia == 1:
                    obrazenia = obrazenia*2
                    if obrazenia >7:
                        liczba_natychmiastowych_smierci+=1  
                        natymchamistowa_smierc = True
                        break
                suma_serii+=obrazenia     
        suma_obrazen+=suma_serii
        if (suma_serii+obrazenia > 12) and (natymchamistowa_smierc == False):
            liczba_ran_smiertelnych+=1
            rana_smiertelna = True
    i+=1

'''
    
    if (rana_smiertelna == False) and (natymchamistowa_smierc == False):
        suma_serii = 0
        inne_modyfikatory-=2
        if (random.randrange(1,11)+Umiejetnosc_W+Refeleks_W+inne_modyfikatory)>Pt:
            liczba_trafien+=1
            if trafiona_seria ==False:
                liczba_trafionych_serii+=1
            liczba_kulek = random.randrange(1,7)
            if liczba_kulek == 6:
                liczba_kulek = 3
                liczba_trafien+=2
            elif liczba_kulek >3:
                liczba_kulek = 2
                liczba_trafien+=1
            else:
                liczba_kulek = 1
            for kula in range(liczba_kulek):
                lokacja_trafienia = random.randrange(1,11)
                if lokacja_trafienia == 1:
                    if trafinienie_w_glowe == False:
                        liczba_trafien_w_glowe+=1
                    Penetracja = True
                suma_kosci = (random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7))
                obrazenia = suma_kosci - Wb_L
                if obrazenia > 0:
                    if Penetracja == False:
                        liczba_penetracji+=1
                    obrazenia = obrazenia+Bc_L
                    Wb_L-=1
                    if obrazenia < 1:
                        obrazenia = 1
                    if lokacja_trafienia == 1:
                        obrazenia = obrazenia*2
                        if obrazenia >7:
                            liczba_natychmiastowych_smierci+=1  
                            natymchamistowa_smierc = True
                            break
                    suma_serii+=obrazenia     
            suma_obrazen+=suma_serii
            if (suma_serii+obrazenia > 12) and (natymchamistowa_smierc == False):
                liczba_ran_smiertelnych+=1
                rana_smiertelna = True
'''
    


# Wypisanie wartości 
print("Szana na trafienie choć jedną kulą:")
print(liczba_trafionych_serii/i)
print("Średnia ilość kul trafiających")
print(liczba_trafien/i)
print("Szansa na choć jedno trafienie w głowę:")
print(liczba_trafien_w_glowe/i)
print("Szansa na choć jedną penetrację panczerza:")
print(liczba_penetracji/i)
print("Średnie obrażnia")
print(suma_obrazen/i)
print("Szansa na natychmastową śmierć:")
print(liczba_natychmiastowych_smierci/i)
print("Szansa na ranę śmiertelną:")
print(liczba_ran_smiertelnych/i)



'''
for proba in range(Ilosc_obliczen):
    if 0 == 0:
        break
    print("a")
'''