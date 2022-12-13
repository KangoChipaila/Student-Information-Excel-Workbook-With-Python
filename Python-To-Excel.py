import xlsxwriter

file_name = str(input("Name your file: ")) + '.xlsx'
workbook = xlsxwriter.Workbook(file_name)

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'First Name')
worksheet.write('B1', 'Last Name')
worksheet.write('C1', 'Other Name')
worksheet.write('D1', 'Student ID')

row = 1
column = 0

no_of_students = int(input("\nHow many students are you entering into this worksheet: "))

for i in range(no_of_students):

    first_name = str(input("First name: "))
    last_name = str(input("Last name: "))
    other_name = str(input("Other name: "))
    student_ID = int(input("Student ID: "))
    
    worksheet.write(row, column, first_name)
    
    column += 1

    worksheet.write(row, column, last_name)
    
    column += 1
    
    worksheet.write(row, column, other_name)

    column += 1

    worksheet.write(row, column, student_ID)

    column += 1

    row += 1
    column -= 4

    print('\n')

workbook.close()