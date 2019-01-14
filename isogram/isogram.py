
def is_isogram(string):
   if type(string) != str:
       raise Exception("Argument should be string")
   elif string== "":
       return True
   elif (string,str) and len(string) != 0:
       string = string.lower()
       if'-' in string:
            new_string = string.replace('-','')
            if len(new_string)==len(set(new_string)):
                return True
            else:
                return False
       elif ' ' in string:
            string_new = string.replace(" ", "")
            if len(string_new) == len(set(string_new)):
                return True
            else:
                return False
       elif len(string)==len(set(string)):
            return True
       else:
            return False
        
        
    