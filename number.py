def devin(NM):
    essais = 0
    MAX= 9
    score = 100
    proposition = int(input('ton nombre(seulement des nombres entiers) : '))
    while proposition != NM and essais<MAX :
        essais = essais + 1
        score= score - 10
        if proposition < NM :
            print('trop petit ma go')
        if proposition > NM :
            print('trop gros ma go')
        proposition = int(input('urnumber : '))
    
if proposition == NM:
    print('thats my ponduuu!')
else:
    print('u lil fumbwa')
    
return score
appel = devin(42)
print(appel)
            
