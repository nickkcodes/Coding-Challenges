def rps(p1, p2):
    # 1. Handle a Tie immediately
    if p1 == p2:
        return "Draw!"
    
    # 2. Define the winning rules
    # The key BEATS the value
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    # 3. Check if Player 1's move beats Player 2's move
    if beats[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"