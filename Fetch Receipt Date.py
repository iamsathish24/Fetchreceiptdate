import pytesseract
from PIL import Image
from itertools import product


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img = Image.open(r'C:\Users\Sathish Kumar\Desktop\Imageextraction\2b577c41.jpeg')   #Copy paste the location of the image.
text = pytesseract.image_to_string(img)                                             #Image to text converter.
wordsraw = text.split()                                                             # Splitting the raw data into individual strings using space as separator.
words = [wordsraw[element].lower() for element in range(len(wordsraw))]             # Converting the texts to lowercase.


# Data to compare.
months = ('jan','feb','mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep','oct','nov', 'dec')
years = ['2019', '2018', '2017']
years2 = ['19', '18', '17']
symbols = ['-','/','.','\ ', "'"]

def check_month():                            # The first obvious to check in the raw data is the presence of month in it, so we're checking the month first.
    for month,word in product(months, words): # Initiate the cycle to check for all the months in the data.
        if month in word:                     # If month present in any string, then it is being sent to 'check_symbol' function to double confirm with the presence of a symbol used as separators like -,., /, \, '.
            check_symbol(month)
            if check_symbol(month) == None:   # If the string doesn't have any separator, then no data is being returned to the fuction.
                return
            else:
                return month                  # If the string has any separator, then the string is being returned to the function.

def check_year():                             # The second thing  to check if month is not present in the data is the presence of year in the raw data, so we'll check the year now.
    for year, word2 in product(years, words): # Let's initiate the cycle to check for all the years in the data.
        if year in word2:                     # If year present in any string, then it is being sent to 'check_symbol' function to double confirm with the presence of a symbol used as separators like -,., /, \, '.
            check_symbol(word2)
            if check_symbol(word2) == None:   # If the string doesn't have any separator, then no data is being returned to the fuction.
                return
            else:
                return word2                  # If the string has any separator, then the string (date) is being returned to the function.

def check_year2():                            # There are some scenarios where month and year will not be present, the year will be in mentioned short form like 17, 18, 19.
    for year2, word3 in product(years2,words):# Initiate the cycle to check for all the months in the data.
        if year2 in word3:                    # If short form of year is present in any string, then it is being sent to 'check_symbol' function to double confirm with the presence of a symbol used as separators like -,., /, \, '.
            check_symbol(word3)
            if check_symbol(word3) == None:   # If the string doesn't have any separator, then no data is being returned to the fuction.
                return
            else:
                return word3                  # If the string has any separator, then the string (date) is being returned to the function.

def check_symbol(x):                          # This check_symbol accepts the string, and checks for the presence of any separators to double confirm.
    for symbol in symbols:                    # Initiate the cycle to check for all the symbols in the string.
        if symbol in x:                       # If the symbol is present, then the string (date) is being returned to function.
            return symbol


if check_month() == None:                     # The first obvious to check in the raw data is the presence of month in it, so we're checking the month first.
    check_year()                              # If month is not present in the data, then check_year function is being called.
    if check_year() == None:                  # If check_year function returns nothing, then check_year2 function is being called.
        check_year2()
        if check_year2() == None:             # If check_year2 function returns nothing then it means that there is no date is present in the receipt so 'Date: null' will be printed.
            print('Date: null')
        else:
            print('date:',check_year2())      # If check_year2 function returns a string (date), then that date is being printed.
    else:
        print('date:',check_year())           # If check_year function returns a string (date) which contains a year, then that date is being printed.
else:
    print('date:',check_month())              # If check_month function returns a string (date) which contains month, then check_month is being printed.
