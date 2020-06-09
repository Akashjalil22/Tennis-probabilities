# Tennis-probabilities
Calculate the probability of winning a game, tiebreak, set, and match using recursion

The intuition here is that we will always take player A as the player for which we wish to compute the winning probabilities

# Definition of variables
a, b  = Points in the current game for player A and B respectively

pa, pb = Probability of player A or player B respectively winning a point when serving

ga, gb = Number of games won in a set for player A and B respectively

sets = Number of sets for the match, this is either 3 or 5 depending on the type of match being played

sa, sb = Number of sets won by player A and player B respectively

server = If player A is serving at the current state

# What pa and pb to use?
The choice of pa and pb will have a significant influence on the probabilities. Thus, it's important to choose these values with respect to the players. A sensible method is to calculate pa and pb using historical data by taking, for example, total point wins with serve / total serves for a given player. 

We'll need to pay close attention to the type of match being modelled. So, if we're trying to calculate the probability of player A winning a game on a <strong>clay</strong> court, we should make sure the value of pa has been calculated based on matches played by player A on a <strong>clay</strong> court.

# Memoization for recursion functions
We use a memo (a dictionary) to store probabilities already calculated as this will speed up
the recursions used to calculate the probabilities
