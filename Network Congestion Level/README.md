# Network Congestion Assessment

## Overview

This Python script uses fuzzy logic to assess network congestion based on delay (in milliseconds) and packet loss percentage provided by the user.

## Functions

### Membership Function Declaration

#### `delay_membership_function(delay)`

Defines membership values for delay levels (`low`, `medium`, `high`).

#### `packet_loss_membership_function(packet_loss)`

Defines membership values for packet loss levels (`low`, `medium`, `high`).

### Fuzzification

#### `fuzzify_measurements(delay, packet_loss)`

Fuzzifies delay and packet loss measurements using their respective membership functions.

### Rule Evaluation

#### `rule_evaluation(delay_fuzzy, packet_loss_fuzzy)`

Evaluates rules to determine network congestion levels (`Low`, `Medium`, `High`) based on fuzzy inputs of delay and packet loss.

### Defuzzification

#### `defuzzify(results)`

Defuzzifies the results to determine the assessed network congestion level.

### Main Functions

#### `assess_network_congestion(delay, packet_loss)`

Coordinates the fuzzification, rule evaluation, and defuzzification processes to assess network congestion.

#### `get_user_input()`

Handles user input for network delay (in milliseconds) and packet loss percentage.

#### `main()`

Main function to execute the network congestion assessment process using user input.

## Execution

To assess network congestion:
1. Run the script.
2. Enter the network delay (between `0.0` and `100.0` milliseconds).
3. Enter the packet loss percentage (between `0.0` and `10.0`).
4. The script will output the assessed network congestion level (`Low`, `Medium`, `High`).

## Usage

This script can be used for real-time monitoring and management of network congestion based on current delay and packet loss conditions using fuzzy logic.

