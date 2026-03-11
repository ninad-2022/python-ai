import statistics;
# mean
# mode
# median 

# avergae = sum of all num / total num 

print(statistics.mean([1,2,3,4,5]))


print([1,2,4,3,4,5])

print("-"*5, "fmean()", "-"*5)
print(statistics.fmean([1,2,3,4,78,5]))

# return float value 

print("-"*5, "median()", "-"*5)
print(statistics.median([1,2,3,4,5]))
print(statistics.median([1,2,3,4,5,6]))
print(statistics.median([1,2,3,4,5,6,7]))
print(statistics.median([1,2,3,4,5,6,7,8,9, 100]))

#if 5.5 then it will give 6
print(statistics.median_high([1,2,3,4,5,6,7,8,9, 100])) 
#if 5.5 then it will give 5
print(statistics.median_low([1,2,3,4,5,6,7,8,9, 100])) 