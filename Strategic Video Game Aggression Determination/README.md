# Fuzzy Logic-Based Aggression Level Determination

## Overview

This Python script implements a fuzzy logic system to determine the aggression level of an enemy based on distance and armament. The system uses fuzzy rules and membership functions to infer the level of aggression.

## Functions

### Membership Functions

#### `dajTrougaoVrijednosti(x, a, b, c)`

Calculates the membership value for a triangular membership function.

#### `dajTrapezVrijednosti(x, a, b, c, d)`

Calculates the membership value for a trapezoidal membership function.

### Fuzzy Class

#### `class Fuzzy`

A class that encapsulates the fuzzy logic system, including inputs, outputs, and inference rules.

#### `napraviUlaznuFunkciju(ime)`

Creates an input membership function.

#### `napraviIzlaznuFunkciju(ime)`

Creates an output membership function.

#### `dodajFunkcijuPripadnostiUlazi(ime, opis, a, b, c, d=None)`

Adds a membership function for an input variable.

#### `dodajFunkcijuPripadnostiIzlazi(ime, opis, a, b, c, d=None)`

Adds a membership function for an output variable.

#### `definisiPravilo(broj, vrijednost1, vrijednost2, vrijednostIzlaza)`

Defines an inference rule.

#### `dajYVrijednosti(ime, opis, xmin, xmax, num_points=1000)`

Returns the y-values of a membership function for plotting.

#### `dajYzaSveFunkcijePripadnosti(ime, x)`

Returns the y-values for all membership functions of an input variable.

#### `izracunajDOF(x, y, opis1, opis2)`

Calculates the degree of fulfillment for a given rule.

#### `spajanje(spojeniUlaz, trenutniIzlaz)`

Combines the current output with the aggregated output.

#### `mamdaniImplikacija(dof, pripadnost)`

Applies the Mamdani implication method.

#### `defuzzifikacijaCOS(spojeniIzlaz, xVrijednost)`

Performs defuzzification using the center of sums method.

#### `zakljuci(x, y)`

Infers the output based on the input values.

## Execution

To determine the aggression level:
1. Run the script.
2. Enter the distance to the enemy (in blocks).
3. Enter the number of troops.
4. The script will output the aggression level.

## Usage

This script can be used for simulating enemy behavior in strategic video games or for educational purposes to demonstrate fuzzy logic applications.

