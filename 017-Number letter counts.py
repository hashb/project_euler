ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
n = 0
count = 0

def nums(num):
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num-10]
    else:
        return tens[int(num/10)] + ones[num-int(num/10)*10]
def main():
    count=0
    for num in range(1, 1001):
        if num < 100:
            n = nums(num)
        elif num < 1000:
            n = ones[int(num/100)] + "hundred"
            if num % 100 != 0:
                n = n + "and" + nums(num-int(num/100)*100)
        elif num == 1000:
            n = "onethousand"
        count += len(n)
    print(count)

if __name__ == '__main__':
    main()