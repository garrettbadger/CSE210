def main():
    rows = int(input("How many rows do you want in your table?"))
    range_size = rows + 1
    for row_number in range(1, range_size):
        for col_number in range(1, range_size):
            
            number = row_number * col_number

            print(f"{number:5}", end=" ")

        print()
    

main()