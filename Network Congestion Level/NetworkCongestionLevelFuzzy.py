# Membership function declaration
def delay_membership_function(delay):
    low = max(0.0, min(1.0, 1 - delay / 50.0))
    medium = max(0.0, min(1.0, 1 - abs(delay - 50) / 50.0))
    high = max(0.0, min(1.0, (delay - 50) / 50.0))
    return {'low': low, 'medium': medium, 'high': high}

def packet_loss_membership_function(packet_loss):
    low = max(0.0, min(1.0, 1 - packet_loss / 5.0))
    medium = max(0.0, min(1.0, 1 - abs(packet_loss - 5) / 5.0))
    high = max(0.0, min(1.0, (packet_loss - 5) / 5.0))
    return {'low': low, 'medium': medium, 'high': high}

# Fuzzification
def fuzzify_measurements(delay, packet_loss):
    delay_fuzzy = delay_membership_function(delay)
    packet_loss_fuzzy = packet_loss_membership_function(packet_loss)
    return delay_fuzzy, packet_loss_fuzzy

# Rule Evaluation
def rule_evaluation(delay_fuzzy, packet_loss_fuzzy):
    # Rules:
    # 1. If delay is low and packet loss is low, then congestion is low.
    # 2. If delay is low and packet loss is medium, then congestion is medium.
    # 3. If delay is low and packet loss is high, then congestion is high.
    # 4. If delay is medium and packet loss is low, then congestion is medium.
    # 5. If delay is medium and packet loss is medium, then congestion is medium.
    # 6. If delay is medium and packet loss is high, then congestion is high.
    # 7. If delay is high and packet loss is low, then congestion is high.
    # 8. If delay is high and packet loss is medium, then congestion is high.
    # 9. If delay is high and packet loss is high, then congestion is high.

    congestion_low = min(delay_fuzzy['low'], packet_loss_fuzzy['low'])
    congestion_medium = max(
        min(delay_fuzzy['low'], packet_loss_fuzzy['medium']),
        min(delay_fuzzy['medium'], packet_loss_fuzzy['low']),
        min(delay_fuzzy['medium'], packet_loss_fuzzy['medium'])
    )
    congestion_high = max(
        min(delay_fuzzy['low'], packet_loss_fuzzy['high']),
        min(delay_fuzzy['medium'], packet_loss_fuzzy['high']),
        min(delay_fuzzy['high'], packet_loss_fuzzy['low']),
        min(delay_fuzzy['high'], packet_loss_fuzzy['medium']),
        delay_fuzzy['high'], packet_loss_fuzzy['high']
    )

    return {'Low': congestion_low, 'Medium': congestion_medium, 'High': congestion_high}

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
def assess_network_congestion(delay, packet_loss):
    # Fuzzification
    delay_fuzzy, packet_loss_fuzzy = fuzzify_measurements(delay, packet_loss)

    # Rule Evaluation
    results = rule_evaluation(delay_fuzzy, packet_loss_fuzzy)

    # Defuzzification
    congestion_assessment = defuzzify(results)

    return congestion_assessment

# User Input
def get_user_input():
    delay = float(input("Enter network delay (0.0 to 100.0 ms): "))
    while delay < 0.0 or delay > 100.0:
        print("Invalid input. Please enter a value between 0.0 and 100.0.")
        delay = float(input("Enter network delay (0.0 to 100.0 ms): "))

    packet_loss = float(input("Enter packet loss percentage (0.0 to 10.0%): "))
    while packet_loss < 0.0 or packet_loss > 10.0:
        print("Invalid input. Please enter a value between 0.0 and 10.0.")
        packet_loss = float(input("Enter packet loss percentage (0.0 to 10.0%): "))

    return delay, packet_loss

# Main function to execute the assessment
def main():
    delay, packet_loss = get_user_input()
    congestion_assessment = assess_network_congestion(delay, packet_loss)
    print(f"Network Congestion Assessment: {congestion_assessment}")

if __name__ == "__main__":
    main()
