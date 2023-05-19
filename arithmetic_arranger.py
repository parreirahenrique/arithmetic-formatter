from typing import List

def arithmetic_arranger(problem_list: List[str], print_result: bool = False):

    arranged_problems: str = ""

    if len(problem_list) > 5:
        arranged_problems = "Error: Too many problems."
    
    else:
        addend_1 = []
        operation = []
        addend_2 = []
        results = []
        line = []

        for i in range(len(problem_list)):
            break_function = False
            
            addend_1.append(problem_list[i].split(' ')[0])

            for j in range(len(addend_1[i])):
                if j == 0 and not addend_1[i][j].isnumeric() and addend_1[i][j] != '-':
                    break_function = True
                    message = "Error: Numbers must only contain digits."
                elif j != 0 and not addend_1[i][j].isnumeric():
                    break_function = True
                    message = "Error: Numbers must only contain digits."

            if len(addend_1[i]) > 5 and addend_1[i][0] == '-':
                break_function = True
                message = "Error: Numbers cannot be more than four digits."

            elif len(addend_1[i]) > 4 and addend_1[i][0] != '-':
                break_function = True
                message = "Error: Numbers cannot be more than four digits."
                
            operation.append(problem_list[i].split(' ')[1])

            if operation[i] != "+" and operation[i] != "-":
                break_function = True
                message = "Error: Operator must be '+' or '-'."
                
            addend_2.append(problem_list[i].split(' ')[2])

            for j in range(len(addend_2[i])):
                if j == 0 and not addend_2[i][j].isnumeric() and addend_2[i][j] != '-':
                    break_function = True
                    message = "Error: Numbers must only contain digits."
                elif j != 0 and not addend_2[i][j].isnumeric():
                    break_function = True
                    message = "Error: Numbers must only contain digits."

            if len(addend_2[i]) > 5 and addend_2[i][0] == '-':
                break_function = True
                message = "Error: Numbers cannot be more than four digits."

            elif len(addend_2[i]) > 4 and addend_2[i][0] != '-':
                break_function = True
                message = "Error: Numbers cannot be more than four digits."

            if break_function:
                break

            if operation[i] == "+":
                results.append(str(int(addend_1[i]) + int(addend_2[i])))

            if operation[i] == "-":
                results.append(str(int(addend_1[i]) - int(addend_2[i])))
            
            if len(addend_1[i]) < len(addend_2[i]):
                largest = len(addend_2[i])
                addend_1[i] = (len(addend_2[i]) - len(addend_1[i])) * " " + addend_1[i]
                line.append('--' + len(addend_2[i]) * "-")
            else:
                largest = len(addend_1[i])
                addend_2[i] = (len(addend_1[i]) - len(addend_2[i])) * " " + addend_2[i]
                line.append('--' + len(addend_1[i]) * "-")
            
            if len(results[i]) <= largest:
                results[i] = "  " + (largest - len(results[i])) * " " + results[i]

            else:
                results[i] = (2 - (len(results[i]) - largest)) * " " + results[i]

        if break_function:
            arranged_problems = message

        else:
            arranged_problems += "  "
            
            for i in range(len(operation)):
                if i < len(operation) - 1:
                    arranged_problems += addend_1[i] + "      "
                else:
                    arranged_problems += addend_1[i]

            arranged_problems += "\n"

            for i in range(len(operation)):
                if i < len(operation) - 1:
                    arranged_problems += operation[i] + " " + addend_2[i] + "    "
                else:
                    arranged_problems += operation[i] + " " + addend_2[i]

            arranged_problems += "\n"

            for i in range(len(operation)):
                if i < len(operation) - 1:
                    arranged_problems += line[i] + "    "
                else:
                    arranged_problems += line[i]

            if print_result:
                arranged_problems += "\n"

                for i in range(len(operation)):
                    if i < len(operation) - 1:
                        arranged_problems += results[i] + "    "
                    else:
                        arranged_problems += results[i]

    return arranged_problems