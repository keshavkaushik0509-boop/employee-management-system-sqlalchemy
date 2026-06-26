import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Session

engine = sa.create_engine("sqlite:///employees.db")


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "employees"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    email = sa.Column(sa.String)
    salary = sa.Column(sa.Integer)


Base.metadata.create_all(engine)


def add_employee():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    salary = int(input("Enter Salary: "))

    with Session(engine) as session:
        employee = Employee(
            name=name,
            email=email,
            salary=salary
        )

        session.add(employee)
        session.commit()

        print("\nEmployee Added Successfully!")
        print(f"Employee ID: {employee.id}")


def view_employees():
    with Session(engine) as session:

        employees = session.scalars(
            sa.select(Employee)
        ).all()

        if not employees:
            print("\nNo Employees Found!")
            return

        row_format = "{:<5}{:<20}{:<35}{:<10}"

        print("\n" + "-" * 70)
        print(row_format.format("ID", "Name", "Email", "Salary"))
        print("-" * 70)

        for employee in employees:
            print(
                row_format.format(
                    employee.id,
                    employee.name,
                    employee.email,
                    employee.salary
                )
            )

        print("-" * 70)


while True:

    print("\n========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        print("\nThank you for using Employee Management System.")
        break

    else:
        print("\nInvalid Choice!")