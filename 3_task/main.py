# from pydantic import BaseModel, ValidationError

# class User(BaseModel):
#     id : int
#     name : str
#     email : str
#     age : int | None = None

# user_data = {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25}
# user = User(**user_data)
# print(user)
# print(user.model_dump())


# try:
#     invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
# except ValidationError as e:
#     print(e)












# from pydantic import BaseModel, EmailStr


# class Address(BaseModel):
#     street: str
#     city: str
#     zip_code: str


# class UserAddress(BaseModel):
#     id : int
#     name : str
#     email: EmailStr
#     addresses : list[Address]

# user_data : dict = {
#                     "id": 5, 
#                     "name": "sajeel", 
#                     "email": "sa@gmail.com", 
#                     "addresses": [
#                                     {"street": "123 Main St", "city": "New York", "zip_code": "10001"},
#                                     {"street": "456 Oak Ave", "city": "Los Angeles", "zip_code": "90001"},
#                                 ],
#                     }  

# user = UserAddress.model_validate(user_data)
# print(user.model_dump())







# from pydantic import BaseModel, EmailStr, ValidationError, validator

# class Address(BaseModel):
#     street: str
#     city: str
#     zip_code: str

# class UserAdress(BaseModel):
#     id : int
#     name : str
#     email : EmailStr
#     addresses : list[Address]

#     @validator("name")
#     def name_must_be_at_least_two_chars(cls, v):
#         if len(v) < 2:
#             raise ValueError("Name must be at least 2 characters long")
#         return v
    

# try:
#     invalid_user = UserAdress(
#         id=3,
#         name="Akjk",
#         email="charlie@example.com",
#         addresses=[{"street": "789 Pine Rd", "city": "Chicago", "zip_code": "60601"}],
#     )
# except ValidationError as e:
#     print(e)





###   use fastapi


from pydantic import BaseModel, EmailStr
from fastapi import FastAPI

app = FastAPI()

# Student model
class Student(BaseModel):
   name: str
   age: int
   phone: int
   rollnumber: int
   email: EmailStr

# Admission model
class Addmission(BaseModel):
    percentage: int
    field: str
    class_time: int
    class_date: int
    student_detail: Student

# POST route
@app.post("/user")
def create_user(
    name: str,
    age: int,
    phone: int,
    rollnumber: int,
    email: EmailStr,
    percentage: int,
    field: str,
    class_time: int,
    class_date: int
):
    student = Student(
        name=name,
        age=age,
        phone=phone,
        rollnumber=rollnumber,
        email=email
    )

    addmission = Addmission(
        percentage=percentage,
        field=field, 
        class_time=class_time,
        class_date=class_date,
        student_detail=student
    )

    return {"student": addmission.model_dump()}
