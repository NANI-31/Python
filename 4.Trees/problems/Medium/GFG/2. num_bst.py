from print import printed

n = 50
dp = [0] * (n+1)
dp[0], dp[1] = 1,1

for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i] += dp[i-j] * dp[j-1]
        
printed(dp[n])