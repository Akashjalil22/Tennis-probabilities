"""
Values a,b can be between 0 - 4 which represent tennis points "Love", "15", "30", "40", and "Game"
"""
memo_for_games = {}
def probability_of_game(a,b,p):    
    
    if (a==4 and b <= 2):
        return 1
    
    elif (b == 4 and a <= 2):
        return 0
    
    elif (a == 3 and b == 3):
        return (p**2)/(p**2 + (1-p)**2)
    
    elif (a == 4 and b == 3): 
        return p
    
    elif (b == 4 and a == 3):
        if (a,b,p) in memo_for_games:
            return memo_for_games[(a,b,p)]
        else:
            temp_prob = p*probability_of_game(3,3,p)
            memo_for_games[(a,b,p)] = temp_prob
        return temp_prob
    
    if (a,b,p) in memo_for_games:
        return memo_for_games[(a,b,p)]
    
    else:
        temp_prob = p*probability_of_game(a+1, b, p) + (1-p)*probability_of_game(a,b+1,p)
        memo_for_games[(a,b,p)] = temp_prob
    return temp_prob

"""
Values a,b in a tiebreaker represent points 0 - 7 where 7 is the winning point
"""
memo_for_tie_breaker = {}
def probability_of_tie_break(a,b,pa,pb,server = True):
    
    if not server:
        a ,b = b, a
        pa, pb = pb, pa
    
    elif (a == 7 and (a-b) >= 2):
        return 1
    
    elif (b == 7 and (b-a) >= 2):
        return 0
    
    elif (a == 6 and b == 6):
        return pa*(1-pb)/(pa*(1-pb) + pb*(1-pa))
    
    elif (2 <= (a + b + 3)%4 <= 3):
        if (a,b,pa,pb,server) in memo_for_tie_breaker:
            return memo_for_tie_breaker[(a,b,pa,pb,server)]
        else:
            temp_prob = pa*probability_of_tie_break(a + 1,b,pa,pb) + (1-pa)*probability_of_tie_break(a,b+1,pa,pb)
            memo_for_tie_breaker[(a,b,pa,pb,server)] = temp_prob
            return temp_prob
            
    elif (0 <= (a + b + 3)%4 <= 1):
        if (a,b,pa,pb,server) in memo_for_tie_breaker:
            return memo_for_tie_breaker[(a,b,pa,pb,server)]
        else:
            temp_prob = pb*probability_of_tie_break(a,b+1,pa,pb) + (1-pb)*probability_of_tie_break(a+1,b,pa,pb)
            memo_for_tie_breaker[(a,b,pa,pb,server)] = temp_prob
            return temp_prob

"""
Values ga, gb can be between 0 - 6 representing the number of games in a set where 6 denotes winning the set
"""
memo_for_set = {}    
def probability_of_set(ga,gb,a,b,pa,pb,server = True):
    
    if not server:
        ga, gb, a, b, pa, pb = gb, ga, b, a, pb, pa
    
    if (ga >= 6 and ga - gb >= 2):
        return 1
    
    elif(gb >= 6 and gb - ga >= 2):
        return 0
    
    elif(ga == 6 and gb == 6):
        return probability_of_tie_break(a,b,pa,pb)
    
    elif((ga+gb)%2 == 0):
        if (ga,gb,a,b,pa,pb,server) in memo_for_set:
            return memo_for_set[(ga,gb,a,b,pa,pb,server)]
        else:
            temp_prob = probability_of_game(a,b,pa)*probability_of_set(ga + 1,gb,0,0,pa,pb) + (1-probability_of_game(a,b,pa))*probability_of_set(ga,gb+1,0,0,pa,pb)
            memo_for_set[(ga,gb,a,b,pa,pb,server)] = temp_prob
            return temp_prob

    elif((ga+gb)%2 != 0):
        if (ga,gb,a,b,pa,pb,server) in memo_for_set:
            return memo_for_set[(ga,gb,a,b,pa,pb,server)]
        else:
            temp_prob = probability_of_game(b,a,pb)*probability_of_set(ga,gb+1,0,0,pa,pb) + (1-probability_of_game(b,a,pb))*probability_of_set(ga+1,gb,0,0,pa,pb)
            memo_for_set[(ga,gb,a,b,pa,pb,server)] = temp_prob
            return temp_prob

"""
Values sa, sb can be between 0 - 3 for a 3 set match or 0 - 5 for a 5 set match where 3 or 5 denotes winning the match
"""
memo_for_match = {}    
def probability_of_match(sets,sa,sb,ga,gb,a,b,pa,pb,server = True):
    if sets == 5:
        if (sa == 3 and sb < 3):
            return 1
        elif (sb == 3 and sa < 3):
            return 0
        elif (sa == 2 and sb ==2):
            return probability_of_set(ga,gb,a,b,pa,pb,server)
    
    elif sets == 3:
        if (sa == 2 and sb < 2):
            return 1
        elif (sb == 2 and sa < 2):
            return 0
        elif (sa == 1 and sb ==1):
            return probability_of_set(ga,gb,a,b,pa,pb,server)
    
    if (sa+sb)%2==0:
        if (sets,sa,sb,ga,gb,a,b,pa,pb,server) in memo_for_match:
            return memo_for_match[(sets,sa,sb,ga,gb,a,b)]
        else:
            temp_prob = probability_of_set(ga,gb,a,b,pa,pb,server)*probability_of_match(sets,sa,sb,ga,gb,a,b,pa,pb,server) + (1-probability_of_set(ga,gb,a,b,pa,pb,server))*probability_of_match(sets,sa,sb+1,ga,gb,a,b,pa,pb,server)
            memo_for_match[(sets,sa,sb,ga,gb,a,b,pa,pb,server)] = temp_prob
            return temp_prob
            
    elif (sa+sb)%2!=0:
        if (sets,sa,sb,ga,gb,a,b,pa,pb,server) in memo_for_match:
            return memo_for_match[(sets,sa,sb,ga,gb,a,b,pa,pb,server)]
        else:
            temp_prob = probability_of_set(ga,gb,a,b,pa,pb,server = False)*probability_of_match(sets,sa,sb+1,ga,gb,a,b,pa,pb,server) + (1-probability_of_set(ga,gb,a,b,pa,pb,server = False))*probability_of_match(sets,sa+1,sb,ga,gb,a,b,pa,pb,server)
            memo_for_match[(sets,sa,sb,ga,gb,a,b,pa,pb,server)] = temp_prob
            return temp_prob
