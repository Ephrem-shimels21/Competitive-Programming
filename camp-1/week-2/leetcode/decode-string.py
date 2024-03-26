class Solution:
    def decodeString(self, s: str) -> str:
        def decode_it(idx):
            curr_strarr = []
            curr_num = 0
            while idx < len(s):
                if s[idx].isdigit():
                    curr_num = curr_num * 10 + int(s[idx])
                elif s[idx] == "[":
                    idx, res = decode_it(idx + 1)
                    curr_strarr.append(curr_num * res)
                    curr_num = 0
                elif s[idx] == "]":
                    return idx, "".join(curr_strarr)
                else:
                    curr_strarr.append(s[idx])
                idx += 1

            return idx, "".join(curr_strarr)

        return decode_it(0)[1]

                


