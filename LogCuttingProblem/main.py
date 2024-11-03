import json
from time import time
from mock.generator import LogPriceGenerator
from algorithms.dynamic_programming import memoized_cut_log
from algorithms.greedy import greedy_cut_log
import matplotlib.pyplot as plt  # type: ignore
import sys

ALGORITHMS = ["top_down", "greedy"]
GRAPHIC_TYPES = ["price", "time"]


def generate_cases(initial: int, final: int, step: int) -> dict:
    return {
        n: LogPriceGenerator.generate_random_log_prices(n)
        for n in range(initial, final + 1, step)
    }


def measure_time(prices: list, func) -> dict:
    initial_time = time()
    max_price = func(tuple(prices), len(prices))
    final_time = time()
    return {"time": final_time - initial_time, "price": max_price}


def process_results(initial: int, final: int, step: int) -> dict:
    sys.setrecursionlimit(99999999)
    log_size_price = generate_cases(initial, final, step)
    results = {}
    for log_size in log_size_price.keys():
        if log_size not in results.keys():
            results[log_size] = {}
        for algorithm in ALGORITHMS:
            if algorithm not in results[log_size].keys():
                results[log_size][algorithm] = -1
            if algorithm == "top_down":
                results[log_size][algorithm] = measure_time(
                    log_size_price[log_size], memoized_cut_log
                )
            if algorithm == "greedy":
                results[log_size][algorithm] = measure_time(
                    log_size_price[log_size], greedy_cut_log
                )
        results[log_size]["perc"] = (
            results[log_size]["greedy"]["price"] * 100
        ) / results[log_size]["top_down"]["price"]
    return results


def save_and_print_results(results: dict) -> None:
    text = ""
    line_format = "{:>12}     {:>12}     {:>12}     {:>12}     {:>12}     {:>12}\n"
    header = line_format.format(
        "n",
        "vDp",
        "tDp",
        "vgreedy",
        "tgreedy",
        "%",
    )
    text += header
    text += "-" * len(header) + "\n"

    for log_size in results.keys():
        text += line_format.format(
            "%d" % int(log_size),
            "%6d" % results[log_size]["top_down"]["price"],
            "%2.6f" % results[log_size]["top_down"]["time"],
            "%6d" % results[log_size]["greedy"]["price"],
            "%2.6f" % results[log_size]["greedy"]["time"],
            "%2.2f" % results[log_size]["perc"],
        )
        # text += "\n"
    with open("results_tables.txt", "w") as file:
        file.write(text)
    with open("results_tables.json", "w") as file:
        json.dump(results, file)
    print(text)


def get_result_axis(results: dict, graphic_type: str, algorithm: str) -> tuple:
    n_values = results.keys()
    y_values = []

    for value in results.values():
        y_values.append(value[algorithm][graphic_type])

    return n_values, y_values


def plot_graphics(results: dict) -> None:
    for graphic_type in GRAPHIC_TYPES:
        i = 0
        plt.figure(i, figsize=(10, 6))

        for algorithm in ALGORITHMS:
            x_axis, y_axis = get_result_axis(results, graphic_type, algorithm)
            plt.plot(x_axis, y_axis, label=f"{algorithm}")

        plt.xlabel("n")
        plt.ylabel(graphic_type)
        plt.title("Dynamic Programming vs greedy")
        plt.grid(True)
        plt.tight_layout()
        plt.legend()
        plt.savefig(f"./results/{graphic_type}.png")
        plt.show()
        i += 1


if __name__ == "__main__":
    initial = int(input("Tamanho Inicial: "))
    final = int(input("Tamanho Final: "))
    step = int(input("Step: "))
    results = process_results(initial, final, step)
    save_and_print_results(results)
    plot_graphics(results)
