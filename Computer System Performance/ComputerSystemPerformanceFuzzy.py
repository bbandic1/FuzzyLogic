# Membership function declaration
def cpu_usage_membership_function(cpu_usage):
    low = max(0.0, min(1.0, 1 - cpu_usage / 50.0))
    medium = max(0.0, min(1.0, 1 - abs(cpu_usage - 50) / 50.0))
    high = max(0.0, min(1.0, (cpu_usage - 50) / 50.0))
    return {'low': low, 'medium': medium, 'high': high}

def memory_usage_membership_function(memory_usage):
    low = max(0.0, min(1.0, 1 - memory_usage / 50.0))
    medium = max(0.0, min(1.0, 1 - abs(memory_usage - 50) / 50.0))
    high = max(0.0, min(1.0, (memory_usage - 50) / 50.0))
    return {'low': low, 'medium': medium, 'high': high}

# Fuzzification
def fuzzify_measurements(cpu_usage, memory_usage):
    cpu_fuzzy = cpu_usage_membership_function(cpu_usage)
    memory_fuzzy = memory_usage_membership_function(memory_usage)
    return cpu_fuzzy, memory_fuzzy

# Rule Evaluation
def rule_evaluation(cpu_fuzzy, memory_fuzzy):
    # Rules:
    # 1. If CPU usage is low and memory usage is low, then load is low.
    # 2. If CPU usage is low and memory usage is medium, then load is medium.
    # 3. If CPU usage is low and memory usage is high, then load is high.
    # 4. If CPU usage is medium and memory usage is low, then load is medium.
    # 5. If CPU usage is medium and memory usage is medium, then load is medium.
    # 6. If CPU usage is medium and memory usage is high, then load is high.
    # 7. If CPU usage is high and memory usage is low, then load is high.
    # 8. If CPU usage is high and memory usage is medium, then load is high.
    # 9. If CPU usage is high and memory usage is high, then load is high.

    load_low = min(cpu_fuzzy['low'], memory_fuzzy['low'])
    load_medium = max(
        min(cpu_fuzzy['low'], memory_fuzzy['medium']),
        min(cpu_fuzzy['medium'], memory_fuzzy['low']),
        min(cpu_fuzzy['medium'], memory_fuzzy['medium'])
    )
    load_high = max(
        min(cpu_fuzzy['low'], memory_fuzzy['high']),
        min(cpu_fuzzy['medium'], memory_fuzzy['high']),
        min(cpu_fuzzy['high'], memory_fuzzy['low']),
        min(cpu_fuzzy['high'], memory_fuzzy['medium']),
        cpu_fuzzy['high'], memory_fuzzy['high']
    )

    return {'Low': load_low, 'Medium': load_medium, 'High': load_high}

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
def assess_system_load(cpu_usage, memory_usage):
    # Fuzzification
    cpu_fuzzy, memory_fuzzy = fuzzify_measurements(cpu_usage, memory_usage)

    # Rule Evaluation
    results = rule_evaluation(cpu_fuzzy, memory_fuzzy)

    # Defuzzification
    load_assessment = defuzzify(results)

    return load_assessment

# User Input
def get_user_input():
    cpu_usage = float(input("Enter CPU usage percentage (0.0 to 100.0): "))
    while cpu_usage < 0.0 or cpu_usage > 100.0:
        print("Invalid input. Please enter a value between 0.0 and 100.0.")
        cpu_usage = float(input("Enter CPU usage percentage (0.0 to 100.0): "))

    memory_usage = float(input("Enter memory usage percentage (0.0 to 100.0): "))
    while memory_usage < 0.0 or memory_usage > 100.0:
        print("Invalid input. Please enter a value between 0.0 and 100.0.")
        memory_usage = float(input("Enter memory usage percentage (0.0 to 100.0): "))

    return cpu_usage, memory_usage

# Main function to execute the assessment
def main():
    cpu_usage, memory_usage = get_user_input()
    load_assessment = assess_system_load(cpu_usage, memory_usage)
    print(f"System Load Assessment: {load_assessment}")

if __name__ == "__main__":
    main()
