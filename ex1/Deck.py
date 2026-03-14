import random
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop()
        return None

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        creatures = sum(1 for c in self.cards
                        if type(c).__name__ == 'CreatureCard')
        spells = sum(1 for c in self.cards
                     if type(c).__name__ == 'SpellCard')
        artifacts = sum(1 for c in self.cards
                        if type(c).__name__ == 'ArtifactCard')

        avg_cost = (sum(c.cost for c in self.cards) /
                    total_cards if total_cards > 0 else 0.0)

        return {
            'total_cards': total_cards,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': round(avg_cost, 1)
        }
