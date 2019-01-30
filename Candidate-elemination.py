
training_Example = [["Sunny", "Warm", "Same", "Yes"],
                    ["Cloudy", "Warm", "Same", "No"],
                    ["Sunny", "Cool", "Change", "Yes"]]

sky = ["Sunny", "Cloudy", "Rainy"]
temp = ["Warm", "Cool"]
forecast = ["Same", "Change"]

G = ["?", "?", "?"]
S = ["%", "%", "%"]

print("S 0", S)
print("G 0", G)

li = []
copyList = []

for row in range(0, 3):

     if training_Example[row][3].__eq__("Yes"):

        for column in range(0, 3):

            if S[column].__eq__("%"):
                S[column] = training_Example[row][column]

            elif training_Example[row][column] != S[column]:
                S[column] = "?"

            elif training_Example[row][column] == S[column]:
                S[column] = training_Example[row][column]


        print("S" , (row + 1) , S)

        if li.__len__() == 0:
            print("G", (row + 1), G)
        elif li.__len__() > 0:
            for n in range(0, li.__len__(), 3):
                copyList = li[n:n+3]


                for greater in range(0, copyList.__len__()):
                    if copyList[greater] == S[greater]:
                        print("G", (row + 1), copyList)
                    break


     if training_Example[row][3].__eq__("No"):

         print("S", (row + 1), S)
         if training_Example[row][0] in sky:
             sky.remove(training_Example[row][0])

             for i in sky:
                 G[0] = i
                 print("G", (row+1), G)
                 li.extend(G)

             sky.extend(training_Example[row][0])

         if training_Example[row][1] in temp:
             temp.remove(training_Example[row][1])

             for i in temp:
                 G[0] = "?"
                 G[1] = i
                 print("G", (row+1), G)
                 li.extend(G)

             temp.extend(training_Example[row][1])

         if training_Example[row][2] in forecast:
             forecast.remove(training_Example[row][2])

             for i in forecast:
                 G[0] = "?"
                 G[1] = "?"
                 G[2] = i
                 print("G", (row+1), G)
                 li.extend(G)

             forecast.extend(training_Example[row][2])

