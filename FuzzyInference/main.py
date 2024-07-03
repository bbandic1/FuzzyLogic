import matplotlib.pyplot as plt
import numpy as np

def dajTrougaoVrijednosti(x, a, b, c):
    if x <= a:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    elif x >= c:
        return 0
    elif x == b:
        return 1

def dajTrapezVrijednosti(x, a, b, c, d):
    if x <= a:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c < x < d:
        return (d - x) / (d - c)
    elif x >= d:
        return 0

class Fuzzy:
    def __init__(self):
        self.ulazi = {}
        self.izlazi = {}
        self.pravila_zakljucivanja = {}

    def napraviUlaznuFunkciju(self, ime):
        self.ulazi[ime] = {}

    def napraviIzlaznuFunkciju(self, ime):
        self.izlazi[ime] = {}

    def dodajFunkcijuPripadnostiUlazi(self, ime, opis, a, b, c, d=None):
        if d is None:
            self.ulazi[ime][opis] = lambda x: dajTrougaoVrijednosti(x, a, b, c)
        else:
            self.ulazi[ime][opis] = lambda x: dajTrapezVrijednosti(x, a, b, c, d)

    def dodajFunkcijuPripadnostiIzlazi(self, ime, opis, a, b, c, d=None):
        if d is None:
            self.izlazi[ime][opis] = lambda x: dajTrougaoVrijednosti(x, a, b, c)
        else:
            self.izlazi[ime][opis] = lambda x: dajTrapezVrijednosti(x, a, b, c, d)

    def definisiPravilo(self, broj, vrijednost1, vrijednost2, vrijednostIzlaza):
        self.pravila_zakljucivanja[broj] = (vrijednost1, vrijednost2, vrijednostIzlaza)

    def dajYVrijednosti(self, ime, opis, xmin, xmax, num_points=1000):
        x_values = np.linspace(xmin, xmax, num_points)
        y_values = [self.ulazi[ime][opis](x) for x in x_values]
        return x_values, y_values

    def dajYzaSveFunkcijePripadnosti(self, ime, x):
        y_values = {opis: self.ulazi[ime][opis](x) for opis in self.ulazi[ime]}
        return y_values

    def izracunajDOF(self, x, y, opis1, opis2):
        return min(self.ulazi["naoruzanje"][opis1](y), self.ulazi["udaljenost"][opis2](x))

    def spajanje(self, spojeniUlaz, trenutniIzlaz):
        return np.fmax(spojeniUlaz, trenutniIzlaz)

    def mamdaniImplikacija(self, dof, pripadnost):
        return np.minimum(pripadnost, dof)

    def defuzzifikacijaCOS(self, spojeniIzlaz, xVrijednost):
        brojnik = np.sum(spojeniIzlaz * xVrijednost)
        nazivnik = np.sum(spojeniIzlaz)
        if nazivnik == 0:
            return 0
        return brojnik / nazivnik

    def zakljuci(self, x, y):
        dofs = []
        for broj, (vrijednost1, vrijednost2, vrijednostIzlaza) in self.pravila_zakljucivanja.items():
            dof = self.izracunajDOF(x, y, vrijednost1, vrijednost2)
            dofs.append((dof, vrijednostIzlaza))

        xVrijednosti = np.linspace(0, 100, 1000)
        spojeniIzlaz = np.zeros_like(xVrijednosti)

        for dof, vrijednostIzlaza in dofs:
            izlaz_values = np.array([self.izlazi["agresivnost"][vrijednostIzlaza](x) for x in xVrijednosti])
            trenutniIzlaz = np.array([self.mamdaniImplikacija(dof, prip) for prip in izlaz_values])
            spojeniIzlaz = self.spajanje(spojeniIzlaz, trenutniIzlaz)

        return self.defuzzifikacijaCOS(spojeniIzlaz, xVrijednosti)


fuzzy = Fuzzy()
fuzzy.napraviUlaznuFunkciju("udaljenost")
fuzzy.napraviUlaznuFunkciju("naoruzanje")
fuzzy.napraviIzlaznuFunkciju("agresivnost")

fuzzy.dodajFunkcijuPripadnostiUlazi("udaljenost", "veoma_blizu", 0, 0, 10, 10)
fuzzy.dodajFunkcijuPripadnostiUlazi("udaljenost", "blizu", 10, 15, 40, 50)
fuzzy.dodajFunkcijuPripadnostiUlazi("udaljenost", "daleko", 50, 60, 70, 80)
fuzzy.dodajFunkcijuPripadnostiUlazi("udaljenost", "veoma_daleko", 80, 80, 100, 100)

fuzzy.dodajFunkcijuPripadnostiUlazi("naoruzanje", "nenaoruzani", 0, 0, 10, 10)
fuzzy.dodajFunkcijuPripadnostiUlazi("naoruzanje", "blago_naoruzani", 10, 50, 100, 130)
fuzzy.dodajFunkcijuPripadnostiUlazi("naoruzanje", "naoruzani", 100, 150, 400, 450)
fuzzy.dodajFunkcijuPripadnostiUlazi("naoruzanje", "vrlo_naoruzani", 400, 600, 800, 800)

fuzzy.dodajFunkcijuPripadnostiIzlazi("agresivnost", "neagresivni", 0, 10, 20, 25)
fuzzy.dodajFunkcijuPripadnostiIzlazi("agresivnost", "malo_agresivni", 20, 40, 60, 70)
fuzzy.dodajFunkcijuPripadnostiIzlazi("agresivnost", "vrlo_agresivni", 65, 85, 90, 95)
fuzzy.dodajFunkcijuPripadnostiIzlazi("agresivnost", "izrazito_agresivni", 93, 95, 100, 100)

fuzzy.definisiPravilo(1, 'nenaoruzani', 'daleko', 'neagresivni')
fuzzy.definisiPravilo(2, 'nenaoruzani', 'blizu', 'neagresivni')
fuzzy.definisiPravilo(3, 'nenaoruzani', 'veoma_blizu', 'neagresivni')
fuzzy.definisiPravilo(4, 'nenaoruzani', 'veoma_daleko', 'neagresivni')
fuzzy.definisiPravilo(5, 'blago_naoruzani', 'daleko', 'neagresivni')
fuzzy.definisiPravilo(6, 'naoruzani', 'daleko', 'neagresivni')
fuzzy.definisiPravilo(7, 'vrlo_naoruzani', 'daleko', 'neagresivni')
fuzzy.definisiPravilo(8, 'nenaoruzani', 'blizu', 'neagresivni')
fuzzy.definisiPravilo(9, 'blago_naoruzani', 'blizu', 'neagresivni')
fuzzy.definisiPravilo(10, 'vrlo_naoruzani', 'blizu', 'malo_agresivni')
fuzzy.definisiPravilo(11, 'naoruzani', 'blizu', 'malo_agresivni')
fuzzy.definisiPravilo(12, 'blago_naoruzani', 'veoma_blizu', 'malo_agresivni')
fuzzy.definisiPravilo(13, 'naoruzani', 'veoma_blizu', 'malo_agresivni')
fuzzy.definisiPravilo(14, 'vrlo_naoruzani', 'veoma_blizu', 'vrlo_agresivni')
fuzzy.definisiPravilo(15, 'vrlo_naoruzani', 'veoma_daleko', 'malo_agresivni')



x = input("Unesite udaljenost od granice (u blokovima): ")

y = input("Unesite broj trupa: ")

x = int(x)
y = int(y)

result = fuzzy.zakljuci(x, y)
print("Crisp vrijednost: ", result)
rezString = ""
if 0 <= result < 20:
    rezString = "neagresivni"
elif 20 <= result < 65:
    rezString = "malo agresivni"
elif 65 <= result < 90:
    rezString = "vrlo agresivni"
elif 90 <= result:
    rezstring = "izrazito agresivni"
print(f"Rezultat za udaljenost = {x} i oruzanje = {y}: " + rezString)

plt.figure(figsize=(14, 8))

xValues = np.linspace(0, 100, 1000)
for opis in fuzzy.ulazi["udaljenost"]:
    yValues = [fuzzy.ulazi["udaljenost"][opis](x) for x in xValues]
    plt.plot(xValues, yValues, label=f'Udaljenost - {opis}')
plt.title('Funkcija pripadnosti za udaljenost')
plt.xlabel('Udaljenost')
plt.ylabel('Stepen pripadnosti')
plt.legend()
plt.grid(True)
plt.show()


xValues = np.linspace(0, 800, 10000)
plt.figure(figsize=(14, 8))
for opis in fuzzy.ulazi["naoruzanje"]:
    yValues = [fuzzy.ulazi["naoruzanje"][opis](x) for x in xValues]
    plt.plot(xValues, yValues, label=f'Naoruzanje - {opis}')
plt.title('Funkcija pripadnosti za naoruzanje')
plt.xlabel('Naoruzanje')
plt.ylabel('Stepen pripadnosti')
plt.legend()
plt.grid(True)
plt.show()
