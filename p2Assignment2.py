import re #will be used for checking if str matches a expression 
import sys #used for command line interface
class Preprocessor:#class made for task 1
    def __init__(self, input_file):#init constructor will be useed for initializing below attrbutes 
        self.input_file = input_file
        self.output_file = "out1.py"
        self.file_content = ""

    def read_file(self):
        try:
            with open(self.input_file, 'r') as file:#file will be opened in read mode and with is used so that the file closes when we move forward
                self.file_content = file.read() #this will read the file and store in self.file content
        except FileNotFoundError:#this will help if there is no file it will exit the program and give error msg
            print(f"Error: File '{self.input_file}' not found.")
            sys.exit(1)

    def eliminate_blank_lines(self):
        lines = [line for line in self.file_content.splitlines() if line.strip()]
        self.file_content = '\n'.join(lines)

        with open(self.output_file, 'w') as file:
            file.write(self.file_content)
#in the eliminate balnk line method i used for loop and stored the file content in list and for loop will go through each line and strip method will help i removing blank lines 
    def eliminate_hashTQC(self):
        lines = self.file_content.splitlines()
        result_lines = []
        x = False
        for line in lines:            
            if '#' in line:        
                line = line.split('#', 1)[0]            
            if '"""' in line:                
                inside_quote_block = not inside_quote_block                
                if inside_quote_block:
                    continue            
            if line.strip():
                result_lines.append(line)       
        self.file_content = '\n'.join(result_lines)        
        with open(self.output_file, 'w') as file:
            file.write(self.file_content)
    def eliminate_tabs_spaces(self):       
        self.file_content = ' '.join(self.file_content.split())       
        with open(self.output_file, 'w') as file:
            file.write(self.file_content)
    def eliminate_imports_annotations(self):        
        lines = [line for line in self.file_content.splitlines() if not line.startswith(('import', 'from', '@'))]        
        self.file_content = '\n'.join(lines)       
        with open(self.output_file, 'w') as file:
            file.write(self.file_content)
#the eliminate comment method i used strip and
# conditional statemnets if there will be # or a """" in input fie 
# using the strip method it will remove the comment and using /n 
# and .join will make the result get concatanated          
#the space methode will use split method and imports method will
# use startwith which will ceck if the line starts with 
# import from or @ it will not show in output file
#      
class Processor:#class mad efor task 2
    def __init__(self, input_file):
        self.input_file = input_file
        self.output_file = "out2.py"
        self.sen = []

    def AddSentinalValue(self):
        try:
            with open(self.input_file, 'r') as file:
                content = file.read()
                # open file in read mode
                self.sen.extend(content.replace('\n', ''))
        except FileNotFoundError:
            print(f"Error: File '{self.input_file}' not found.")
            sys.exit(1)
    def write_sen_to_file(self):       
        self.sen.append('$')        
        with open(self.output_file, 'w') as file:            
            file.write(''.join(self.sen))
    def display_output(self):
        with open(self.output_file, 'r') as file:
            content = file.read()
            print(content)

class LexicalAnalyzer:#class made for lexical analyzer
    def __init__(self, input_file):
        self.input_file = input_file
        self.lexemes = []
    def read_file(self):
        try:
            with open(self.input_file, 'r') as file:
                content = file.read()                
                self.lexemes = re.findall(r'\b\w+|[()+=\d]\b', content)
        except FileNotFoundError:
            print(f"Error: File '{self.input_file}' not found.")
            sys.exit(1)

    def Lexemmes(self):
        for lexeme in self.lexemes:
            print(f"Lexeme: {lexeme}")

  

#program testing for task 1
preprocessor = Preprocessor("myFile.txt")
preprocessor.read_file()
preprocessor.eliminate_blank_lines()
preprocessor.eliminate_hashTQC()
preprocessor.eliminate_tabs_spaces
preprocessor.eliminate_imports_annotations()
#program testing for task 2
processor = Processor("out1.py")
processor.AddSentinalValue()
processor.write_sen_to_file()
processor.display_output()
#program testing for task 3
lexicalanalyzer = LexicalAnalyzer("out2.py")
lexicalanalyzer.read_file()
lexicalanalyzer.Lexemmes()

