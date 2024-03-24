def courseInfo(courseNum:str)->list[str]:
    courseTable=[["CS101", "3004","Haynes", "8:00 am"], ["CS102","4501","Alvarado", "9:00 pm"],["CS103","6755","Rich","10:00 am"]]
    # the rest of entries on the 2D list are skipped for now in the interest of class time.
    error="The course "+courseNum+" does not exist."
    for row in courseTable:
        if row[0]==courseNum:
            return row[1:4]
    return error

print(courseInfo("something random"))
print(courseInfo("CS101"))

#"beep"
#None
#"what this function do? boop"