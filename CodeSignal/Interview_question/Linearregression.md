Given obs_A = [0,2,3], obs_B = [1,2,1]

Output: linearRegressionLoo(obs_A, obs_B) = 0.75

Given obs_A = [0,2,3], obs_B = [1,2,1]

Output  linearRegressionLoo(obs_A, obs_B) = 4.083


I have a confusion that how the weights (a and b) for equation (y= a+bx) are calculated in linear regression Machine learning Algorithm -

by solving the linear equation a = mean (y) - b * mean(x) and b =  covariance / vaiance of X

```Python
def linearRegressionLoo(obs_A, obs_B):
    error_sum = 0
    loo = lambda arr, idx :arr[:idx] + arr[(idx+1):]
    n = len(obs_A)
    
    for i in range(n):
        A_train = loo(obs_A, i)
        B_train = loo(obs_B, i)
        mean_A = sum(A_train) / (n - 1.0)
        mean_B = sum(B_train) / (n - 1.0)
        print(A_train)
        print(B_train)
        print(mean_A)
        print(mean_B)
        
        slope = (((A_train[0] * B_train[0]  + A_train[1] * B_train[1])/ 2) - (mean_B * mean_A)) / (((A_train[0] - mean_A)** 2 + 
        (A_train[1] - mean_A)** 2)/2)
        intercept = mean_B - slope * mean_A
        pred_B = slope * obs_A[i] + intercept 
        error_sum += (pred_B - obs_B[i]) **2 
        
    ans = error_sum / float(n)
    return ans

obs_A = [0,2,3]
obs_B = [1,2,1]
linearRegressionLoo(obs_A, obs_B) 
```
