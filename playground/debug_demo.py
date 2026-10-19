def average(timings_ms):
    total = 0
    for t in timings_ms:
        total += t
    return total / len(timings_ms)


if __name__ == "__main__":
    runs = [10, 20, 30]
    print(average(runs))
    print(average([]))
