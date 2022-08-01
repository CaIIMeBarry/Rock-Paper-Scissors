# sang kaqaz qeichi
import random
user_wins=0
pc_wins=0
draw=0
for i in range(10):
    a=['s','k','q']
    pc=random.choice(a)
    
    user=input('your turn :')
    
    if (pc=='s' and user=='q') or (pc=='q' and user=='k') or (pc=='k' and user=='s'):
        print('pc turn :',pc)
        pc_wins+=1
        
    elif (pc=='s' and user=='s') or (pc=='q' and user=='q') or (pc=='k' and user=='k'):
        print('pc turn :',pc)
        draw+=1
        
    else:
        print('pc turn :',pc)
        user_wins+=1
        
if pc_wins>user_wins:
    print('PC IS THE WINNER!!')
elif pc_wins<user_wins:
    print('USER IS THE WINNER!!')
elif pc_wins==user_wins:
    print('THE MATCH IS A DRAW')
print('Total match result =======>' ,  'PC wins :',pc_wins,    'USER wins :',user_wins ,    'DRAW :',draw)                        