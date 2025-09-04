class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
     if abs(x - z) < abs(y - z):
        return 1
     elif abs(y - z) < abs(x - z):
        return 2
     elif abs(y - z) == abs(x -z): 
        return 0
       
# The function findClosest takes three integers x, y, and z as input and returns:
# 1 if x is closer to z than y,
# 2 if y is closer to z than x,
# 0 if both x and y are equally close to z.
# abs() function is used to calculate the absolute difference between the numbers.