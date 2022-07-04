import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        #print(nums)
        self.nums = nums
        # ヒープ構造のリストになっている
        heapq.heapify(self.nums)
        #print(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while  len(self.nums) > self.k:
            #小さいやつを削除
            heapq.heappop(self.nums)
            print(self.nums)
        #print(self.nums)
        #一番前が３番目に小さいやつ
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)