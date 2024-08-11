import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!



def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif len(pattern) == 2:
        if pattern=="\d":
            return len(input_line.translate(str.maketrans('','','0123456789'))) != len(input_line)

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
