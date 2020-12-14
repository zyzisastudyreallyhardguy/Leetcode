class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start = 0
        end = x
        while True:
            mid = start + (end - start)//2
            if mid > x/mid:
                end = mid
            else:
                if (mid + 1) > x/(mid + 1):
                    return int(mid)
                start = mid