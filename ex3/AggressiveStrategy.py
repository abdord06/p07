from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda card: card.cost)

        mana_available = 5
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        for card in sorted_hand:
            if mana_available >= card.cost:
                cards_played.append(card.name)
                mana_used += card.cost
                mana_available -= card.cost

                if hasattr(card, 'attack'):
                    damage_dealt += card.attack
                elif (hasattr(card, 'effect_type') and
                      card.effect_type == 'damage'):
                    damage_dealt += card.cost

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': self.prioritize_targets([]),
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        targets = []
        if available_targets:
            targets.extend(available_targets)
        targets.append('Enemy Player')
        return targets
