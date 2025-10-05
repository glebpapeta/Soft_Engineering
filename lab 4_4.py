def main(x, *args):
    one = x
    two = sum(args)
    three = float(one + two) / len(args)
    print(f"one={one}\ntwo={two}\nthree={three}")
    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    print(main(1, 0, 2, -1, 0, -1, 1, 2))

