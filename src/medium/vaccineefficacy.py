participants = int(input())

vaccinated = 0
control = 0
infected_control_a = 0
infected_vaccinated_a = 0
infected_control_b = 0
infected_vaccinated_b = 0
infected_control_c = 0
infected_vaccinated_c = 0

for p in range(participants):
    record = input()
    v, a, b, c = list(record)

    if v == "N":
        control += 1
    else:
        vaccinated += 1

    if a == "Y":
        if v == "N":
            infected_control_a += 1
        else:
            infected_vaccinated_a += 1

    if b == "Y":
        if v == "N":
            infected_control_b += 1
        else:
            infected_vaccinated_b += 1

    if c == "Y":
        if v == "N":
            infected_control_c += 1
        else:
            infected_vaccinated_c += 1


def get_vaccine_efficacy(infected_vaccinated, vaccinated, infected_control, control):
    infection_rate_vaccinated = infected_vaccinated / vaccinated
    infection_rate_control = infected_control / control
    return 1 - infection_rate_vaccinated / infection_rate_control


vaccine_efficacy = [
    get_vaccine_efficacy(
        infected_vaccinated_a,
        vaccinated,
        infected_control_a,
        control,
    ),
    get_vaccine_efficacy(
        infected_vaccinated_b,
        vaccinated,
        infected_control_b,
        control,
    ),
    get_vaccine_efficacy(
        infected_vaccinated_c,
        vaccinated,
        infected_control_c,
        control,
    ),
]

for value in vaccine_efficacy:
    if value <= 0:
        print("Not Effective")
    else:
        print(f"{value*100:.6f}")
