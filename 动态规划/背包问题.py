class solute():
    def al(self,w,v,W,N):
        ## w,v代表物体的质量以及其编号
        ## W 代表背包能装下的质量
        ##N代表可以装N件时
        dp = [[0]*(W+1) for i in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,W+1):
                dp[i][j] = dp[i-1][j]
                if j - w[i-1] >= 0:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
        return dp

    def rem(self,w,v,W,N):
        dp = [[0]  *(W+1)] + [[0] + [-1] * W for i in range(N)]
        maxim = self.remal(w,v,N,W,dp)
        print(dp
              )
        return maxim

    def remal(self,w,v,N,W,dp):
        if dp[N][W] < 0:
            if W < w[N-1]:
                val = self.remal(w,v,N-1,W,dp)
            else:
                val = max(self.remal(w,v,N-1,W,dp),
                          v[N-1]+self.remal(w,v,N-1,W-w[N-1],dp))
            dp[N][W] =val

        return dp[N][W]


if __name__ == '__main__':
    w = [2,1,3,2]
    v = [12,10,20,15]
    N = 4
    W = 5
    sol = solute()
    print(sol.rem(w,v,W,N))
