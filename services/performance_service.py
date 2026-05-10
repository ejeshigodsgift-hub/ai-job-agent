import time


def measure_performance(function):
    start = time.time()

    function()

    end = time.time()

    return end - start