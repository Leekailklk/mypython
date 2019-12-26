def savingResultMsg(self, resultmsg):
    if not os.path.exists('./log'):
        os.makedirs('./log')
    self.savingtxtmsg = open('./log/result.txt', 'a')
    self.savingtxtmsg.write(resultmsg)
    self.savingtxtmsg.write('\n')
    self.savingtxtmsg.close()
    self.TxtToPdf('./log/result.txt','./log/result.pdf')
def TxtToPdf(self,strSourceTxt,strTargetPdf):

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
TxtToPdf(self,'./txt2pdf.py','./txt2pdf.pdf')