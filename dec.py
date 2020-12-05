import time

def time_this(NUM_RUNS=10):
    def decorator(func_tr):
        def func(*args, **kwargs):
            avg_time = 0
            for _ in range(NUM_RUNS):
                t0 = time.time()
                func_tr(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= NUM_RUNS
            fn = func_tr.__name__
            print("Среднее время выполнения %s за %s запусков: %.5f секунд" % (fn, NUM_RUNS, avg_time))
        return func
    return decorator