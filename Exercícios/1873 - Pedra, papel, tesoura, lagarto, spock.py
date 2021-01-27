C = int(input())
for i in range(0, C):
    r, s = input().split(" ")
    s = str(s)
    r = str(r)
    
    if (s == 'tesoura') and (r=='papel'):
        print("sheldon")
    elif (r == 'tesoura') and (s=='papel'):
        print("rajesh")
    
    elif (s == 'papel') and (r=='pedra'):
        print("sheldon")
    elif (r == 'papel') and (s=='pedra'):
        print("rajesh")
    
    elif (s == 'pedra') and (r=='lagarto'):
        print("sheldon")
    elif (r == 'pedra') and (s=='lagarto'):
        print("rajesh")
    
    elif (s == 'lagarto') and (r=='spock'):
        print("sheldon")
    elif (r == 'lagarto') and (s=='spock'):
        print("rajesh")
    
    elif (s == 'spock') and (r=='tesoura'):
        print("sheldon")
    elif (r == 'spock') and (s=='tesoura'):
        print("rajesh")
    
    elif (s == 'tesoura') and (r=='lagarto'):
        print("sheldon")
    elif (r == 'tesoura') and (s=='lagarto'):
        print("rajesh")
    
    elif (s == 'lagarto') and (r=='papel'):
        print("sheldon")
    elif (r == 'lagarto') and (s=='papel'):
        print("rajesh")
    
    elif (s == 'papel') and (r=='spock'):
        print("sheldon")
    elif (r == 'papel') and (s=='spock'):
        print("rajesh")
    
    elif (s == 'spock') and (r=='pedra'):
        print("sheldon")
    elif (r == 'spock') and (s=='pedra'):
        print("rajesh")
    
    elif (s == 'pedra') and (r=='tesoura'):
        print("sheldon")
    elif (r == 'pedra') and (s=='tesoura'):
        print("rajesh")
        
    elif(s == r):
        print("empate")