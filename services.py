from bson import ObjectId
from datbase import get_collection
from schemas import Student

collection=get_collection()


def help(student:Student)->dict:
    return{
        'id':str(student['_id']),
        'name':str(student['name']),
        'age':int(student['age']),
        'course':str(student['course'])
    }

def createstudent(student:Student):
    newdict=student.model_dump()
    result=collection.insert_one(newdict)
    created_student = collection.find_one({
        "_id": result.inserted_id
    })

    return help(created_student)


def getstudents():
    students = collection.find()

    return [help(studentx) for studentx in students]

def updatestudent(student_id: str, student: Student):
    result = collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student.model_dump()}
    )

    updated_student = collection.find_one({
        "_id": ObjectId(student_id)
    })

    return help(updated_student)
def deletestudent(student_id: str):
    result = collection.delete_one({
        "_id": ObjectId(student_id)
    })

    return {"message": "Student deleted successfully"}
