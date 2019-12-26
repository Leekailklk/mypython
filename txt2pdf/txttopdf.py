strSourceTxt='./txt2pdf.py'
strTargetPdf='./txt2pdf.pdf'
ptr = open(strSourceTxt, "r")  # text file I need to convert
lineas = ptr.readlines()
ptr.close()

numeroLinea = 0
p = Canvas(strTargetPdf)
p.setFont('msyh', 12)
while numeroLinea < len(lineas):
    if numeroLinea - len(lineas) < 70:  # I'm gonna write every 60 lines because I need it like that
        i = 750
        for linea in lineas[numeroLinea:numeroLinea + 60]:
            p.drawString(15, i, linea.strip())
            numeroLinea += 1
            i -= 12
        p.showPage()
    else:
        i = 750
        for linea in lineas[numeroLinea:]:
            p.drawString(15, i, linea.strip())
            numeroLinea += 1
            i -= 12
        p.showPage()
p.save()