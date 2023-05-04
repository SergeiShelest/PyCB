import time

profiler_data = {}


def get_profiler_data():
    return sorted([*(map(tuple, profiler_data.values()))], key=lambda v: v[1], reverse=True)


def print_profiler_data():
    for idx, (prof_type, elapsed, calls) in enumerate(get_profiler_data()):
        print("%i) %s: %.6f s (%i calls, %.6f s per call)." % (
            idx + 1, prof_type, elapsed, calls, elapsed / calls
        ))


def profiler(prof_type=None):
    def decorator(func):
        nonlocal prof_type

        prof_type = prof_type or repr(func)
        profiler_data[prof_type] = [prof_type, 0, 0]

        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            profiler_data[prof_type][1] += end - start
            profiler_data[prof_type][2] += 1

            return result
        return wrapper
    return decorator
