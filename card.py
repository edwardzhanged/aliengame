import random
class blackjack:
    def __init__(self, number_picks, decision):
        self.number_picks = number_picks
        self.value=value
    def pick_cards(self):
        cards=['a','a','a','a','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5',
               '5','6','6','6','6','7','7','7','7','8','8','8','8','9',
               '9','9','9','10','10','10','10','j','j','j','j','q','q','q','q','k','k','k','k']
        number=self.number_picks
        cards_picked = []
        for n in range(number):
            ran_position =random.randint(1, len(cards))
            cards_picked.append(cards[ran_position])
            del cards[ran_position]
        return cards_picked,cards
        global  cards_picked,cards
    def get_value(self):
        value=[]
        for m in self.number_picks:
            if cards_picked[m]=='j'or'q'or'k':
                value_transfer=10
                value.append(value_transfer)
            elif cards_picked[m]=='2'or'3'or'4'or'5'or'6'or'7'or'8'or'9'or'10':
                value_transfer=int(cards_picked[m])
                value.append(value_transfer)
            elif cards_picked[m]=='a':
                if self.decision=='1':
                  value_transfer=1
                  value.append(value_transfer)
                elif self.decision=='11':
                    value_transfer=11
                    value.append(value_transfer)
        return value
                    
