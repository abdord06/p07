from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {}

        self.turns_simulated += 1

        hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("lightning")
        ]

        turn_result = self.strategy.execute_turn(hand, [])

        total_damage = turn_result.get('damage_dealt', 0)

        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': total_damage,
            'cards_created': len(hand)
        }

    def get_engine_status(self) -> dict:
        return {
            'configured': (self.factory is not None and
                           self.strategy is not None),
            'turns_simulated': self.turns_simulated
        }
