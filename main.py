class Product:
    def __init__(self, in_str, out_str):
        self.in_str = in_str
        self.out_str = out_str
    def get_not_term(cur_buf, r_val):
        res = []
        for letter in r_val:
            if(ord(letter) >= 65 and ord(letter) <= 90 and (letter not in cur_buf)):
                res.append(letter)
        return res
    def parse_string(buff,str):
        frst = str[0]
        for elem in str[str.find(">")+1:].split('|'):
            buff.append(Product(frst,elem))
        return buff
    def remove_useless(prods):
        buff = []
        for elem in prods:
            if(elem.in_str == "S"):
                for el in Product.get_not_term(cur_buf=buff, r_val=elem.out_str):
                   buff.append(el)
        new_buff = []
        for prod in prods:
            if(prod.in_str not in new_buff):
                new_buff.append(prod.in_str)
            pool  = Product.get_not_term(cur_buf=new_buff, r_val=prod.out_str)
            for r_value in pool:
                if(r_value not in new_buff):
                    new_buff.append(r_value)
        used = []
        while len(buff) != 0:
            l_value = buff[0]
            for prod in prods:
                if(l_value == prod.in_str):
                    if(l_value in new_buff):
                        new_buff.remove(l_value)
                        used.append(l_value)
                    for letter in Product.get_not_term(cur_buf=buff, r_val = prod.out_str):
                        if(letter not in used and letter not in buff):
                            buff.append(letter)
            del buff[0]
        new_buff.remove("S")
        new_prods = []
        for prod in prods:
            if(prod.in_str not in new_buff ):
                flag = True
                for n_prod in new_prods:
                    if prod.in_str in n_prod.in_str:
                        flag = False
                        n_prod.out_str += "|" + prod.out_str
                if(flag == True):
                    new_prods.append(prod)
        return new_prods
    def print_all(prods):
        for prod in prods:
            print(prod.in_str + " -> " + prod.out_str)

if __name__ == '__main__':
    buff = []
    #Нужно заполнить!!!!!
    file_path = "";
    with open(file_path, 'r') as file:
        data = file.readlines()
        print("Original Grammar: ")
        for line in data:
            print(line.replace('\n', ''))
            Product.parse_string(buff=buff, str=line.replace('\n', ''))
    print()
    print("Result grammar:")
    Product.print_all(Product.remove_useless(buff))
    #w_r.add_prod(pr)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
