class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            while i:
                #  
                # binaryの最初の桁が1
                # 13 1101 15 1111 17 10001
                # 9 1001なら 9 & 1 = 1
                # 8 100 8 % 1 = 0
                # 2 10
                # 1 1
                count += i & 1
                i >>= 1
            ans.append(count)
        return ans