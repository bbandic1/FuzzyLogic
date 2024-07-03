# Membership function declaration
def spin_membership_function(spin):
    if spin == 'up':
        return {'up': 1.0, 'down': 0.0, 'superposition': 0.0}
    elif spin == 'down':
        return {'up': 0.0, 'down': 1.0, 'superposition': 0.0}
    else:
        return {'up': 0.5, 'down': 0.5, 'superposition': 1.0}

def energy_membership_function(energy):
    low = max(0.0, min(1.0, 1 - energy/5.0))
    medium = max(0.0, min(1.0, 1 - abs(energy - 5)/5.0))
    high = max(0.0, min(1.0, (energy - 5)/5.0))
    return {'low': low, 'medium': medium, 'high': high}

# Fuzzification
def fuzzify_measurements(spin, energy):
    spin_fuzzy = spin_membership_function(spin)
    energy_fuzzy = energy_membership_function(energy)
    return spin_fuzzy, energy_fuzzy

# Rule Evaluation
def rule_evaluation(spin_fuzzy, energy_fuzzy):
    # Rules:
    # 1. If spin is up and energy is low, then state is |0⟩
    # 2. If spin is down and energy is low, then state is |1⟩
    # 3. If spin is superposition and energy is medium, then state is a superposition
    # 4. If spin is up and energy is high, then state is |1⟩
    # 5. If spin is down and energy is high, then state is |0⟩
    # 6. If spin is up and energy is medium, then state is a superposition
    # 7. If spin is down and energy is medium, then state is a superposition
    # 8. If spin is superposition and energy is low, then state is a superposition
    # 9. If spin is superposition and energy is high, then state is a superposition

    state_0 = max(min(spin_fuzzy['up'], energy_fuzzy['low']),
                  min(spin_fuzzy['down'], energy_fuzzy['high']))
    state_1 = max(min(spin_fuzzy['down'], energy_fuzzy['low']),
                  min(spin_fuzzy['up'], energy_fuzzy['high']))
    superposition = max(min(spin_fuzzy['superposition'], energy_fuzzy['medium']),
                        min(spin_fuzzy['up'], energy_fuzzy['medium']),
                        min(spin_fuzzy['down'], energy_fuzzy['medium']),
                        min(spin_fuzzy['superposition'], energy_fuzzy['low']),
                        min(spin_fuzzy['superposition'], energy_fuzzy['high']))

    return {'|0⟩': state_0, '|1⟩': state_1, 'Superposition': superposition}

# Defuzzification
def defuzzify(results):
    max_state = max(results, key=results.get)
    membership_value = results[max_state]

    if membership_value > 0.7:
        return max_state
    elif 0.3 < membership_value <= 0.7:
        return f"{max_state} (uncertain)"
    else:
        return 'Uncertain'

# Main Function
def classify_quantum_state(spin, energy):

    # Fuzzification
    spin_fuzzy, energy_fuzzy = fuzzify_measurements(spin, energy)

    # Rule Evaluation
    results = rule_evaluation(spin_fuzzy, energy_fuzzy)

    # Defuzzification
    classified_state = defuzzify(results)

    return classified_state

# User Input
def get_user_input():
    spin_measurement = input("Enter spin state (up, down, superposition): ").lower()
    while spin_measurement not in ['up', 'down', 'superposition']:
        print("Invalid input. Please enter 'up', 'down', or 'superposition'.")
        spin_measurement = input("Enter spin state (up, down, superposition): ").lower()

    energy_measurement = float(input("Enter energy measurement (0.0 to 10.0): "))
    while energy_measurement < 0.0 or energy_measurement > 10.0:
        print("Invalid input. Please enter a value between 0.0 and 10.0.")
        energy_measurement = float(input("Enter energy measurement (0.0 to 10.0): "))

    return spin_measurement, energy_measurement


# Main function to execute the classification
def main():
    spin_measurement, energy_measurement = get_user_input()
    classified_state = classify_quantum_state(spin_measurement, energy_measurement)
    print(f"Classified Quantum State: {classified_state}")

if __name__ == "__main__":
    main()