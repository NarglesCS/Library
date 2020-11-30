class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #Step 1 get slope of a line
        rise = coordinates[1][1] - coordinates[0][1]
        run = coordinates[1][0] - coordinates[0][0]
        if (run == 0):
            slope = 0
            b = 0
        elif(rise == 0):
            slope = "inf"
            b = 0
        else:
            slope = rise/run
            b = coordinates[0][1] - slope*coordinates[0][0]
        for coord in coordinates:
            if (slope == 0):
                if (coord[0] != coordinates[0][0]):
                    return False
            elif (slope == "inf"):
                if (coord[1] != coordinates[0][1]):
                    return False
            elif (coord[1] != slope*coord[0] + b):
                return False

        return True
