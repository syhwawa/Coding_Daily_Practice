Analyzing the effectiveness of a tutorial used in statistics class.

Have a error in score, after correcting this error, you want to perform a two-tailed, paired t-test with the following hypotheses,

- H0(null): The average difference between before and after the tutorial is 0
- H1(alternative): The average difference is non-Zero

score after and score before is between 300-1000, alpha is 0.001 to 0.10.

You are allow to use scipy and numpy:

Example: 

a = [786,828,814,790,828,850,854,826,828,762,812,770,762,794,782,816,808,760,828,848]
b = [792,688,860,800,786,706,744,810,794,738,778,764,772,798,762,772,778,762,742,764]

alpha = 0.005, the output should be shouldreject(a, b, alpha) = true

```Python
from scipy.stats import ttest_ind
import numpy as np

def shouldreject(a, b, alpha):
    score_before = np.asarray(a)
    score_after = np.asarray(b)

    score_before_mean = np.mean(score_before)
    score_after_mean = np.mean(score_after)
    
    print(score_before_mean)
    print(score_after_mean)
    
    score_before_std = np.std(score_before)
    score_after_std = np.std(score_after)

    print(score_before_std)
    print(score_after_std)

    ttest,pval = ttest_ind(score_before,score_after)
    
    print(pval)
    
    if pval < alpha:
        return True
    else:
        return False
    
a = [786,828,814,790,828,850,854,826,828,762,812,770,762,794,782,816,808,760,828,848]
b = [792,688,860,800,786,706,744,810,794,738,778,764,772,798,762,772,778,762,742,764]
alpha = 0.005

shouldreject(a, b, alpha)
```

https://towardsdatascience.com/hypothesis-testing-in-machine-learning-using-python-a0dc89e169ce
