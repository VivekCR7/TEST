"""
problem Statement: find the longest common subsequence between 2 strings

input
SHINCHAN
NOHARAAA

output
3

NHA is longest common subsequence

"""

def LCS(s1,s2):
    curr = [0]*(len(s1)+1)
    prev = [0]*(len(s2)+1)

    for c1 in s1:
        curr,prev = prev,curr
        for j,c2 in enumerate(s2,1):
            curr[j] = (1+prev[j-1]) if c1==c2 else max(prev[j],curr[j-1])

    return curr[-1]


s1 = input()
s2 = input()
print('The Longest common subsequence between two string is: ',LCS(s1,s2))


