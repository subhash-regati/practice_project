k=open('text.txt','r')
with open('text.txt','r') as rf,open('test_copy.txt','r+') as wf:
    str=rf.read()
    str1=rf

    count1=0
    count2=0
    for line in wf:
        print(line)
        wf.write(line.replace('RggbLogarithmicMasterWindowA','VideoStream1'))
        wf.write(line.replace('RggbLogarithmicMasterWindowB', 'VideoStream2'))
    for i in range(0,len(str)):
        if(str[i]=='R'):
            if(str[i:i+28]=='RggbLogarithmicMasterWindowA'):
                count1 +=1
            elif(str[i:i+28]=='RggbLogarithmicMasterWindowB'):
                count2 +=1
            else:
                pass
print('RggbLogarithmicMasterWindowA is repeated as many as ' ,count1,' times\n' )
print('RggbLogarithmicMasterWindowB is repeated as many as ',count2,' times' )


