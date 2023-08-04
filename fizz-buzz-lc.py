class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ls_fb = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                ls_fb.append("FizzBuzz") 
            elif i % 3 == 0:
                ls_fb.append("Fizz") 
            elif i % 5 == 0:
                ls_fb.append("Buzz")
            else:
                ls_fb.append(str(i))
        return ls_fb