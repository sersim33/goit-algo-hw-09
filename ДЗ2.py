import time

def find_min_coins(total, coins):
    n = len(coins)
    # Create a table to store the optimal values of subproblems
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    # Initialize a table to store the coins used to achieve each amount
    coin_used = [[] for _ in range(total + 1)]

    # Build the table bottom-up
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin_used[i - coin] + [coin]

    # Count the occurrences of each coin denomination
    coin_count = {}
    for coin in coins:
        coin_count[coin] = coin_used[total].count(coin)

    return coin_count

def measure_time(func, *args, iterations=100):
    """
    Вимірює час виконання функції середньо за вказану кількість ітерацій.
    """
    start_time = time.time()
    for _ in range(iterations):
        func(*args)
    end_time = time.time()

    avg_time_taken = (end_time - start_time) / iterations
    print(f"Average time taken for {func.__name__}: {avg_time_taken:.10f} seconds")

total = 11131
coins = [50, 25, 10, 5, 2, 1]

measure_time(find_min_coins, total, coins)
print(find_min_coins(total, coins))