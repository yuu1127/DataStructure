class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            while (i):
                # >>は右にずれて押し出す（1桁目は消える）
                # <<は左に引っ張り０を追加する
                # binaryの最初の桁が1
                # 13 1101 15 1111 17 10001
                # 9 1001なら 9 & 1 = 1
                # 8 100 8 % 1 = 0
                # 2 10
                # 1 1
                count += i & 2
                i >>= 1
            ans.append(count)
        return ans