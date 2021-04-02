
alpha = 'P'

Clauses = [['~F', '~D', 'P'],
           ['F'],
           ['D'],
           ['~P']]


def change(x):
    if '~' in x:
        return x.replace('~', '')
    else:
        return '~'+x



def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


NAlpha = [change(alpha)]
Clauses.append(NAlpha)
print(Clauses)



def TTEntail(Clauses):

    Copy_Clause = []

    test = Clauses[:]

    #Res_Clause = []
    #Res_Constant = ''

    for row in range(0, Clauses.__len__()):
        Res_Clause = Clauses[row]

        for i in range(0, Res_Clause.__len__()):
            Res_Constant = Res_Clause[i]

            ex = change(Res_Constant)
            
            for n in range(row+1, Clauses.__len__()):
                if Clauses[n].__contains__(ex):
                    Copy_Clause.extend(Clauses[n])
                    Copy_Clause.extend(Res_Clause)
                    Copy_Clause.remove(ex)
                    Copy_Clause.remove(Res_Constant)

                    Clauses.append(Remove(Copy_Clause))

                    if Copy_Clause == []:
                        print(Remove(Clauses))
                        return 'KB |= alpha'

                    Copy_Clause.clear()

            print(Remove(Clauses))

            if test == Clauses:
                return 'KB ~|= alpha'
            test = Clauses[:]

x = TTEntail(Clauses)
print(x)