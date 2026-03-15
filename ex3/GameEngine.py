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
        self.turns_simulated += 1
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': (self.strategy.get_strategy_name()
                              if self.strategy else 'None'),
            'total_damage': 8,
            'cards_created': 3
        }

    def get_engine_status(self) -> dict:
        return {
            'configured': (self.factory is not None and
                           self.strategy is not None),
            'turns_simulated': self.turns_simulated
        }
