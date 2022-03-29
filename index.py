"""
Robbie Platt
Library of Congress (Project 4)
Due date: 3/26/2022


This program will read the file that is in the sys.argv and will write it 
to another file. To use this you will want to use your IDE to run the file,
have a file in the sys.argv that has a bar separated 3 letter code at the 
end of each line.


"""

import sys
import csv
import operator


def lines_length(lines):
    return len(lines)
        

def longest_line():
    """
    Identifies the longest line.
    """###
    with open(sys.argv[1], "r") as in_file:
        with open("novel_summary.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            longest = 0
            code = ""
            for row in reader:
                if int(row[1]) > longest:
                    longest = int(row[1])
                    code = row[2]
            print(longest)
            return code
            return longest  
                  

def shortest_line():
    """
    Identifies the shortest line.
    """




def get_code(data):
    """
    gets 3 letter codes
    """
    pass
    pass
    pass
    with open(sys.argv[1], "r") as in_file:
        with open("novel_text.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            lines = list(reader)
            return lines[2]


def write_book_data():
    """
    Format's data
    """
    for code, length, text in data:
        return ("{} {} {}".format(code, length, text))



def sorted_lines():
    with open(sys.argv[1], "r") as in_file:
        with open("book_data.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            lines = list(reader)
            


            def sort_key(line):
                return line[2]
            def sort_two(line):
                sort_num = int(str(line[1]))
                return sort_num           
            
            
            #lines.sort(key = operator.itemgetter(2, 1))
            
            lines.sort(key = sort_two)
            lines.sort(key = sort_key)

            for line in lines:
                #print(lines)
                out_file.write(f"{lines}")
                return lines
            
            

    


                               
def sort_books_data(data, index):
    """
    Sorts the books
    """
    with open(sys.argv[1], "r") as in_file:
        with open("novel_text.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            lines = list(reader)
    header = lines[0]
    sorted_books = lines[1:]
    if index == 3:
        sorted_books.sort(key = get_code)
    else:
        sorted_books.sort(key = get_code)
    print(sorted_books)
    return sorted_books
    
def total():
    """
    Adds line counts together. (For use in getting average)
    """
    with open(sys.argv[1], "r") as in_file:
        with open("novel_text.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            lines = list(reader)
            for row in lines:
                num = row[1]
            print(num)
            return num

def count():
    """
    Counts the total lines.
    """

def avg(num_one, num_two):
    """
    Fix This!! Gets the average line length.
    """
    return(num_one + num_two) / 2

def fetch_book_data(file):
    """

    """ ####
    with open(sys.argv[1], "r") as in_file:
        with open("novel_text.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")

            book_info = []
            for row in reader:
                book_info.append(row[0])
            print(book_info[0])
            print(book_info[1])
            return book_info


def code():
    """
    isolates the book code.
    """
    with open(sys.argv[1], "r") as in_file:
        with open("novel_text.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            lines = []
            for row in reader:
                lines.append(row[0])
        #code_group = [code.append(code) for i in range(20)]
        print(code)
        return code

def code_two():
    """
    Gets the second book code
    """
    with open(sys.argv[1], "r") as in_file:
        with open("novel_text.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            lines = list(reader)
            code = lines[1][2]
        return code      

def code_loop(item, term):
    """
    Appends lines to book codes
    """
    with open(sys.argv[1], "r") as in_file:
        with open("novel_text.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            lines = []
            for row in reader:
                if str(item).lower() == str(term).lower():
                    lines.append(row[0])
                else:
                    pass
            print(lines)
            print(row[0])
            return lines

def fetch_book_data(file):
    """

    """ ####
    with open(sys.argv[1], "r") as in_file:
        with open("novel_text.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")

            book_info = []
            for row in reader:
                book_info.append(row[0])
            print(book_info[0])
            print(book_info[1])
            return book_info

def lines_length():
    with open(sys.argv[1], "r") as in_file:
        with open("novel_text.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            lines = list(reader)
            for row in reader:
                print(lines)

    
    return len(lines)
        

def longest_line():
    """
    Identifies the longest line.
    """###
    with open(sys.argv[1], "r") as in_file:
        with open("novel_summary.txt", "w") as out_file:
            reader = csv.reader(in_file, delimiter = "|")
            longest = 0
            code = ""
            for row in reader:
                if int(row[1]) > longest:
                    longest = int(row[1])
                    code = row[2]
            print(longest)
            return code
            return longest  
                  

def shortest_line():
    """
    Identifies the shortest line.
    """
  

def main():
    """
    Main function, used to call the functions of the program.
    """
    code()
    #code_two()
    #code_loop(code(), code())
    #fetch_book_data(sys.argv[1])
    #longest_line()
    #write_book_data()
    #total()
    #sort_books_data(sys.argv, code())
    #lines_length()
    #sorted_lines()
    #sorted_lines_two([sorted_lines()])

if __name__ == "__main__":
    main()
