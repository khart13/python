def get_info():  # 학생 정보 입력 함수
    id = input("학번을 입력해주세요:")
    name = input("이름을 입력해주세요:")
    eng = int(input("영어 점수를 입력해주세요:"))
    c = int(input("C언어 점수를 입력해주세요:"))
    py = int(input("파이썬 점수를 입력해주세요:"))
    return [id, name, eng, c, py]


def cal_score(student):  # 총점/평균 계산 함수
    total = student[2] + student[3] + student[4]
    avg = round(total / 3, 2)
    return total, avg


def cal_grade(avg):  # 학점 계산 함수
    if avg >= 95:
        return 'A+'
    elif avg >= 90:
        return 'A'
    elif avg >= 85:
        return 'B+'
    elif avg >= 80:
        return 'B'
    elif avg >= 75:
        return 'C+'
    elif avg >= 70:
        return 'C'
    elif avg >= 65:
        return 'D+'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


def cal_rank(students):  # 등수 계산 함수
    for student in students:
        student[8] = 1  # 등수 초기화
    for i in range(len(students)):
        for j in range(len(students)):
            if students[i][5] < students[j][5]:
                students[i][8] += 1


def insert_student(students):  # 학생 추가 함수
    student = get_info()
    total, avg = cal_score(student)
    grade = cal_grade(avg)
    student.extend([total, avg, grade])
    students.append(student)
    cal_rank(students)
    print("학생 추가 완료!")


def delete_student(students, student_id):  # 학생 삭제 함수
    for student in students:
        if student[0] == student_id:
            students.remove(student)
            cal_rank(students)
            print("학생 삭제 완료!")
            return
    print("해당 학번의 학생을 찾을 수 없습니다.")


def search_student_by_id(students, student_id):  # 학번으로 학생 찾기
    for student in students:
        if student[0] == student_id:
            return student
    return None


def search_student_by_name(students, name):  # 이름으로 학생 찾기
    results = [student for student in students if student[1] == name]
    return results


def sort_students(students):  # 총점 기준 정렬
    students.sort(key=lambda x: x[5], reverse=True)
    print("총점 기준 정렬 완료!")


def count_80(students):  # 80점 이상 학생 수 카운트
    return sum(1 for student in students if student[6] >= 80)


def print_info(students):  # 정보 출력 함수
    print("성적관리 프로그램")
    print("===============================================================" )
    print("학번        이름    영어  C언어  파이썬  총점  평균  학점  등수")
    print("===============================================================" )
    for student in students:
        print(f"{student[0]}  {student[1]}   {student[2]}    {student[3]}      {student[4]}    {student[5]}   {student[6]}   {student[7]}     {student[8]}")


def main():  # 메인 함수
    students = []
    student_count = 5
    for _ in range(student_count):    
        student = get_info()
        total, avg = cal_score(student)
        grade = cal_grade(avg)
        student.extend([total, avg, grade, 1])  # 등수 추가
        students.append(student)
    cal_rank(students)
    print_info(students)
    
    while True:
        print("\n메뉴: 1.학생 추가 2.학생 삭제 3.학번 검색 4.이름 검색 5.총점 정렬 6.80점 이상 학생 수 7.종료")
        choice = input("선택: ")
        
        if choice == '1':
            insert_student(students)
        elif choice == '2':
            student_id = input("삭제할 학생의 학번을 입력하세요: ")
            delete_student(students, student_id)
        elif choice == '3':
            student_id = input("찾을 학생의 학번을 입력하세요: ")
            student = search_student_by_id(students, student_id)
            if student:
                print(student)
            else:
                print("해당 학번의 학생이 없습니다.")
        elif choice == '4':
            name = input("찾을 학생의 이름을 입력하세요: ")
            results = search_student_by_name(students, name)
            if results:
                for student in results:
                    print(student)
            else:
                print("해당 이름의 학생이 없습니다.")
        elif choice == '5':
            sort_students(students)
            print_info(students)
        elif choice == '6':
            print(f"80점 이상 학생 수: {count_80(students)}명")
        elif choice == '7':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 입력해주세요.")


main()
