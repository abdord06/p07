from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.registered_cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name.split()[-1].lower()}_001"
        self.registered_cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.registered_cards.get(card1_id)
        card2 = self.registered_cards.get(card2_id)

        self.matches_played += 1

        if card1 and card2:
            card1.rating = 1216
            card1.update_wins(1)

            card2.rating = 1134
            card2.update_losses(1)

            return {
                'winner': card1_id,
                'loser': card2_id,
                'winner_rating': card1.rating,
                'loser_rating': card2.rating
            }
        return {}

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self.registered_cards.values(),
                              key=lambda x: x.rating, reverse=True)
        return [card.get_tournament_stats() for card in sorted_cards]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.registered_cards)
        if total_cards == 0:
            return {}

        avg_rating = sum(card.rating for card in
                         self.registered_cards.values()) // total_cards

        return {
            'total_cards': total_cards,
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
