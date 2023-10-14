import scipy.stats as stats

# Define the parameters for t 1he binomial distribution
n = int(input('enter the number of trails'))  # Number of trials
p = float(input('enter the probability'))  # Probability of success in each trial

# Create a binomial distribution object
binom_dist = stats.binom(n, p)

# Calculate and print the probability mass function (PMF)
print("Binomial Distribution PMF:")
for k in range(n + 1):
    probability = binom_dist.pmf(k)
    print(f"P(X = {k}) = {probability:.4f}")

# Calculate and print the cumulative distribution function (CDF)
print("\nBinomial Distribution CDF:")

for k in range(n + 1):
    cumulative_probability = binom_dist.cdf(k)
    print(f"P(X <= {k}) = {cumulative_probability:.4f}")