import argparse
import importlib
import logging
from typing import Tuple, List, Any

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def import_strategy(strategy_arg: str) -> Any:
    """
    Dynamically imports and instantiates a strategy class based on a string argument.
    If the argument contains a dot ('.'), it is assumed to be in the form "module.ClassName";
    otherwise, it imports the class from the default 'strategies' module.

    Args:
        strategy_arg (str): A string in the format "module.ClassName" or "ClassName".

    Returns:
        Any: An instance of the specified strategy class.

    Raises:
        ValueError: If the strategy argument is invalid or the module/class cannot be found.
    """

    try:
        if '.' in strategy_arg:
            module_name, class_name = strategy_arg.rsplit('.', 1)
            module = importlib.import_module(module_name)
        else:
            class_name = strategy_arg
            module = importlib.import_module("strategies")

        strategy_instance = getattr(module, class_name)()
        logging.info(f"Successfully imported strategy: {strategy_arg}")
        return strategy_instance
        
    except (ValueError, ImportError, AttributeError) as e:
        raise ValueError(f"Failed to import strategy: {e}")

def run_competition(s1: Any, s2: Any, rounds: int) -> Tuple[int, int, List[str], List[str]]:
    """
    Runs an iterated Prisoner's Dilemma competition between two strategies for a specified number of rounds.

    Args:
        s1 (object): An instance of the first strategy.
        s2 (object): An instance of the second strategy.
        rounds (int): The number of rounds to simulate.

    Returns:
        Tuple[int, int, List[str], List[str]]: Final scores for strategy 1 and strategy 2, along with their move histories.

    Raises:
        ValueError: If an invalid move (not 'C' or 'D') is detected.
    """
    s1_history, s2_history = [], []
    score1, score2 = 0, 0

    for _ in range(rounds):
        move1 = s1.choose_move(s1_history.copy(), s2_history.copy())
        move2 = s2.choose_move(s2_history.copy(), s1_history.copy())

        # Validating the moves
        if move1 not in ['C', 'D'] or move2 not in ['C', 'D']:
            raise ValueError("Invalid move detected")

        # Calculating the scores
        if move1 == 'C' and move2 == 'C':
            score1 += 3; score2 += 3
        elif move1 == 'C' and move2 == 'D':
            score2 += 5
        elif move1 == 'D' and move2 == 'C':
            score1 += 5
        else:
            score1 += 1; score2 += 1

        # Update histories
        s1_history.append(move1)
        s2_history.append(move2)

    return score1, score2, s1_history, s2_history

def main() -> None:
    """
    Main function to run the iterated Prisoner's Dilemma competition.
    Parses command-line arguments, imports strategies, runs the competition, and prints the results.
    Usage:
        $ python prisoner_dilemma.py TitForTat CustomModule.AlwaysDefect --rounds 100
    """
    parser = argparse.ArgumentParser(description='Run an iterated Prisoner\'s Dilemma competition between two strategies.')
    parser.add_argument('strategy1', help='The first strategy module and class, e.g. "strategies.TitForTat" or "TitForTat".')
    parser.add_argument('strategy2', help='The second strategy module and class, e.g. "strategies.AlwaysDefect" or "AlwaysDefect".')
    parser.add_argument("-r",'--rounds', type=int, default=50, help='Number of rounds to simulate (default: 50)')
    args = parser.parse_args()

    # Importing strategies
    strategy1 = import_strategy(args.strategy1)
    strategy2 = import_strategy(args.strategy2)

    # Running competition
    score1, score2, s1_history, s2_history  = run_competition(strategy1, strategy2, args.rounds)

    print(f"\nCompetition results after {args.rounds} rounds:")
    print(f"Strategy 1 {args.strategy1}: {score1} points")
    print(f"Strategy 2 {args.strategy2}: {score2} points")
    print("\nFinal move histories:")
    print(f"Strategy 1: {'-'.join(s1_history)}")
    print(f"Strategy 2: {'-'.join(s2_history)}")




if __name__ == '__main__':
    main()