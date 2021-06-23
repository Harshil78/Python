class emp:
    def getdata(this):
        this.empno = int(input("Enter EmpNo=>"))
        this.empname = input("Enter EmpName=>")

    def __init__(self):
        self.no = 2
        self.name = "Velcy"

    def disp(this):
        print("Emp NO=>", this.empno)
        print("Emp Name=>", this.empname)
        print("Emp NO=>", this.no)
        print("Emp Name=>", this.name)


e = emp()
e.getdata()
e.disp()
