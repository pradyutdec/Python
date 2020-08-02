import xlwt

# Initialize a workbook
book = xlwt.Workbook()

# Add a sheet to the workbook
sheet2 = book.add_sheet("Sheet2")

# The data
cols = ["x", "x", "x", "x", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P"]
txt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Loop over the rows and columns and fill in the values
for num in range(100):
    row = sheet2.row(num)
    for index, col in enumerate(cols):
        value = txt[index] + num
        row.write(index, value)

# Save the result
book.save("test1.xls")
