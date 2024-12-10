import math
import json

def calculate_bmr(weight, height, age, gender):
    """기초대사량(BMR) 계산."""
    if gender.lower() == '남성':
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == '여성':
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("성별은 '남성' 또는 '여성'만 입력하세요.")

def calculate_daily_calories(bmr, activity_level):
    """활동 수준에 따른 총 필요 칼로리 계산."""
    activity_factors = {
        "가벼움": 1.2,
        "중간": 1.55,
        "고강도": 1.9
    }
    return bmr * activity_factors.get(activity_level, 1.2)

def calculate_days_needed(total_calories_to_burn, daily_calorie_deficit):
    """목표 달성까지 필요한 일 수 계산."""
    return math.ceil(total_calories_to_burn / daily_calorie_deficit)

def recommend_exercise(total_calories_to_burn, exercise_choice):
    """운동 선택에 따른 소요 시간 계산."""
    with open("data/exercise_data.json", "r", encoding="utf-8") as f:
        exercise_data = json.load(f)

    if exercise_choice not in exercise_data:
        raise ValueError("해당 운동은 데이터에 없습니다.")

    calories_per_hour = exercise_data[exercise_choice]
    hours_needed = total_calories_to_burn / calories_per_hour
    return hours_needed

def main():
    print("다이어트 계산기를 시작합니다!")

    # 사용자 입력 받기
    weight = float(input("현재 체중(kg)을 입력하세요: "))
    goal_weight = float(input("목표 체중(kg)을 입력하세요: "))
    height = float(input("키(cm)를 입력하세요: "))
    age = int(input("나이를 입력하세요: "))
    gender = input("성별을 입력하세요 (남성/여성): ")
    activity_level = input("활동 수준을 선택하세요 (가벼움/중간/고강도): ")

    # BMR 계산
    bmr = calculate_bmr(weight, height, age, gender)

    # 하루 칼로리 소비량 계산
    daily_calories = calculate_daily_calories(bmr, activity_level)

    # 목표 체중까지 필요한 총 칼로리 소모량 계산
    weight_to_lose = weight - goal_weight
    total_calories_to_burn = weight_to_lose * 7700

    # 목표 달성 예상 기간 계산
    daily_calorie_deficit = daily_calories * 0.8  # 예: 80%만 감량 목표로 설정
    days_needed = calculate_days_needed(total_calories_to_burn, daily_calorie_deficit)

    # 결과 출력
    print("\n==== 결과 ====")
    print(f"현재 하루 소모 칼로리: {daily_calories:.2f} kcal")
    print(f"목표 체중까지 소모해야 할 칼로리: {total_calories_to_burn:.2f} kcal")
    print(f"예상 목표 달성 기간: 약 {days_needed}일")

    # 운동 추천
    exercise_choice = input("\n선호하는 운동을 입력하세요 (예: 조깅, 줄넘기, 수영): ")
    try:
        hours_needed = recommend_exercise(total_calories_to_burn, exercise_choice)
        print(f"{exercise_choice}를 약 {hours_needed:.2f}시간 동안 하면 목표를 달성할 수 있습니다.")
    except ValueError as e:
        print(f"운동 추천 중 오류 발생: {e}")

if __name__ == "__main__":
    main()
