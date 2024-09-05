def format_indian_currency(number):
    integer_part, decimal_part = str(number).split('.')
    integer_part = integer_part[::-1]
    first_group = integer_part[:3]
    remaining_groups = integer_part[3:]
    formatted = first_group + ''.join([',' + remaining_groups[i:i+2] for i in range(0, len(remaining_groups), 2)])
    return formatted[::-1] + '.' + decimal_part


#eg: number = 123456.7891
num = float(input("enter currency amount: "))
formatted_number = format_indian_currency(num)
print("Formatted Indian Currency:", formatted_number)
