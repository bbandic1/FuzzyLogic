#include <iostream>
#include <string>
#include <map>

// Definicija lingvističkih varijabli i funkcija pripadnosti
enum class Vrijeme {jakakisa, magla, suncano};
enum class Saobracaj {guzva, malosaobracaja, nemasaobracaja};
enum class StanjePuta {klizav, suh};
enum class Vidljivost {niska, srednja, visoka};
enum class Udaljenost {blizu, umjereno, daleko};
enum class Brzina {sporo, umjereno, brzo};

// Funkcije pripadnosti za vremenske uslove
double pripadnostVremenu(Vrijeme vrijeme, double x) 
{
    switch (vrijeme) 
    {
        case Vrijeme::jakakisa:
            if (x >= 0 && x <= 2)
                return 1.0;
            else if (x > 2 && x <= 5)
                return 1.0 - (x - 2) / 3.0;
            else
                return 0.0;
        case Vrijeme::magla:
            if (x > 2 && x <= 5)
                return (x - 2) / 3.0;
            else if (x > 5 && x <= 7)
                return 1.0;
            else if (x > 7 && x <= 10)
                return 1.0 - (x - 7) / 3.0;
            else
                return 0.0;
        case Vrijeme::suncano:
            if (x <= 7)
                return 0.0;
            else if (x > 7 && x <= 10)
                return (x - 7) / 3.0;
            else
                return 1.0;
    }
    return 0.0;
}

// Funkcije pripadnosti za gustinu saobraćaja
double pripadnostSaobracaju(Saobracaj saobracaj, double x) 
{
    switch (saobracaj) 
    {
        case Saobracaj::guzva:
            if (x >= 0 && x <= 3)
                return 1.0;
            else if (x > 3 && x <= 5)
                return 1.0 - (x - 3) / 2.0;
            else
                return 0.0;
        case Saobracaj::malosaobracaja:
            if (x > 3 && x <= 5)
                return (x - 3) / 2.0;
            else if (x > 5 && x <= 7)
                return 1.0;
            else if (x > 7 && x <= 9)
                return 1.0 - (x - 7) / 2.0;
            else
                return 0.0;
        case Saobracaj::nemasaobracaja:
            if (x <= 7)
                return 0.0;
            else if (x > 7 && x <= 9)
                return (x - 7) / 2.0;
            else
                return 1.0;
    }
    return 0.0;
}

// Funkcije pripadnosti za vidljivost
double pripadnostVidljivosti(Vidljivost vidljivost, double x) 
{
    switch (vidljivost) 
    {
        case Vidljivost::niska:
            if (x >= 0 && x <= 3)
                return 1.0;
            else if (x > 3 && x <= 5)
                return 1.0 - (x - 3) / 2.0;
            else
                return 0.0;
        case Vidljivost::srednja:
            if (x > 3 && x <= 5)
                return (x - 3) / 2.0;
            else if (x > 5 && x <= 7)
                return 1.0;
            else if (x > 7 && x <= 9)
                return 1.0 - (x - 7) / 2.0;
            else
                return 0.0;
        case Vidljivost::visoka:
            if (x <= 7)
                return 0.0;
            else if (x > 7 && x <= 9)
                return (x - 7) / 2.0;
            else
                return 1.0;
    }
    return 0.0;
}

// Funkcije pripadnosti za udaljenost od vozila ispred
double pripadnostUdaljenosti(Udaljenost udaljenost, double x) 
{
    switch (udaljenost) 
    {
        case Udaljenost::blizu:
            if (x >= 0 && x <= 2)
                return 1.0;
            else if (x > 2 && x <= 5)
                return 1.0 - (x - 2) / 3.0;
            else
                return 0.0;
        case Udaljenost::umjereno:
            if (x > 2 && x <= 5)
                return (x - 2) / 3.0;
            else if (x > 5 && x <= 7)
                return 1.0;
            else if (x > 7 && x <= 10)
                return 1.0 - (x - 7) / 3.0;
            else
                return 0.0;
        case Udaljenost::daleko:
            if (x <= 7)
                return 0.0;
            else if (x > 7 && x <= 10)
                return (x - 7) / 3.0;
            else
                return 1.0;
    }
    return 0.0;
}

// Fuzzy pravila za određivanje brzine vožnje
Brzina odredi_brzinu(StanjePuta stanjePuta, Vidljivost vidljivost, Udaljenost udaljenost, Vrijeme vrijeme, Saobracaj saobracaj) {
    // Definisanje fuzzy pravila
    if ((stanjePuta == StanjePuta::klizav && vidljivost == Vidljivost::niska && udaljenost == Udaljenost::blizu) ||
        (stanjePuta == StanjePuta::klizav && vidljivost == Vidljivost::srednja && udaljenost == Udaljenost::blizu) ||
        (stanjePuta == StanjePuta::klizav && vidljivost == Vidljivost::niska && udaljenost == Udaljenost::umjereno) ||
        (vrijeme == Vrijeme::jakakisa && saobracaj == Saobracaj::guzva)) {
        return Brzina::sporo;
    } else if ((stanjePuta == StanjePuta::suh && vidljivost == Vidljivost::visoka && udaljenost == Udaljenost::daleko) ||
               (vrijeme == Vrijeme::suncano && saobracaj == Saobracaj::malosaobracaja)) {
        return Brzina::brzo;
    } else if ((stanjePuta == StanjePuta::suh && vidljivost == Vidljivost::srednja && udaljenost == Udaljenost::umjereno) ||
               (stanjePuta == StanjePuta::suh && vidljivost == Vidljivost::visoka && udaljenost == Udaljenost::daleko) ||
               (vrijeme == Vrijeme::suncano && saobracaj == Saobracaj::nemasaobracaja)) {
        return Brzina::umjereno;
    } else {
        return Brzina::umjereno;
    }
}
int main() 
{
    std::map<std::string, Vrijeme> vrijemeMap = {{"jaka kisa", Vrijeme::jakakisa}, {"magla", Vrijeme::magla}, {"suncano", Vrijeme::suncano}};
    std::map<std::string, Saobracaj> saobracajMap = {{"guzva", Saobracaj::guzva}, {"malo saobracaja", Saobracaj::malosaobracaja}, {"nema saobracaja", Saobracaj::nemasaobracaja}};
    std::map<std::string, StanjePuta> stanjePutaMap = {{"klizav", StanjePuta::klizav}, {"suh", StanjePuta::suh}};
    std::map<std::string, Vidljivost> vidljivostMap = {{"niska", Vidljivost::niska}, {"srednja", Vidljivost::srednja}, {"visoka", Vidljivost::visoka}};
    std::map<std::string, Udaljenost> udaljenostMap = {{"blizu", Udaljenost::blizu}, {"umjereno", Udaljenost::umjereno}, {"daleko", Udaljenost::daleko}};
    std::string vrijeme_str, saobracaj_str, stanjePuta_str, vidljivost_str, udaljenost_str;

    std::cout << "Unesite vremenske uslove (jaka kisa, magla, suncano): ";
    std::getline(std::cin, vrijeme_str);
    std::cout << "Unesite gustinu saobraćaja (guzva, malo saobracaja, nema saobracaja): ";
    std::getline(std::cin, saobracaj_str);
    std::cout << "Unesite stanje puta (klizav, suh): ";
    std::getline(std::cin, stanjePuta_str);
    std::cout << "Unesite vidljivost (niska, srednja, visoka): ";
    std::getline(std::cin, vidljivost_str);
    std::cout << "Unesite udaljenost od vozila ispred (blizu, umjereno, daleko): ";
    std::getline(std::cin, udaljenost_str);

    Vrijeme vrijeme = vrijemeMap[vrijeme_str];
    Saobracaj saobracaj = saobracajMap[saobracaj_str];
    StanjePuta stanjePuta = stanjePutaMap[stanjePuta_str];
    Vidljivost vidljivost = vidljivostMap[vidljivost_str];
    Udaljenost udaljenost = udaljenostMap[udaljenost_str];

    Brzina preporucenaBrzina = odredi_brzinu(stanjePuta, vidljivost, udaljenost, vrijeme, saobracaj);

    // Ispis preporučene brzine vožnje
    switch (preporucenaBrzina) {
        case Brzina::sporo:
            std::cout << "Preporucena brzina: sporo" << std::endl;
            break;
        case Brzina::umjereno:
            std::cout << "Preporucena brzina: umjereno" << std::endl;
            break;
        case Brzina::brzo:
            std::cout << "Preporucena brzina: brzo" << std::endl;
            break;
    }

    return 0;
}