from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, defense_power: int, initial_rating: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.rating = initial_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card deployed'
        }

    def attack(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(self.defense_power, incoming_damage)
        damage_taken = incoming_damage - damage_blocked

        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        return {'attack': self.attack_power, 'defense': self.defense_power}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {'rating': self.rating,
                'wins': self.wins,
                'losses': self.losses}

    def get_tournament_stats(self) -> dict:
        return {
            'name': self.name,
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }
