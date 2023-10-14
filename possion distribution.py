import scipy.stats as stats
lambda_parameter = float(input('enter the lambda'))
poisson_dist = stats.poisson(mu=lambda_parameter)

# Calculate and print the probability mass function (PMF) for various values of k
print("Poisson Distribution PMF:")
for k in range(10):  # You can adjust the range as needed
    probability = poisson_dist.pmf(k)
    print(f"P(X = {k}) = {probability:.4f}")

# Calculate and print the cumulative distribution function (CDF) for various values of k
print("\nPoisson Distribution CDF:")
for k in range(10):  # You can adjust the range as needed
    cumulative_probability = poisson_dist.cdf(k)
    print(f"P(X <= {k}) = {cumulative_probability:.4f}")

# Calculate and print mean and variance
mean = poisson_dist.mean()
variance = poisson_dist.var()
print(f"\nMean: {mean:.4f}")
print(f"Variance: {variance:.4f}")