"""Calculating the value of cards in Blackjack"""

def value_of_card(card):
    """Return the Blackjack value of a single card."""
    if card in 'JQK':
        return 10
    if card == 'A':
        return 1
    if card.isdigit() and 2 <= int(card) <= 10:
        return int(card)
    return 0

def higher_card(card_one, card_two):
    """Return the card with the higher value, or both if tied."""
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)

    if val_one > val_two:
        return card_one
    if val_one == val_two:
        return (card_one, card_two)
    return card_two

def value_of_ace(card_one, card_two):
    """Return the value of an Ace given the other card."""
    # If one card is Ace, always return 1
    if card_one == 'A' or card_two == 'A':
        return 1

    # Otherwise, choose 11 if it doesn't bust
    total = value_of_card(card_one) + value_of_card(card_two)
    return 11 if total + 11 <= 21 else 1


def is_blackjack(card_one, card_two):
    """Return True if the two cards make a Blackjack, else False."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total == 21 or (total + 10 == 21 and ('A' in (card_one, card_two)))

def can_split_pairs(card_one, card_two):
    """Return True if the two cards can be split (same value)."""
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Return True if the total value allows doubling down (9, 10, 11)."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total <= 11
