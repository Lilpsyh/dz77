def print_operation_table(num_rows,num_columns):
    for i in range(1,num_columns+1):
        for j in range(1,num_rows+1):
            print(f"{i*j}",end=" ") 
        print()
print_operation_table(6,6)



