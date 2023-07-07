
def warning(self):
    #change colour
    
        def get_change(self, current, previous):
            self.previous = current
            change = (abs(current - previous) / previous) * 100.0
            if current == previous:
                return 0
            try:
                change = (abs(current - previous) / previous) * 100.0
                if change < 95:
                    colour_change()
                return change
            except ZeroDivisionError:
                return float('inf')
    
        def colour_change(self):
            self.Warningbox.setStyleSheet("font: 100 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(95, 202, 127)")
            self.Warning_box.additem("Warning - loss change exceeds 5%")
           # self.Text_warning_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Text box for selecting warning - dispays amount of data lost, between which two points, and the timestamp</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
