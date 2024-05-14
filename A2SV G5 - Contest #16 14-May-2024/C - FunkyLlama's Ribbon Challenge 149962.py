# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

import sys, threading


def main():
    inputt = list(map(int, input().split()))

    amount = inputt[:1][0]
    pieces = inputt[1:]

    def dp(curr_amount):
        if curr_amount < min(pieces):
            if curr_amount == 0:
                return 0
            return float("-inf")

        if curr_amount not in memo:
            max_val = float("-inf")
            for piece in pieces:
                if curr_amount - piece >= 0:
                    max_val = max(max_val, dp(curr_amount - piece))

            memo[curr_amount] = max_val + 1

        return memo[curr_amount]

    memo = {}
    max_val = dp(amount)

    print(max_val)


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
