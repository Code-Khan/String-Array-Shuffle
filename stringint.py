# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
# Example 1:
# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Example 2:
# Input: s = "odcgin", indices = [1, 2, 0, 5, 3, 4]
# Output: "coding"
# Example 3:
# Input: s = "aiohn", indices = [3,1,4,2,0]
# Output: "nihao"
# Example 4:
# Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
# Output: "arigatou"
# Example 5:
# Input: s = "art", indices = [1,0,2]
# Output: "rat"

# Solution in Python # 

def unshuffle(s, indices):
    new_string = [" "] * len(s)
    for i in range(len(s)):
        new_string[indices[i]] = s[i]
    return ''.join(new_string)
print("SOLUTION 1")
print(unshuffle('abc', [0,1,2]))
print(unshuffle('odcgin', [1, 2, 0, 5, 3, 4]))
print(unshuffle('aiohn', [3,1,4,2,0]))
print(unshuffle('aaiougrt', [4,0,2,6,7,3,1,5]))
print(unshuffle('art', [1,0,2]))
print('\n')
def unshuffle2(s, arr):
  zipped = zip(s, arr)
  sorted_str = sorted(zipped, key=lambda x: x[1])
  return ''.join([x[0] for x in sorted_str])
print("SOLUTION 2")
print(unshuffle2('abc', [0,1,2]))
print(unshuffle2('odcgin', [1, 2, 0, 5, 3, 4]))
print(unshuffle2('aiohn', [3,1,4,2,0]))
print(unshuffle2('aaiougrt', [4,0,2,6,7,3,1,5]))
print(unshuffle2('art', [1,0,2]))

