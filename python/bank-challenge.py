'''
Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.
'''
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        hold_array = []
        answer = 0
        for i in range(len(bank)):
            counter = 0
            for j in range(len(bank[i])):
                if bank[i][j] == '1':
                    counter = counter +1
            if counter != 0:
                hold_array.append(counter)
        
        #expect its a square bc of logic so minus two be
        #we need to last row
        i = 0
        while i < len(hold_array)-1:
            j = i+1
            answer = answer + (hold_array[i] * hold_array[j])
            i = i+1

        return answer
            