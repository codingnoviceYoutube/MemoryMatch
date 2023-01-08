from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MemoryGame(GridLayout):
    def __init__(self, **kwargs):
        super(MemoryGame, self).__init__(**kwargs)
        self.cols = 4
        self.matched_cards = []
        self.first_card = None
        self.second_card = None

        # create a list of card values
        self.card_values = ["A", "B", "C", "D", "E", "F", "G", "H"] * 2
        self.card_back = "card_back.png"

        # shuffle the card values
        import random
        random.shuffle(self.card_values)

        # create the card buttons and add them to the grid
        for index, value in enumerate(self.card_values):
            button = Button(text="?", font_size=40, background_normal=self.card_back)
            button.bind(on_release=self.flip_card)
            self.add_widget(button)

    def flip_card(self, button):
        # get the index of the button in the grid layout
        index = self.children.index(button)
        # get the value of the card at that index
        value = self.card_values[index]

        # show the letter on the card
        button.text = value

        if not self.first_card:
            # if this is the first card, just store it and return
            self.first_card = (button, value)
            return

        # if this is the second card, store it and check for a match
        self.second_card = (button, value)

        # check if the cards match
        if self.first_card[1] == self.second_card[1]:
            # if the cards match, add them to the list of matched cards
            self.matched_cards.append(self.first_card[0])
            self.matched_cards.append(self.second_card[0])

            # check if all the cards have been matched
            if len(self.matched_cards) == len(self.card_values):
                # if all the cards have been matched, the player has won
                print("You win!")
        else:
            # if the cards don't match, flip them back over after a short delay
            import time
            time.sleep(0.5)
            self.first_card[0].text = "?"
            self.first_card[0].background_normal = self.card_back
            self.second_card[0].text = "?"
            self.second_card[0].background_normal = self.card_back

        # reset the first and second cards
        self.first_card = None
        self.second_card = None


class MemoryMatchApp(App):
    def build(self):
        return MemoryGame()


if __name__ == "__main__":
    MemoryMatchApp().run()
