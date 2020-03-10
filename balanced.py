# rjcastaneda
# Filename: balanced.py

# Function to remove comments
# Takes into account block comments
def removeCom(input):
    NOT_FOUND = -1

    output = open("./Driver.nocom","w")
    blockCommentFound = False
    for line in input:
        if blockCommentFound:
            deLimIndx = line.find("*/")
            if deLimIndx == NOT_FOUND:
                continue
            else:
                blockCommentFound = False
                noComLine = line.rsplit("*/")
                output.write(noComLine[1])
                continue

        if "//" in line and blockCommentFound != True:
            noComLine = line.rsplit("//")
            output.write(noComLine[0])
            continue

        if "/*" in line and blockCommentFound != True:
            deLimIndx = line.find("*/")
            if deLimIndx != NOT_FOUND:
                noComLine = line.rsplit("/*")    
                output.write(noComLine[0])
                continue
            else:
                blockCommentFound = True
                continue
      
        else: 
            output.write(line)
      
    output.close()          

# Function to detect if element is within quotes
# Finds the first and last index of the quotes and
# compares them to where the index of the element
# is at.
def quoteCheck(input,index):
    LAST_INDEX = len(input)
    NEXT_INDEX = 1
    NOT_FOUND = -1

    queue = []
    x = 0
    while x < LAST_INDEX:
        Delim = input.find("\"",x,LAST_INDEX)    
        if(Delim != NOT_FOUND):
            queue.append(Delim)
            x = Delim
        Delim = NOT_FOUND    
        x += NEXT_INDEX 
       
            
    for element in queue:
        begDelim = queue.pop(0)
        endDelim = queue.pop(0)
        if index >= begDelim and index <= endDelim:
            return True
    return False

def balanced(input):
    stack = []
    for line in input:
        for index, element in enumerate(line):
            if element == '(':
                if quoteCheck(line,index):
                    continue
                stack.append(element)

            if element == '[':
                if quoteCheck(line,index):
                    continue
                stack.append(element)
            
            if element == '{':
                if quoteCheck(line,index):
                    continue
                stack.append(element)
            
            if element == ')':
                if quoteCheck(line,index):
                    continue
                
                # If stack is empty
                # You cannot pop from stack
                # Meaning it is not balanced           
                if not stack:
                    return False    

                temp = stack.pop()
                if temp != '(':
                    return False
            
            if element == ']':
                if quoteCheck(line,index):
                    continue

                if not stack:
                    return False    

                temp = stack.pop()
                if temp != '[':
                    return False
            
            if element == '}':
                if quoteCheck(line,index):
                    continue
     
                if not stack:
                    return False    

                temp = stack.pop()
                if temp != '{':
                    return False

    # Checks if stack is still full
    # If it is, it is not balanced                  
    if stack:
        return False
    return True
                   
def main():
    file = open("./Driver.java","r") 
    removeCom(file)
    file.close()

    file = open("./Driver.nocom","r")
    if balanced(file):
        print("The code is balanced! :)")
    else:
        print("The code is not balanced. :(")
    file.close()
    

if __name__ == "__main__":
    main()

