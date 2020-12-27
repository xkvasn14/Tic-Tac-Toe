# write your code here
#name = input()
#print("Enter cells: " + name)
name = "         "
code = []
code[:0] = name
pl1 = code[0] 
pl2 = code[1]
pl3 = code[2]
pl4 = code[3]
pl5 = code[4]
pl6 = code[5]
pl7 = code[6]
pl8 = code[7]
pl9 = code[8]
print("---------")
print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
print("---------")


switcher = "X"
runner = True
while runner:
    coords = input()
    print("Enter the coordinates: " + coords)
    coord = coords.split()


    if coord[0].isnumeric() == False or coord[1].isnumeric() == False:
        print("You should enter numbers!")
    else:
        if int(coord[0]) < 1 or int(coord[0]) > 3 or int(coord[1]) < 1 or int(coord[1]) > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            if int(coord[0]) == 1 and int(coord[1]) == 1 and pl1 != "X" and pl1 != "O":
                pl1 = switcher
                print("---------")
                print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
                print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
                print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
                print("---------")
                #runner = False
            elif int(coord[0]) == 1 and int(coord[1]) == 2 and pl2 != "X" and pl2 != "O":
                pl2 = switcher
                print("---------")
                print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
                print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
                print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
                print("---------")
                #runner = False
            elif int(coord[0]) == 1 and int(coord[1]) == 3 and pl3 != "X" and pl3 != "O":
                pl3 = switcher
                print("---------")
                print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
                print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
                print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
                print("---------")
                #runner = False
            elif int(coord[0]) == 2 and int(coord[1]) == 1 and pl4 != "X" and pl4 != "O":
                pl4 = switcher
                print("---------")
                print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
                print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
                print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
                print("---------")
                #runner = False
            elif int(coord[0]) == 2 and int(coord[1]) == 2 and pl5 != "X" and pl5 != "O":
                pl5 = switcher
                print("---------")
                print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
                print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
                print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
                print("---------")
                #runner = False
            elif int(coord[0]) == 2 and int(coord[1]) == 3 and pl6 != "X" and pl6 != "O":
                pl6 = switcher
                print("---------")
                print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
                print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
                print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
                print("---------")
                #runner = False
            elif int(coord[0]) == 3 and int(coord[1]) == 1 and pl7 != "X" and pl7 != "O":
                pl7 = switcher
                print("---------")
                print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
                print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
                print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
                print("---------")
                #runner = False
            elif int(coord[0]) == 3 and int(coord[1]) == 2 and pl8 != "X" and pl8 != "O":
                pl8 = switcher
                print("---------")
                print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
                print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
                print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
                print("---------")
                #runner = False
            elif int(coord[0]) == 3 and int(coord[1]) == 3 and pl9 != "X" and pl9 != "O":
                pl9 = switcher
                print("---------")
                print("|" + " " + pl1 + " " + pl2 + " " + pl3 + " " + "|")
                print("|" + " " + pl4 + " " + pl5 + " " + pl6 + " " + "|")
                print("|" + " " + pl7 + " " + pl8 + " " + pl9 + " " + "|")
                print("---------")
                #runner = False
            else:
                print("This cell is occupied! Choose another one!")


    if switcher == "X":
        switcher = "O"
    elif switcher == "O":
        switcher = "X"        


    row1 = [pl1,pl2,pl3]
    row2 = [pl4,pl5,pl6]
    row3 = [pl7,pl8,pl9]
    col1 = [pl1,pl4,pl7]
    col2 = [pl2,pl5,pl8]
    col3 = [pl3,pl6,pl9]
    diagl = [pl1,pl5,pl9]
    diagr = [pl3,pl5,pl7]

    cube = [row1,row2,row3,col1,col2,col3,diagl,diagr]
    rows = [row1,row2,row3]

    if True:
        winX = False
        winO = False

        if row1[0] == row1[1] == row1[2] == "X":
            winX = True
        if row1[0] == row1[1] == row1[2] == "O":
            winO = True
        if row2[0] == row2[1] == row2[2] == "X":
            winX = True
        if row2[0] == row2[1] == row2[2] == "O":
            winO = True
        if row3[0] == row3[1] == row3[2] == "X":
            winX = True
        if row3[0] == row3[1] == row3[2] == "O":
            winO = True
        if col1[0] == col1[1] == col1[2] == "X":
            winX = True
        if col1[0] == col1[1] == col1[2] == "O":
            winO = True
        if col2[0] == col2[1] == col2[2] == "X":
            winX = True
        if col2[0] == col2[1] == col2[2] == "O":
            winO = True
        if col3[0] == col3[1] == col3[2] == "X":
            winX = True
        if col3[0] == col3[1] == col3[2] == "O":
            winO = True
        if diagl[0] == diagl[1] == diagl[2] == "X":  
            winX = True
        if diagl[0] == diagl[1] == diagl[2] == "O":
            winO = True
        if diagr[0] == diagr[1] == diagr[2] == "X":
            winX = True  
        if diagr[0] == diagr[1] == diagr[2] == "O":
            winO = True
    X = 0
    O = 0
    exit = False
    for i in rows:
        for j in i:
            if j == " " or j == "_":
                exit = True
            if j == "X":
                X +=1
            if j == "O":
                O +=1
            
    if X+1==O or X==O or X-1==O:
        a = True
    else:
        exit = False
        winX = True
        winO = True
        
   


   
    if winX == True and winO == True:
        print("Impossible")
        #runner = False
        True
    elif winX == True and winO == False:
        print("X wins")
        runner = False
    elif winX == False and winO == True:
        print("O wins")
        runner = False
    elif winX == False and winX == False and (X + O == 9):
        print("Draw")
        runner = False
