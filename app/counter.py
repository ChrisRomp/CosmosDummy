'''Counter print and increment'''
class Counter:
    '''Counter print and increment'''
    Value = 0

    @staticmethod
    def increment():
        '''Increment counter'''
        Counter.Value += 1
        return Counter.Value
