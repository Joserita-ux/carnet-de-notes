NM = 42
essais = 0
MAX = 9
score = 100

Proposition = int(input('urnumber : '))
while Proposition != NM and essais<MAX :
    essais = essais + 1
    score= score - 10
    if Proposition < NM :
        print('trop petit ma go')
    if Proposition > NM :
        print('trop gros ma go')
    Proposition = int(input('urnumber : '))
    
if Proposition == NM:
    print('thats my ponduuu!')
else:
    print('u lil fumbwa')
    
print(f"you score is:{score}")
            
