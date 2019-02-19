import random

class blackjack:
    global cards
    global cards_picked
    def __init__(self, number_picks,decision):
        self.number_picks = number_picks
        self.decision=decision
    def get_value(self):
        cards=['a','a','a','a','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5',
               '5','6','6','6','6','7','7','7','7','8','8','8','8','9',
               '9','9','9','10','10','10','10','j','j','j','j','q','q','q','q','k','k','k','k']
        number=self.number_picks
        cards_picked = []
        for n in range(number):
            ran_position =random.randint(1, len(cards))
            cards_picked.append(cards[ran_position])
            del cards[ran_position]
        print(cards_picked)
        value=[]
        for m in range(self.number_picks):
            if cards_picked[m]=='j' or cards_picked[m]=='q' or cards_picked[m]=='k':
                a=cards_picked[m]
                value_transfer=10
                value.append(value_transfer)
            elif cards_picked[m]=='2'or cards_picked[m]=='3'or cards_picked[m]=='4' or cards_picked[m]=='5'or cards_picked[m]=='6'or \
                    cards_picked[m]=='7'or cards_picked[m]=='8'or cards_picked[m]=='9'or cards_picked[m]=='10':
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

a=blackjack(4,'1')
print(a.get_value())
