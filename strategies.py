class TitForTat:
    """A strategy that cooperates initially and then mimics the opponent's last move.

        Returns:
            str: 'C' for cooperate, 'D' for defect.
    """

    def choose_move(self, own_history, enemy_history):
        return 'C' if not enemy_history else enemy_history[-1]

class AlwaysCooperate:
    """A strategy that always cooperates, regardless of the opponent's behavior."""

    def choose_move(self, own_history, enemy_history):
        return 'C'

class AlwaysDefect:
    """A strategy that always defects, never cooperating."""

    def choose_move(self, own_history, enemy_history):
        return 'D'

class RandomBuster:
    """A strategy that randomly chooses between cooperation and defection."""

    def choose_move(self, own_history, enemy_history):
        import random
        return random.choice(['C', 'D'])

class GrimTrigger:
    """A strategy that cooperates until the opponent defects, then always defects forever."""

    def choose_move(self, own_history, enemy_history):
        return 'C' if 'D' not in enemy_history else 'D'
    

# User Can Write their Own Strategy Class down below, Just Make Sure The Output Is Either 'C' or 'D' 

class CustomStrategy:
        def choose_move(self, own_history: list, enemy_history: list) -> str:
            # Implement your logic here
            pass