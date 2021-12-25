class Mathfunction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Enter values are ", self.x, self.y)

    def ADD(self):
        return self.x + self.y

    def Sub(self):
        return self.x - self.y

    def Mul(self):
        if self.x > self.y:
            return self.x * self.y
        else:
            return "Not Valid Input"

    def Div(self):
        return self.x / self.y

    def check_prime(self):
        if self.x % 2 == 0:
            print("Given number is prime number")
        else:
            print("Given number is not a prime number")

    def square(self):
        return self.x * self.x, self.y * self.y


b = Mathfunction(10, 5)

s = b.square()


print(f"Square of given numbers are", s)


b.check_prime()
