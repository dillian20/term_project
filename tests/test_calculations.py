import unittest
from diet_calculator import calculate_bmr, calculate_daily_calories, calculate_days_needed

class TestDietCalculator(unittest.TestCase):

    def test_calculate_bmr(self):
        """BMR 계산 테스트"""
        self.assertAlmostEqual(calculate_bmr(70, 175, 30, '남성'), 1665.0, places=1)
        self.assertAlmostEqual(calculate_bmr(60, 160, 25, '여성'), 1373.5, places=1)
        with self.assertRaises(ValueError):
            calculate_bmr(70, 175, 30, '기타')  # 성별이 올바르지 않을 경우

    def test_calculate_daily_calories(self):
        """활동 수준에 따른 총 필요 칼로리 계산 테스트"""
        bmr = 1665.0  # 테스트를 위한 BMR 값
        self.assertAlmostEqual(calculate_daily_calories(bmr, "가벼움"), 1998.0, places=1)
        self.assertAlmostEqual(calculate_daily_calories(bmr, "중간"), 2570.75, places=1)
        self.assertAlmostEqual(calculate_daily_calories(bmr, "고강도"), 3163.5, places=1)

    def test_calculate_days_needed(self):
        """목표 달성까지 필요한 일 수 계산 테스트"""
        total_calories_to_burn = 7700  # 1kg 감량에 필요한 칼로리
        daily_calorie_deficit = 500    # 하루 칼로리 부족분
        self.assertEqual(calculate_days_needed(total_calories_to_burn, daily_calorie_deficit), 16)

        total_calories_to_burn = 15400  # 2kg 감량
        self.assertEqual(calculate_days_needed(total_calories_to_burn, daily_calorie_deficit), 31)

if __name__ == "__main__":
    unittest.main()
