from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


def main():
    print("\n=== DataDeck - Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {type(strategy).__name__}")
    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")

    hand = [
        CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
        CreatureCard("Goblin Warrior", 2, "Common", 5, 2),
        SpellCard("Lightning Bolt", 3, "Common", "damage")
    ]

    hand_display = ", ".join([f"{card.name} ({card.cost})" for card in hand])
    print(f"Hand: [{hand_display}]")
    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")

    actions = strategy.execute_turn(hand, [])
    print(f"Actions: {actions}\n")

    print("Game Report:")
    print(engine.simulate_turn())
    print("\nAbstract Factory + Strategy Pattern:"
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
