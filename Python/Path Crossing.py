class Solution:
    def isPathCrossing(self, path: str) -> bool:
        stackTraveled = [[0,0]]
        og = [0,0]

        for c in path:
            if c== "N":
                og[1] +=1
            elif c== "S":
                og[1] -=1
            elif c== "E":
                og[0] +=1
            elif c== "W":
                og[0] -=1


            if og in stackTraveled:
                return True
            stackTraveled.append([og[0],og[1]])

            print(stackTraveled)
        print(stackTraveled)
        return False
