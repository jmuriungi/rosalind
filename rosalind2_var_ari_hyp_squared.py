def main():
    a = 948; b = 914
    hypotenuse_square(a, b)

def hypotenuse_square(a, b):
    hypotenuse_squared = (a*a) + (b*b)
    print(hypotenuse_squared)
    return hypotenuse_squared

if __name__ == "__main__":
    main()
