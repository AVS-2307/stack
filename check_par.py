from Stack import Stack

s = Stack()
line = '{}'

par_open = ('(', '[', '{')
par_close = (')', ']', '}')
is_good = True
for i in line:
    if i in par_open:
        s.push(i)
    elif i in par_close:
        if s.isEmpty():
            is_good = False
            break
        else:
            open_bracket = s.pop()
            if open_bracket == '(' and i == ')':
                continue
            if open_bracket == '[' and i == ']':
                continue
            if open_bracket == '{' and i == '}':
                continue
            is_good = False
            break

if is_good == True and s.size() == 0:
    print('Cбалансированно')
else:
    print('Несбалансированно')
