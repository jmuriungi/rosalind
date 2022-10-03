# def main():
#     s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
#     a = 22; b = 27; c = 97; d = 102
#     slice_string(s, a, b, c, d)

# def slice_string(s, a, b, c, d):
s = "9FoMgztmVKIC7r6Cx9le6AFoHpU8lNGjYyPTzEtjmlfVaneMyotisoBdbq5RvELIOezdmz52YqAPTvulpesyc2EpLiemperS6aXY1el0GB9p9bcUKM4Y2RCiyL3gSrIPo0oVQz54cBlBEC6h9DKrGCrL0JemWlQQkr4D5nHAST0umV9McvRPnrnXZZiJ83."
a = 47; b = 52; c = 77; d = 82
sliced_string = ""
diff1 = int(b - a)
diff2 = int(d - c)
# sliced_string = s[a:b:diff1] + " " + s[c:d:diff2]
sliced_string = s[a:b+1] + " " + s[c:d+1]
print(sliced_string)
    # return sliced_string

# if __name__ == "__main__":
#     main()