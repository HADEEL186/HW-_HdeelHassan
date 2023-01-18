class par_solution:
   def par_match(self, my_str):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in my_str:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(par_solution().par_match("(){}[]"))
print(par_solution().par_match("()[{)}"))
print(par_solution().par_match("()"))