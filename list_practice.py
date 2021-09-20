def main():
    print("Add numbers to the list and type 0 when finished")
    listno = -1
    list = []
    while listno != 0:
        listno = int(input("Add a number to the list: "))
        list.append(listno)
    
    compute_total(list)
    
def compute_total(list):
    sum = 0
    for i in list:
        i + sum
    return sum




main()