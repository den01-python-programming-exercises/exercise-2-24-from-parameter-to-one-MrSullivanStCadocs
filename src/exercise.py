def main():
    #write your code below this line

    print_from_number_to_one(5)

def print_from_number_to_one(number):
  i = 5
  while (i <= number):
      print(i)
      i -= 1
      if (i == -1):
        break

if __name__ == '__main__':
    main()
