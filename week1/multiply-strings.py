class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        i_num_d = {}

        for k, v in num_d.items():
            i_num_d[v] = k
        
        nu1 = sum([num_d[digit] * 10 ** i for i,digit in enumerate(num1[::-1])])
        nu2 = sum([num_d[digit] * 10 ** i for i,digit in enumerate(num2[::-1])])

        product = nu1 * nu2
        if not product:
            return "0"

        product_string = ""

        while product:
            product_string = i_num_d[product % 10] + product_string
            product = product // 10
        
        return product_string
    