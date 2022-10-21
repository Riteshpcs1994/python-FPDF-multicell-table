from fpdf import FPDF

data = (
    ("First Name", "Last name", "Age", "Text"),
    ("JulSSes", "Smith", "34", "This contains a long text. not too long but longer than cell's width"),
    (
        "Mary",
        "Ramos",
        "45",
        "This should not exceed the cell's width.",
    ),
    ("Ritesh ", "Kumar", "19", "This is a quite long text for a cell. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."),
    ("Lucas", "Cimon", "31", "This also contains a long text, not too long but longer than cell's width"),
)

#python 
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=10)
line_height = pdf.font_size * 2.5
col_width = 45
errMargin = 13  # distribute content evenly
lh_list = []
for row in data:
    max_len = len(max(row, key=len))
    if max_len < (col_width - errMargin):
        split_len = 1
        lh_list.append(1)
    else:
        textLength = len(max(row, key=len))
        max_ch = max(row, key=len)
        startChar = 0
        maxChar = 0
        textArray = []
        tmpString = ""

        while startChar < (textLength):
            while maxChar < (col_width - errMargin):
                tmpString = max_ch[startChar:maxChar]
                maxChar += 1

            startChar = startChar + maxChar
            textArray.append(tmpString)
            maxChar = 0
            tmpString = ""

        lh_list.append(len(textArray))


for j, row in enumerate(data):
    for datum in row:
        if len(datum) < (col_width - errMargin):
            pdf.cell(
                col_width,
                line_height * lh_list[j],
                datum,
                border=1,
                ln=0,
            )
        else:
            #Save the current position
            xPos = pdf.get_x()
            yPos = pdf.get_y()
            pdf.multi_cell(
                col_width,
                line_height,
                datum,
                border=1,
            )
            #Put the position to the right of the cell
            pdf.set_xy(xPos + col_width, yPos)

    #Go to the next line
    pdf.ln(line_height * lh_list[j])

pdf.output('fpdf_wrap_text.pdf','F')
