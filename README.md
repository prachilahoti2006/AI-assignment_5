# AI_Assignment_5 README

### PROJECT 1 - SEARCH TECHNIQUES

1. minimax.py

   * Implements the Minimax Search Algorithm
   * Used in Tic-Tac-Toe game strategy
   * Determines the best possible move

2. alphabeta.py

   * Implements Alpha-Beta Search
   * Eliminates unnecessary branches
   * Increases search performance

3. heuristic_alphabeta.py

   * Implements Heuristic-Based Alpha-Beta Pruning
   * Uses board evaluation scores
   * Effective for deeper game trees

4. monte-carlo.py

   * Implements Monte Carlo Tree Search (MCTS)
   * Uses UCT selection strategy
   * Widely used in modern game-playing AI

HOW TO RUN

python minimax.py

python alphabeta.py

python heuristic_alphabeta.py

python monte-carlo.py

### PROJECT 2 - SMART TRAVEL PLANNER

planner.py

Features:

* Suggests tourist attractions based on interests
* Considers user budget constraints
* Uses a predefined travel knowledge base

Example:

City: Hyderabad

Interest: History

Budget: 3000

Output:

Travel recommendations and estimated expenses.

HOW TO RUN

python planner.py

### PROJECT 3 - KNOWLEDGE GRAPH SYSTEM

knowledge_graph.txt

Stores sample knowledge graph triples:

* Subject
* Predicate
* Object

Tools Studied:

* Neo4j
* Apache Jena
* Protégé
* RDFLib

### PROJECT 4 - BAYESIAN NETWORK MODEL

bayesian_model.py

Uses:

* pgmpy package

Sample Network:

Rain → Traffic → Late

Performs probability-based reasoning and inference.

HOW TO RUN

Install dependency:

pip install pgmpy

Execute:

python bayesian_model.py

### TESTING

Alpha-Beta Pruning:
Compare explored nodes with standard Minimax.

Heuristic Alpha-Beta:
Run with search depths 2, 4 and 6.

Monte Carlo Tree Search:
Execute with different iteration counts.

### REPORT CONTENTS

Include the following sections:

* Working of algorithms
* Flow diagrams
* Output screenshots
* Complexity evaluation
* Pros and cons
* Practical applications
