
training_Example = [["Sunny", "Warm", "Same", "Yes"],
                    ["Cloudy", "Warm", "Same", "No"],
                    ["Sunny", "Cool", "Change", "Yes"]]

hypothes = ["?", "?", "?"]

sky = ["Sunny", "Cloudy", "Rainy"]
temp = ["Warm", "Cool"]
forecast = ["Same", "Change"]

print("H 0" , hypothes)

for row in range(0, 3):

    if training_Example[row][3].__eq__("No"):

        if training_Example[row][0] in sky:
            sky.remove(training_Example[row][0])

            for i in sky:
                hypothes[0] = i
                print("H",row , hypothes)

            sky.append(training_Example[row][0])

        if training_Example[row][1] in temp:
            temp.remove(training_Example[row][1])

            for i in temp:
                hypothes[0] = "?"
                hypothes[1] = i
                print("H",row ,hypothes)

            temp.append(training_Example[row][1])

        if training_Example[row][2] in forecast:
            forecast.remove(training_Example[row][2])

            for i in forecast:
                hypothes[0] = "?"
                hypothes[1] = "?"
                hypothes[2] = i
                print("H",row ,hypothes)

            forecast.append(training_Example[row][2])




