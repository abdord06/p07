from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = 'Spell'

    def play(self, game_state: dict) -> dict:
        effect_desc = (f"Deal {self.cost} damage to target"
                       if self.effect_type == "damage" else
                       f"Cast {self.effect_type} spell")
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effect_desc
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'resolved': True,
            'targets_affected': targets
        }
