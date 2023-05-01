# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        mid = 0

        while start < end:
            mid = (start+end) // 2

            # if True, ignore right half
            if isBadVersion(mid):
                end = mid

            # ignore left half since:
            else:
                start = mid+1

        return start
