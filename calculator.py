import os


priorities = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0
}
digits = '0123456789'

def transform(s):
    '''Transform infix expression to postfix.


    transform(...)
        transform(s)

        arguments:
        s -- the expression in infix form.

        
        Return the postfix form of s.
        
    '''
    i = 0
    output = ''
    stack = []
    while i < len(s):
        if s[i].isdigit():
            while i < len(s) and s[i].isdigit():
                output += s[i]
                i+=1
            output += ' '
        elif s[i] == '(':
            if s[i+1]=='+' or s[i+1] == '-':
                i+=1
                output+=s[i]
                i+=1
                while i < len(s) and s[i].isdigit():
                    output += s[i]
                    i+=1
                output+=' '
                if s[i]==')':
                    i+=1
                else:
                    raise KeyError
            else:
                stack.append(s[i])
                i+=1
        elif s[i] == ')':
            top = stack.pop()
            while top != '(' :
                output += top
                output += ' '
                top = stack.pop()
            i+=1
        elif s[i] in priorities:
            while ((len(stack) != 0) and (priorities[stack[len(stack) - 1]] >= priorities[s[i]])):
                output+=stack.pop()
                output+=' '
            stack.append(s[i])
            i+=1
    while len(stack)!=0:
        output+=stack.pop()
        output+=' '
    return output



def calculate(s):
    '''Calculate the postfix expression.

    calculate(...)
        calculate(s)

        arguments:
        s -- expression in postfix form.

        
        Return the result of calculating the expression s.

    '''
    stack = []
    s = s.strip().split()
    i=0
    while i < len(s):
        if s[i] not in priorities:
            stack.append(s[i])
        elif s[i] in priorities:
            b = int(stack.pop())
            a = int(stack.pop())
            if s[i]=='+':
                stack.append(a+b)
            elif s[i]=='-':
                stack.append(a-b)
            elif s[i] == '*':
                stack.append(a*b)
            elif s[i] == '/':
                stack.append(a/b)
        i+=1
    return stack
    




def is_correct(s):
    for i in range(10):
        s = s.replace(str(i),'')
    for i in priorities:
        s = s.replace(i,'')
    s = s.replace(')','')
    if len(s)==0:
        return True
    else:
        return False



    
def go(s):
    print("Вывод:", end = "")
    print(s, end=" ")
    try:
        res = calculate(transform(s))
    except ZeroDivisionError:
        print("--- Ошибка: Деление на ноль!")
    except:
        print("--- Ошибка ввода!")
    else:
        print("=", end = " ")
        print(res.pop())




while True:
    print("Введите выражение или\nсошлитесь на файл с помощью кострукции 'f <название файла с расширением>'")
    print("Для выхода введите exit")
    command = input().strip()
    if command[0]=='(' or command[0] in digits:
        if is_correct(command):
            go(command)
        else:
            print("Ошибка ввода!")
    elif command[0] == 'f':
        fileName = command[1:].strip()
        try:
            f = open(fileName)
        except FileNotFoundError:
            print("Файл не найден")
        else:
            for expression in f:
                expression = expression.replace('\n','')
                expression = expression.strip()
                if is_correct(expression):
                    go(expression)
                else:
                    print("Ошибка ввода!")
            f.close()
    elif command == 'exit':
        break
    else:
        print("Неизвестная команда!")

    print("Очистить консколь?(y/n)")
    flag = input()
    if flag=="y" or flag == "Y":
        os.system("cls")
    else:
        pass
        


    

