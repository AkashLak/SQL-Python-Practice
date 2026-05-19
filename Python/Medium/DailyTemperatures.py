class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        #Default of 0 if no warmer days
        answer = [0] * size
        #Stores indices
        stack = []

        for i, temp in enumerate(temperatures):
            #Checking if current temp is warmer than the temp at the index on top of the stack
            while stack and temp > temperatures[stack[-1]]:
                #Removing index of colder day
                j = stack.pop()
                #Days until a warmer day occurs (stored in answer list)
                answer[j] = i - j
            #Current index, thats waiting for a warmer day
            stack.append(i)             
        return answer