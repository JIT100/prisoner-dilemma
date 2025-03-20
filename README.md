# Iterated Prisoner's Dilemma

This is a Python-based command-line tool that simulates an **Iterated Prisoner’s Dilemma** competition between two strategies. Players (strategies) repeatedly decide whether to **cooperate ( C )** or **defect ( D )**, and scores are assigned based on their choices. The competition runs for a specified number of rounds, and the results are displayed at the end.

## Features
- Battle two strategies over multiple rounds.
- Detailed move history tracking.
- Standard Prisoner's Dilemma scoring system.
- Flexible strategy import system.

-   Supports multiple built-in strategies, including:
    
    -   **TitForTat**: Cooperates initially, then mimics the opponent’s last move.
        
    -   **AlwaysCooperate**: Always cooperates.
        
    -   **AlwaysDefect**: Always defects.
        
    -   **RandomBuster**: Randomly chooses between cooperating and defecting.
        
    -   **GrimTrigger**: Cooperates until the opponent defects, then always defects forever.
        
-   Users can define and use **custom strategies**.
    
-   Command-line interface to run competitions between different strategies.

## Payout Scores

The scoring system follows the standard Prisoner’s Dilemma rules:

-   **Both Cooperate (C, C)** → **3 points each**
    
-   **One Cooperates, One Defects (C, D)** → **Defector: 5 points, Cooperator: 0 points**
    
-   **Both Defect (D, D)** → **1 point each**
    
## Installation

### Prerequisites

Ensure you have **Python 3.10+** installed on your system.

### Clone the Repository

### Install Dependencies

This project does not require external libraries, so no additional installation is needed.

## Usage

Run the **competition** using the command-line tool:

    python prisoner_dilemma.py [STRATEGY1] [STRATEGY2] [OPTIONS]
    
    # Example:
    python prisoner_dilemma.py TitForTat strategies.AlwaysDefect -r 30

### Arguments:

-   `strategy1` and `strategy2`: The names of the competing strategies. You can use built-in strategies or custom ones.
    
-   `-r, --rounds`: _(Optional)_ The number of rounds (default is **50**).
    

### Example Output:

    INFO: Successfully imported strategy: TitForTat
    INFO: Successfully imported strategy: strategies.AlwaysDefect
    
    Competition results after 30 rounds:
    Strategy 1 TitForTat: 29 points
    Strategy 2 strategies.AlwaysDefect: 34 points
    
    Final move histories:
    Strategy 1: C-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D
    Strategy 2: D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D-D

## Adding Custom Strategies
1.  Create new strategies in  `strategies.py`:
>     class CustomStrategy:
>         def choose_move(self, own_history: list, enemy_history: list) -> str:
>             # Implement your logic here
>             # return 'C'   or 'D'

3.  Required interface:

>     def choose_move(self, own_history, enemy_history) -> str:
>         # Must return 'C' or 'D'


**Example:**

You can then run:

    python prisoner_dilemma.py TitForTat CustomStrategy

## Logging

The program uses Python's `logging` module to provide status updates for importing the modules.

## Author

Developed by **JIT100**. Contributions and suggestions are welcome!

