class Seat:
    def __init__(self, block, row, column, classSeat, passenger):
        self.block = block
        self.row = row
        self.column = column
        self.classSeat = classSeat
        self.passenger = passenger


class AirPlane:
    def __init__(self):
        self.resArr = []

    def sortSeats(self, inputArr):
        for block in range(1, len(inputArr) + 1):
            for column in range(1, inputArr[block - 1][0] + 1):
                for row in range(1, inputArr[block - 1][1]):
                    if block == 1 and column == 1 and inputArr[block - 1][0] > 1:
                        new_Seat = Seat(self, block, row, column, 2)
                        self.resArr.append(new_Seat)
                    elif (
                        block == len(inputArr)
                        and column == inputArr[block - 1][0]
                        and inputArr[block - 1][0] > 1
                    ):
                        new_Seat = Seat(self, block, column, row, 2)
                        self.resArr.append(new_Seat)
                    elif column == 1 or column == inputArr[block - 1][0]:
                        new_Seat = Seat(self, block, column, row, 1)
                        self.resArr.append(new_Seat)
                    else:
                        new_Seat = Seat(self, block, column, row, 3)
                        self.resArr.append(new_Seat)

    def seatPassengers(self, queue):
        if len(self.resArr) < queue:
            for i in range(0, len(self.resArr)):
                self.resArr[i].passenger = i + 1
        else:
            for i in range(0, queue):
                self.resArr[i].passenger = i + 1


result = []
seats = [[3, 4], [4, 5], [2, 3], [3, 4]]
queue = 30

airplane = AirPlane()
airplane.sortSeats(seats)
airplane.seatPassengers(queue)

for i in range(0, len(airplane.resArr)):
    print("block: ", airplane.resArr[i].block)
    print("row: ", airplane.resArr[i].row)
    print("column: ", airplane.resArr[i].column)
    print("classSeat: ", airplane.resArr[i].classSeat)
    print("passenger: ", airplane.resArr[i].passenger)
    print("\n")
