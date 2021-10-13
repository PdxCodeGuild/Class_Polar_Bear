super_heros = {
    'Batman': 1
}
# {heroname: 200}

while True:
    hero = input("Ente a super hero: ")

    if hero in super_heros:
        super_heros[hero] += 1
    else:
        super_heros[hero] = 1

    print(super_heros)