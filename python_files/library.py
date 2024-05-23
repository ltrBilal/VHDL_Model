class Library:
    code = ""
    file1 = open('./library.txt', 'r')
    Lines = file1.readlines()

    for line in Lines:
        code += line
    
    def library_vhdl(self):
        return self.code