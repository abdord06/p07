from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main():
    print("\n=== DataDeck - Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 4, 3, 1150)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card, cid in [(dragon, dragon_id), (wizard, wizard_id)]:
        print(f"{card.name} (ID: {cid}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}\n")

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['name']} - Rating: "
              f"{entry['rating']} ({entry['record']})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
