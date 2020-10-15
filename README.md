# Tic-Tac-Toe
Tic-Tac-Toe using minimax algorithm

## Algorithm

node ← position in the game tree  
depth ← depth of the game tree  
maximizingPlayer ← true if the player is maximizing  

<pre>
Minimax(node, depth, maximizingPlayer)  
{  
if depth == 0 or node is a terminal node then  
    return static evaluation of node  
    
if maximizingPlayer then  
  best_score = - infinity  
  for each child of node do  
  current_score = minimax(child, depth-1, false)  
  best_score = max(best_score, current_score)  
  return best_score  
  
else  
  best_score = + infinity  
  for each child of node do  
  current_score = minimax(child, depth-1, true)   
  best_score = min(best_score, current_score)  
  return best_score  
}
</pre>
