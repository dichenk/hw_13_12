class MyList(list):
    
    def __new__(cls, *args, **kwargs):
        print('magic method is working')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, lst):
        print('magic method is working')
        super().__init__(lst)

    def __len__(self):
        print('magic method is working')
        return super().__len__()

    def __str__(self):
        print('magic method is working')
        return super().__str__()

    def __repr__(self):
        print('magic method is working')
        return super().__repr__()

lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))
