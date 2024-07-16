# Fuzzy Logic for Driving Speed Recommendation

## Overview

This C++ program utilizes fuzzy logic to recommend driving speed based on various environmental and traffic conditions. It defines linguistic variables and membership functions for conditions like weather, traffic density, road state, visibility, and distance from the vehicle ahead. The program then uses fuzzy rules to determine a recommended driving speed.

## Linguistic Variables and Membership Functions

### Weather Conditions

- **Strong Rain**: Membership function `pripadnostVremenu(Vrijeme::jakakisa, x)`
- **Fog**: Membership function `pripadnostVremenu(Vrijeme::magla, x)`
- **Sunny**: Membership function `pripadnostVremenu(Vrijeme::suncano, x)`

### Traffic Density

- **Heavy Traffic**: Membership function `pripadnostSaobracaju(Saobracaj::guzva, x)`
- **Light Traffic**: Membership function `pripadnostSaobracaju(Saobracaj::malosaobracaja, x)`
- **No Traffic**: Membership function `pripadnostSaobracaju(Saobracaj::nemasaobracaja, x)`

### Road State

- **Slippery**: Membership function `pripadnostStanjuPuta(StanjePuta::klizav, x)`
- **Dry**: Membership function `pripadnostStanjuPuta(StanjePuta::suh, x)`

### Visibility

- **Low**: Membership function `pripadnostVidljivosti(Vidljivost::niska, x)`
- **Medium**: Membership function `pripadnostVidljivosti(Vidljivost::srednja, x)`
- **High**: Membership function `pripadnostVidljivosti(Vidljivost::visoka, x)`

### Distance from Vehicle Ahead

- **Close**: Membership function `pripadnostUdaljenosti(Udaljenost::blizu, x)`
- **Moderate**: Membership function `pripadnostUdaljenosti(Udaljenost::umjereno, x)`
- **Far**: Membership function `pripadnostUdaljenosti(Udaljenost::daleko, x)`

## Speed Determination Rules

The program applies fuzzy rules based on the above conditions to determine the recommended driving speed.

## Execution

To use the program:
1. Compile and run the C++ file.
2. Enter the environmental and traffic conditions as prompted.
3. The program will output the recommended driving speed (sporo, umjereno, brzo).

##Usage

This program can serve as a foundation for developing advanced driving assistance systems using fuzzy logic.