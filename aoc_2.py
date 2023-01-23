with open('input2.txt') as f:
    # [A - rock , B - paper , C - scissors]
    # [X - rock , Y - paper , Z - scissors]   PT1
    # [X - lose , Y - draw , Z - win]         PT2
    MATCH_SCORE = { ('A', 'X'): 3,
                    ('A', 'Y'): 6,
                    ('A', 'Z'): 0,
                    ('B', 'X'): 0,
                    ('B', 'Y'): 3,
                    ('B', 'Z'): 6,
                    ('C', 'X'): 6,
                    ('C', 'Y'): 0,
                    ('C', 'Z'): 3,
                  }
    CHOICE_SCORE = {'X': 1, 'Y': 2, 'Z': 3}

    CONVERSION = {  ('A', 'X'): ('A', 'Z'),
                    ('A', 'Y'): ('A', 'X'),
                    ('A', 'Z'): ('A', 'Y'),
                    ('B', 'X'): ('B', 'X'),
                    ('B', 'Y'): ('B', 'Y'),
                    ('B', 'Z'): ('B', 'Z'),
                    ('C', 'X'): ('C', 'Y'),
                    ('C', 'Y'): ('C', 'Z'),
                    ('C', 'Z'): ('C', 'X'),
                 }
    score = 0
    for line in f.readlines():
        opponent, me =  line.rstrip().split()
        opponent, me = CONVERSION[(opponent, me)]
        score += (MATCH_SCORE[(opponent, me)]+ CHOICE_SCORE[me])
    print(score)