
training_Example = [["Sunny", "Warm", "Cool", "Yes"],
                    ["Cloudy", "Warm", "Cool", "No"],
                    ["Sunny", "Cool", "Warm", "Yes"]]

hypothes = ["%", "%", "%"]

for row in range(0, 3):

     if training_Example[row][3].__eq__("Yes"):

        for column in range(0, 3):

            if hypothes[column].__eq__("%"):
                hypothes[column] = training_Example[row][column]

            elif training_Example[row][column] != hypothes[column]:
                hypothes[column] = "?"

            elif training_Example[row][column] == hypothes[column]:
                hypothes[column] = training_Example[row][column]

     print("Hyposis" , row , hypothes)
