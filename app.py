from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Data awal mahasiswa (10 data) dengan detail lebih lengkap
students = {
    "1": {
        "name": "Ahmad Rizki",
        "major": "Teknik Informatika",
        "semester": 6,
        "gpa": 3.75,
        "email": "ahmad.rizki@univ.ac.id",
        "enrollment_date": "2020-08-15"
    },
    "2": {
        "name": "Budi Santoso",
        "major": "Sistem Informasi",
        "semester": 4,
        "gpa": 3.50,
        "email": "budi.santoso@univ.ac.id",
        "enrollment_date": "2021-08-17"
    },
    "3": {
        "name": "Citra Dewi",
        "major": "Manajemen",
        "semester": 8,
        "gpa": 3.90,
        "email": "citra.dewi@univ.ac.id",
        "enrollment_date": "2019-08-13"
    },
    "4": {
        "name": "Dodi Pratama",
        "major": "Akuntansi",
        "semester": 2,
        "gpa": 3.60,
        "email": "dodi.pratama@univ.ac.id",
        "enrollment_date": "2022-08-10"
    },
    "5": {
        "name": "Eka Saputra",
        "major": "Teknik Sipil",
        "semester": 5,
        "gpa": 3.40,
        "email": "eka.saputra@univ.ac.id",
        "enrollment_date": "2020-08-20"
    },
    "6": {
        "name": "Fani Mulyani",
        "major": "Psikologi",
        "semester": 3,
        "gpa": 3.55,
        "email": "fani.mulyani@univ.ac.id",
        "enrollment_date": "2021-08-16"
    },
    "7": {
        "name": "Gita Puspita",
        "major": "Teknik Elektro",
        "semester": 6,
        "gpa": 3.70,
        "email": "gita.puspita@univ.ac.id",
        "enrollment_date": "2020-08-11"
    },
    "8": {
        "name": "Hendra Wijaya",
        "major": "Desain Produk",
        "semester": 4,
        "gpa": 3.65,
        "email": "hendra.wijaya@univ.ac.id",
        "enrollment_date": "2021-08-12"
    },
    "9": {
        "name": "Indah Permata",
        "major": "Farmasi",
        "semester": 7,
        "gpa": 3.80,
        "email": "indah.permata@univ.ac.id",
        "enrollment_date": "2019-08-15"
    },
    "10": {
        "name": "Joko Subandi",
        "major": "Ilmu Komunikasi",
        "semester": 1,
        "gpa": 3.45,
        "email": "joko.subandi@univ.ac.id",
        "enrollment_date": "2023-08-18"
    }
}

# Classes for CRUD functionality as in the previous example
class StudentList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(students),
            "students": students
        }

class StudentDetail(Resource):
    def get(self, student_id):
        if student_id in students:
            return {
                "error": False,
                "message": "Success",
                "student": students[student_id]
            }
        return {"error": True, "message": "Student not found"}, 404

class AddStudent(Resource):
    def post(self):
        data = request.get_json()
        student_id = str(len(students) + 1)
        new_student = {
            "name": data.get("name"),
            "major": data.get("major"),
            "semester": data.get("semester"),
            "gpa": data.get("gpa"),
            "email": data.get("email"),
            "enrollment_date": data.get("enrollment_date")
        }
        students[student_id] = new_student
        return {
            "error": False,
            "message": "Student added successfully",
            "student": new_student
        }, 201

class UpdateStudent(Resource):
    def put(self, student_id):
        if student_id in students:
            data = request.get_json()
            student = students[student_id]
            student["name"] = data.get("name", student["name"])
            student["major"] = data.get("major", student["major"])
            student["semester"] = data.get("semester", student["semester"])
            student["gpa"] = data.get("gpa", student["gpa"])
            student["email"] = data.get("email", student["email"])
            student["enrollment_date"] = data.get("enrollment_date", student["enrollment_date"])
            return {
                "error": False,
                "message": "Student updated successfully",
                "student": student
            }
        return {"error": True, "message": "Student not found"}, 404

class DeleteStudent(Resource):
    def delete(self, student_id):
        if student_id in students:
            deleted_student = students.pop(student_id)
            return {
                "error": False,
                "message": "Student deleted successfully",
                "student": deleted_student
            }
        return {"error": True, "message": "Student not found"}, 404

api.add_resource(StudentList, '/students')
api.add_resource(StudentDetail, '/students/<string:student_id>')
api.add_resource(AddStudent, '/students/add')
api.add_resource(UpdateStudent, '/students/update/<string:student_id>')
api.add_resource(DeleteStudent, '/students/delete/<string:student_id>')

if __name__ == '__main__':
    app.run(debug=True)
