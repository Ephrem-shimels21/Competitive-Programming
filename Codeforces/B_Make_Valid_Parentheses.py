def find_regular(pars):
    stack = []
    n = len(pars)

    for par in pars:
        if par == "(":
            stack.append(par)
        elif par == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(par)
    return n - len(stack)


pars = input()

print(find_regular(pars))
