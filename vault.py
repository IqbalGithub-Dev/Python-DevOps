class Security_System:
    def __init__(self):
        self.pass_Word = "iqbal786"
        self.is_Lock = False
        self.failed_attempt = 0
        
    #rules 
    def enter_Code(self,guess):
        if self.is_Lock:
            raise PermissionError("SECURITY FAILURE , CALLED POLICE")
        
        if guess == self.pass_Word:
            self.failed_attempt =0
            return "Access Granted"
        
        else:
            self.failed_attempt += 1
            if self.failed_attempt >= 3:
                self.is_Lock = True
            raise ValueError("accesess denied")
            
