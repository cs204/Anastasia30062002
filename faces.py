def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    f = input()
    x = convert(f)
    print(x)

if __name__ == "__main__":
    main()
