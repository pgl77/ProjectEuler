# https://medium.com/coderbastion/optimizing-primes-5551760d5f39

function sumPrimes(num) {
  const primes = [];
  const filteredArr = [];
  let i;
  let j;
  for (i = 2; i <= num; i++) {
    if (!filteredArr[i]) {
      primes.push(i);
      // j = i << 1; is same as multiples of i and j = i. So the number that is passed over
      // in the inside loop is the prime number. And that refers back to !filteredArr[i].
      for (j = i * 2; j <= num; j += i) {
        filteredArr[j] = true;
      }
    }
  }
  return primes.reduce((a, b) => a + b);
}
console.log(sumPrimes(2000000));

The answer is 142,913,828,922. Using this algorithm in node takes less than a second.
# We start with an outer loop for each number from 2 to 2,000,000. For each loop we check the filtered array for a value at the index of our number. The filtered array starts out empty. So we first take 2, push it onto our primes array, then go over our filtered array and replace all multiples of 2 with the boolean true.
# I believe the reason this solution is so much faster is that there is almost no calculations or intensive memory storage. In the previous solution I was filtering the array, but each time I called the array.filter() method, an entirely new array had to be built and allocated memory. I also forced the computer to perform a modulus operation and check the result. That’s an incredible amount of computation when you’re going through an array of two million elements.
# In the end, both the second and third iteration of the algorithm both use the basic idea of Sieve of Eratosthenes, but one only had to assign a boolean and check elements for true or false. The other relied on mathematical operations and constructing millions of objects in memory. So the next time your algorithm is taking forever to compute, see if you can cut down on mathematical comparisons.
