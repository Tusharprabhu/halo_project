import statistics

# Define your data
ordinal_data = [1, 2, 3, 2, 3, 3, 4, 5, 4, 3]
continuous_data = [3.2, 4.5, 3.0, 4.7, 5.1, 3.8]
discrete_data = [2, 4, 6, 4, 6, 8, 8, 10]


def calculate_statistics(data, data_type):
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data) if data_type == "ordinal" else "Mode not applicable"

    if data_type in ["continuous", "discrete"]:
        variance = statistics.variance(data)
        std_dev = statistics.stdev(data)
    else:
        variance = "Variance not applicable"
        std_dev = "Standard Deviation not applicable"

    frequency = {item: data.count(item) for item in set(data)}

    return mean, median, mode, variance, std_dev, frequency


data_types = ["ordinal", "continuous", "discrete"]
data_lists = [ordinal_data, continuous_data, discrete_data]

for data_type, data_list in zip(data_types, data_lists):
    mean, median, mode, variance, std_dev, frequency = calculate_statistics(data_list, data_type)

    print(f"Statistics for {data_type} data:")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")
    print("Frequency:")
    for item, count in frequency.items():
        print(f"{item}: {count} times")
    print()
