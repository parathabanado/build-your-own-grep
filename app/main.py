import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!
def match_character_string(text,pattern):
    if pattern[0]=='^':
        return not any(char in pattern for char in text)
    else:
        return any(char in pattern for char in text)


def match_pattern(text, pattern):
    j=-1
    i=0
    if pattern[0]=='\\':
        if pattern[1]=='d':
            for k in text:
                if k.isdigit():
                    j=text.find(k)
                    i=2
                    break
        elif pattern[1]=='w':
            for k in text:
                if k.isalnum():
                    j=text.find(k)
                    i=2
                    break
    else:
        for k in text:
            if k==pattern[0]:
                j=text.find(k)
                i=1
    if j==-1:
        return False  
    # print(f"First Match at {j} which is {text[j]}")
    j+=1
    call_j=j
    while i<len(pattern) and j<len(text):
        if pattern[i]=="\\":
            i+=1
            if pattern[i]=="d":
                if text[j].isdigit()==False:
                    return False
                else:
                    j+=1
            elif pattern[i]=="w":
                if text[j].isalnum==False:
                    return False
                else:
                    j+=1
        else:
            if pattern[i]!=text[j]:
                return False
            else:
                j+=1
        i+=1
    if(i<len(pattern) and j>=len(pattern)):
        return match_pattern(text[call_j::],pattern)
    return True
    
    
                


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    print(pattern)
    print(input_line)
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)


    # Uncomment this block to pass the first stage
    if(pattern[0]=='[' and pattern[-1]==']'):
        if match_character_string(input_line,pattern[1:-1]):
            exit(0)
        else:
            exit(1)
    else:
        if match_pattern(input_line, pattern):
            exit(0)
        else:
            exit(1)


if __name__ == "__main__":
    main()
