class Example:
    def __init__(self):
        return

    def main(self): # コメントなのだ
        print('Hello World')
        self.hello_world()
        print(self.str_join('Hello', 'World.'))
        print(self.equals('A', 'A'))
        for i in range(5):
            print(i)
        for j in [1, 2, 3]:
            print(j)
        aDict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        aList = [1, 2, 3]
        anotherList = [item if item < 10 else item + 10 for item in aList]
        n = 5
        it = [1, 3, 5, 7, 9]
        aNumber = 111
        aNumber += 12
        aNumber -= 0
        for k in aDict:
            print(aDict[k])
        self.f(1, 2, 3, 4, 5)
    
    # 追加
    def hello_world(self):
        hello = 'Hello World'
        return hello

    def str_join(self, *strings):
        res = ''
        for aString in strings:
            res += aString
        # return ''.join(strings)
        return res

    def equals(self, aString='', anotherString=''):
        return aString == anotherString
    
    def f(self, a, b=2, *c, **d):
        while b > 0:
            print(b)
            b -= 1
        return

def aFunction():
    a = 5
    b = a - 1
    print(b)

if __name__ == '__main__':
    example = Example()
    example.main()