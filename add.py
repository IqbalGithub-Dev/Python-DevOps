class calculator:
    def sum(self,a,b):
        self.a = a
        self.b = b
        return(a+b)
    def div(self,a,b):
        self.a = a
        self.b = b
        if b==0:
            print("division cant be happen")
        return (a/b)

