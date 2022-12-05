try:
    with open('testng.txt', 'w') as wf, open('text.txt', 'r') as rf:
        sr = rf.readlines()
        for i in sr:
            wf.write(i.replace('RggbLogarithmicMasterWindowA', 'Videostream1'))
            wf.write(i.replace('RggbLogarithmicMasterWindowB', 'Videostream2'))
            print(i)

        print(rf.readlines())
except:
    print("NO file found for Reading")
