T = int(input())
for _ in range(T):

    N = int(input())
    dp = [[0,0] for _ in range(41)]
    dp[0] = [1,0]
    dp[1] = [0,1]

    for i in range(2, N+1):
        a = dp[i-1][0] + dp[i-2][0]
        b = dp[i-1][1] + dp[i-2][1]
        dp[i] = [a,b]
    print(dp[N][0], dp[N][1])
