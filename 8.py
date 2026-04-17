class Solution:
    def reverseStr(s: str):


        s: str = input()

        l = list(s)
        l.reverse()
        return "".join(l)
 
    if __name__ == "__main__":
    # 1. Create an instance of the class
        sol = Solution()
    
    # 2. Get input from the user
        user_input = input("Enter a string to reverse: ")
    
    # 3. Call the method and store the result
        result = sol.reverseStr(user_input)
    
    # 4. Show the result
        print(f"Reversed string: {result}")