import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!



def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern=="\\d":
        return len(input_line.translate(str.maketrans('','','0123456789'))) != len(input_line)
    elif pattern=="\\w":
        return len(input_line.translate(str.maketrans('','','abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))) != len(input_line)
    elif pattern[0]=='[' and pattern[-1]==']':
        actual_pattern=pattern[1:-1]
        if actual_pattern[0]=='^':
            return not any(char in actual_pattern for char in input_line)
        else:
            for char in actual_pattern:
                if char in input_line:
                    return True
            return False
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    print(pattern)
    print(input_line)
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)


    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
