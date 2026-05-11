my_loves = {
    "Arthur morgan": 36,
    "Artyom":24,
    "Cj":24,
    "Edward":12,
    "Carl Grimes":7
}

for name , age in my_loves.items():
    if age >= 18:
        print(f"{name} is adult")