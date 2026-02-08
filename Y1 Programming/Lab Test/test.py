file_name = "products.txt"
prods = dict()
with open(file_name, 'r') as data_file:
    field = ''
    char = data_file.read(1)
    i = 0
    while char:
        if char not in ('|', '\n'):
            field += char
        else:
            #print(field, i)
            if i == 0:
                barcode = field
            elif i == 1:
                name = field
            elif i == 2:
                price = field
            elif i == 3:
                date = field
            elif i == 4:
                quantity = field

            field = ''
            i += 1

        if char == '\n':
            i = 0
            prods[barcode] = (name, price, date, quantity)
        
        char = data_file.read(1)
    
    #print(prods)

barcode = input("\n\nenter a barcode: ")
details = prods.get(barcode, "")

if details:
    print("Name:",details[0])
    print("Price:",details[1])
    print("Exp date:",details[2])
    print("Quantity:",details[3])
else:
    print("Product does not exist")