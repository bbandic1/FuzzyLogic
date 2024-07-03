# System Load Assessment

## Overview

This Python script uses fuzzy logic to assess the system load based on CPU and memory usage percentages provided by the user.

## Functions

### Membership Function Declaration

#### `cpu_usage_membership_function(cpu_usage)`

Defines membership values for CPU usage levels (`low`, `medium`, `high`).

#### `memory_usage_membership_function(memory_usage)`

Defines membership values for memory usage levels (`low`, `medium`, `high`).

### Fuzzification

#### `fuzzify_measurements(cpu_usage, memory_usage)`

Fuzzifies CPU and memory usage measurements using membership functions.

### Rule Evaluation

#### `rule_evaluation(cpu_fuzzy, memory_fuzzy)`

Evaluates rules to determine the system load (`Low`, `Medium`, `High`) based on fuzzy inputs of CPU and memory usage.

### Defuzzification

#### `defuzzify(results)`

Defuzzifies the results to determine the assessed system load.

### Main Functions

#### `assess_system_load(cpu_usage, memory_usage)`

Coordinates the fuzzification, rule evaluation, and defuzzification processes to assess the system load.

#### `get_user_input()`

Handles user input for CPU and memory usage percentages.

#### `main()`

Main function to execute the system load assessment process using user input.

## Execution

To assess system load:
1. Run the script.
2. Enter the CPU usage percentage (between `0.0` and `100.0`).
3. Enter the memory usage percentage (between `0.0` and `100.0`).
4. The script will output the assessed system load (`Low`, `Medium`, `High`).

## Usage

This script can be used for monitoring and managing system resources dynamically based on current CPU and memory usage levels using fuzzy logic.

