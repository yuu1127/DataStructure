class Solution:
    def removeComments(source):
        in_block = False
        ans = []
        for line in source:
            i = 0
            if not in_block:
                new_line = []
            while i < len(line):
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif not in_block and line[i:i+2] == '//':
                    break
                elif not in_block:
                    new_line.append(line[i])
                i += 1
            if new_line and not in_block:
                ans.append("".join(new_line))
        return ans

def main():
    s = ["a/*comment", "line", "more_comment*/b"]
    print(Solution.removeComments(s))

if __name__ == "__main__":
    main()
