class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a = a & mask
        b = b & mask
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        if a <= 0x7FFFFFFF:
            return a
        else:
            return ~(a ^ mask)