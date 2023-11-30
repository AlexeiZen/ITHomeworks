class Calc1:
    vowels = 'eyuioa'
    consonants = 'qwrtpsdfghjklzxcvbnm'

    def __init__(self, value):
        self.value = value

    def lenght(self):
        return self.value, len(str(self.value))

    def result(self):
        vow = ''
        cons = ''
        sum_even = 0
        if type(self.value) == str:
            for item in self.value:
                if item in Calc1.vowels:
                    vow += item
                elif item in Calc1.consonants:
                    cons += item
            multip = len(vow) * len(cons)
            if multip <= len(self.value):
                return vow
            elif multip > len(self.value):
                return cons
        elif type(self.value) == int:
            for num in str(self.value):
                if int(num) % 2 == 0:
                    sum_even += int(num)
            res = sum_even * len(str(self.value))
            return res


str_res = Calc1('aeyuighdhdhfd')
print(str_res.result(), ' ', str_res.lenght())
int_res = Calc1(123456789)
print(int_res.result(), ' ', int_res.lenght())
