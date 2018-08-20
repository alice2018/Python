# -*- coding: cp936 -*-


class code_emoji():
    def __init__(self, n):
        self.number = n
        self.code = [94, 95, 118, 62, 60, 39, 36]
    def __str__(self):
        return 'this is just a code emoji class!'
    def __order(self, func):
        func = getattr(func, '__name__')
        if func == "smile":
            return [self.code[0], self.code[1], self.code[0]]
        elif func == "peace":
            return [self.code[2], self.code[1], self.code[2]]
        elif func == "dizzy":
            return [self.code[3], self.code[1], self.code[4]]
        elif func == "greedy":
            return [self.code[-1], self.code[1], self.code[-1]]
        elif func == "nerd":
            return [self.code[-2], self.code[1], self.code[-2]]
    def smile(self):
        print "\n笑脸"
        for i in range(self.number):
            print "".join([chr(i) for i in self.__order(self.smile)])
    def dizzy(self):
        print "\n晕"
        for i in range(self.number):
            print "".join([chr(i) for i in self.__order(self.dizzy)])
    def peace(self):
        print "\n平静"
        for i in range(self.number):
            print "".join([chr(i) for i in self.__order(self.peace)])
    def greedy(self):
        print "\n贪婪"
        for i in range(self.number):
            print "".join([chr(i) for i in self.__order(self.greedy)])
    def nerd(self):
        print "\n毫无波动"
        for i in range(self.number):
            print "".join([chr(i) for i in self.__order(self.nerd)])
            
if __name__ == '__main__':
    a = code_emoji(2)
    a.smile()
    a.dizzy()
    a.peace()
    a.greedy()
    a.nerd()
