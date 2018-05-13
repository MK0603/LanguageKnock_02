'''
Created on 2018/05/13

'''

if __name__ == '__main__':
    patrol ="パトカー"
    taxi = "タクシー"
    for i in range(max([len(patrol),len(taxi)])):
        if patrol[i] !=None and taxi[i] != None:
            print(patrol[i]+taxi[i],end="")
