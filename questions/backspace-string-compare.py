r# using stack is really efficient especially in
# remove element from container !!!


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # def RemoveBack(s):
        #     new = ""
        #     for c in s:
        #         if c != "#":
        #             new += c
        #         else:
        #             new = new[:-1]
        #     return "" + new
        #
        # ss = RemoveBack(s)
        # tt = RemoveBack(t)
        # return ss == tt
        def remove_back(s):
            new = []
            for c in s:
                if c != "#":
                    new.append(c)
                else:
                    if new:
                        new.pop()
            return "".join(new)

        ss = remove_back(s)
        tt = remove_back(t)
        return ss == tt
