# A Prerequisite for The Oral Exam - Programming Techniques

## Overview

This C++ program utilizes fuzzy logic to determine whether a student has met the prerequisites to take an oral exam based on their scores in assignments and exams. The decision is made by fuzzifying the input scores, applying rules, and defuzzifying the results using the Method of Maximum (MOM).

## Classes and Functions

### Membership Function Declarations

#### class Zadace

Defines membership functions for the linguistic variable "assignments."

##### static double Los(double x)

Returns the membership degree for "poor" assignment scores.

##### static double Dobar(double x)

Returns the membership degree for "good" assignment scores.

##### static double Natprosjecan(double x)

Returns the membership degree for "above average" assignment scores.

#### class Ispiti

Defines membership functions for the linguistic variable "exams."

##### static double Dobar(double x)

Returns the membership degree for "good" exam scores.

##### static double Los(double x)

Returns the membership degree for "poor" exam scores.

### Output Functions

#### class UsmeniDaNeMozda

Defines the output functions for the decision on whether the student can take the oral exam, needs to retake the exam, or can take the oral exam with additional tasks.

##### static double Popravni(double x, double minimum)

Returns the degree to which the student needs to retake the exam.

##### static double Usmeni(double x, double minimum)

Returns the degree to which the student can take the oral exam.

##### static double UsmeniSaZadacima(double x, double minimum)

Returns the degree to which the student can take the oral exam with additional tasks.

### Main Functions

#### int main()

The main function coordinates the entire process:

- **Input**: Reads the number of points the student scored on assignments and exams.
- **Fuzzification**: Calculates membership values for the input scores.
- **Rule Evaluation**: Applies fuzzy logic rules to determine the Degrees of Fulfillment (DOF).
- **Defuzzification**: Uses the Method of Maximum (MOM) to make the final decision based on the highest membership value from the output functions.

## Usage

This program can be used as a basis for developing more complex educational assessment systems using fuzzy logic.
