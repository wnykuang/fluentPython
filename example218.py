import bisect
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score) 
    return grades[i]

#use the bisect to find out the index/rank the score "should be" inserted
print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])