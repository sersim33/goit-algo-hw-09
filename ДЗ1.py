import time


def find_coins_greedy(amount, coins):
    coin_count = {coin: 0 for coin in coins}

    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Кількість монет даного номіналу
            amount -= coin * count  # Зменшуємо суму на вартість цих монет
            coin_count[coin] = count  # Записуємо кількість використаних монет
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

measure_time(find_coins_greedy, total, coins)
print(find_coins_greedy(total,coins))