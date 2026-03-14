from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck - Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard(name="Fire Dragon",
                          cost=5, rarity="Legendary",
                          attack=7, health=5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print()

    mana_available = 6
    print(f"Playing {dragon.name} with {mana_available} mana available:")
    print(f"Playable: {dragon.is_playable(mana_available)}")
    if dragon.is_playable(mana_available):
        print(f"Play result: {dragon.play({})}")
    print()

    target_name = "Goblin Warrior"
    print(f"{dragon.name} attacks {target_name}:")
    print(f"Attack result: {dragon.attack_target(target_name)}")
    print()

    low_mana = 3
    print(f"Testing insufficient mana ({low_mana} available):")
    print(f"Playable: {dragon.is_playable(low_mana)}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
