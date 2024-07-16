#include <iostream>
#include <cmath>
#include <algorithm>


/* Radi jednostavnosti cemo za defuzzyfikaciju koristiti metod MOM, 
tj uzimacemo da je reprezentativni elemenat cijelog fuzzy
skupa onaj elemenat koji ima najveci stepen pripadnosti skupu */

//defeinramo funkcije pripadnosti za lingvisticku varijablu zadace
class Zadace{
    public:
    static double Los(double x);
    static double Dobar(double x);
    static double Natprosjecan(double x);
};

double Zadace::Los(double x){
    if(x<=5) return 1;
    else if(x>5 && x<=10) return  -x/5+2;
    return 0;
}

double Zadace::Dobar(double x){
    if(x<15 && x>=10) return -x/5+2;
    if(x>5 && x<10) return x/5-1;
    return 0;
}

double Zadace::Natprosjecan(double x){
    if(x>=17) return 1;
    if(x>15 && x<17)  return x/2-7.5;
    return 0;
}

//funkcije pripadnosti za varijablu ispiti
class Ispiti{
    public:
    static double Dobar(double x);
    static double Los(double x);
};

double Ispiti::Dobar(double x){
    if(x>=25) return 1;
    if(x>20 && x<25) return x/5-4;
    return 0;

}

double Ispiti::Los(double x){
    if(x>0 && x <20) return 1;
    if(x>=20 && x<=25) return -x/5+5;
    return 0;
}


//izlazne funkcije
class UsmeniDaNeMozda{
    public:
    /*prvi parametar funkcija se biti vrijednost argumenta,
    kao drugi parametar izlaznim funkcijama pripadnosti cemo 
    slati vrijednost koju dobijemo it DOF-ova, 
    kako bismo mogli u hodu modificirati funkcije
    tj. primijeniti Mamdami implikacioni operator na izlazne funkcije*/
    static double Popravni(double x,double minimum);
    static double Usmeni(double x, double minimum);
    static double UsmeniSaZadacima(double x, double minimum);
};
 
/*u hodu prilagodjavamo izalzne funkcije
(implmenmtiramo Mamdani implikacioni operator)*/
double UsmeniDaNeMozda::Popravni(double x,double m){
    if(x>=0 && x<=20) return m; 
    // posto je u ovom intervalu vrijednost funkcije 1, 
    //to ce minimum biti vrijednost m
    if(x>20 && x<25) return std::min(-x/5+5, m);
    return 0; 
    //u ovom slucaju kakvu god vrijednost m imamo minimalna vrj ce biti 0
}

double UsmeniDaNeMozda::Usmeni(double x, double m){
    if(x>50) return m; 
    if(x>=35 && x<=50) return std::min(x/15 - 2.333,m);
    return 0;
}

double UsmeniDaNeMozda::UsmeniSaZadacima(double x, double m){
    if(x>=25 && x<=35) return std::min(x/5-4,m);
    if(x>=35 && x<=50) return std::min(-x/5+6,m);
    return 0;
}


int main(){
    double BodoviNaIspitima, BodoviZadace;
    std::cout<<"\nUnesite broj bodova koje je student ostvario na zadacama:";
    std::cin>>BodoviZadace;
    std::cout<<"\nUnesite broj bodova koje je student ostvario na ispitima: ";
    std::cin>>BodoviNaIspitima;
    
      //izracun vrijednosti funkcija pripradnosti za ulazne podatke
    double dobar_zadace= Zadace::Dobar(BodoviZadace);
    double los_zadace=Zadace::Los(BodoviZadace);
    double natprosjecan_zadace=Zadace::Natprosjecan(BodoviZadace);

    double dobar_ispiti=Ispiti::Dobar(BodoviNaIspitima);
    double los_ispiti=Ispiti::Los(BodoviNaIspitima);
    
    /*ispisujemo stanje rada studenta na kursu modelirano kao 
    fuzzy skupovi Ispiti i Zadace */
    std::cout<<"\nStanje rada studenta na kursu: ";
    std::cout<<"\n Ispiti: "<<dobar_ispiti<<"/dobar + "<<los_ispiti<<"/los";
    std::cout<<"\nZadace: "<<dobar_zadace<<" /dobar + "<<
    los_zadace<<"/los + "<<natprosjecan_zadace<<"/natprosjecan";
    
    
    //sada pravimo DOF-ove
    //posto radimo Mamdani postupak, t-norma je min(x,y)
    double DOF1=std::min(dobar_zadace,dobar_ispiti);
    double DOF2=std::min(dobar_zadace,los_ispiti);
    double DOF3=std::min(los_zadace,dobar_ispiti);
    double DOF4=std::min(los_zadace,los_ispiti);
    double DOF5=std::min(natprosjecan_zadace,dobar_ispiti);
    double DOF6=std::min(natprosjecan_zadace,los_ispiti);

    //sada trazimo na koje izalzne funkcije uticu proracunati DOF-ovi
    /*primjenjujemo mamdani implikacioni operator,
    tj. modeliramo izlazne funkcije shodno dobivenim vrjednostima DOF-ova
    - kada pogledmao navedena ITE pravila u tabeli, 
    trebat cemo pronaci 6 mogucih izlaznih kombinacija 
    - posto koristimo metod MOM za defuzzyfikaciju, 
    jednostavno cemo provjeravati za koje vrijednosti ulaznih parametara 
    izlazne funkcije daju najvecu vrijednost, 
    zatim cemo te vrijednosti uporediti s ciljem dobivanja konacnog rezultata */
    
    //shodno pravilima iz tabele dobivamo sljedece moguce kombinacije:
    double usmeni1=UsmeniDaNeMozda::Popravni(BodoviZadace+BodoviNaIspitima, DOF1);
   
   double usmenisazadacima=UsmeniDaNeMozda::UsmeniSaZadacima(BodoviNaIspitima+
   BodoviZadace, DOF2);
    
   double popravni1=UsmeniDaNeMozda::Popravni(BodoviNaIspitima+ BodoviZadace, DOF3);
   
   double popravni2=UsmeniDaNeMozda::Popravni(BodoviNaIspitima+ BodoviZadace, DOF4); 
   
   double usmeni2 = UsmeniDaNeMozda::Popravni(BodoviZadace+BodoviNaIspitima, DOF5);
   
   double usmenisazadacima2= UsmeniDaNeMozda::UsmeniSaZadacima(BodoviNaIspitima+
   BodoviZadace,DOF6);

    //sada metodom MOM trazimo reprezanetativni elemat za sve fuzzy skupove
        double max_value = std::max({ usmeni1, usmenisazadacima, 
        popravni1, popravni2, usmeni2, usmenisazadacima2 });

    if (max_value == usmeni1 || max_value == usmeni2)
        std::cout << "\nStudent je ostvario pravo izlaska na usmeni ispit!";
    else if (max_value == popravni1 || max_value == popravni2)
        std::cout << "\nStudent nije ostvario pravo izlaska na usmeni ispit";
    else
    std::cout << "\nStudent je ostvario pravo da izadje na usmeni ispit, ali ce se za njega usmeni ispit sastojati i od radjenja zadataka!";
    
    return 0;
}