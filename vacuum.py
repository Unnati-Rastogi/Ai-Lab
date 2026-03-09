
def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

environment = {}

environment["A"] = input("Enter status of location A (Dirty/Clean): ")
environment["B"] = input("Enter status of location B (Dirty/Clean): ")


location = input("Enter initial location of vacuum (A/B): ")


for step in range(5):
    status = environment[location]

    action = reflex_vacuum_agent(location, status)

    print("\nStep:", step + 1)
    print("Location:", location)
    print("Status:", status)
    print("Action:", action)

    # Update environment
    if action == "Suck":
        environment[location] = "Clean"

    elif action == "Right":
        location = "B"

    elif action == "Left":
        location = "A"