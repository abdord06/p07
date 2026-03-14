from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck - Deck Builder ===")
    print("Building deck with different card types...")
    deck = Deck()

    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(ArtifactCard("Mana Crystal", 2,
                               "Rare", 10, "+1 mana per turn"))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))

    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:")

    for _ in range(3):
        card = deck.draw_card()
        if card:
            card_type_name = type(card).__name__.replace('Card', '')
            print(f"Drew: {card.name} ({card_type_name})")
            print(f"Play result: {card.play({})}")
            print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
