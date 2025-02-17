# 5,3
# 1 -> 1 -> 4 -> 7 -> 19 
def rabbit_fib(months, rabbit_pairs_produced, memo={}):
    if (months in memo):
        return memo[months]
    if (months <= 2):
        return 1

    memo[months] = rabbit_fib(months - 1, rabbit_pairs_produced, memo) + rabbit_fib(months - 2, rabbit_pairs_produced, memo) * rabbit_pairs_produced
    return memo[months]

result = rabbit_fib(5,3,{})
print(result)
print(result == 19)

result2 = rabbit_fib(34, 4, {})
print(result2)