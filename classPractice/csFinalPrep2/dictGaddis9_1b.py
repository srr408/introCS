def courseInfo(courseNum:str)->tuple:

    courses={"CS101":("3004", "Haynes", "8:00 am"),
            "CS102":("4501","Alvarado","9:00 am"),
            "CS103":("6755","Rich","10:00 am"),
            "NT110":("1244","Burke","11:00 am"),
            "CM2411":("1411","Lee","1:00 pm")
    }
    error="The course " + courseNum + " does not exist"
    return courses.get(courseNum,error)


courseList=["CS101","CS102","CS103","NT110","CM2411"]

for course in courseList:
        (room,instructor,time)=courseInfo(course)#tuple unpacking
        print(course+",", room+",", instructor+",",time+",")