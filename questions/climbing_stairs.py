class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:

            return 2

        # 3なら1 step beforeまでに2パターンある
        one_step_before = 2
        two_steps_before = 1
        all_ways = 0

        # 3から始まる考え方
        for _ in range(2, n):
            #　例えば5はその前の3,4の手順を足したもの, ２個前は次のレベルで1個前になる
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways
        return all_ways
