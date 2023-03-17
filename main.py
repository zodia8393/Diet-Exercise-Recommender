from input_data import get_user_data
from diet_recommendation import recommend_meal_plan
from exercise_recommendation import recommend_exercise_routine

def display_recommendations(meal_plan, exercise_routine):
    print("\nRecommended Meal Plan:")
    print(f"Name: {meal_plan['name']}")
    print(f"Breakfast: {meal_plan['breakfast']}")
    print(f"Lunch: {meal_plan['lunch']}")
    print(f"Dinner: {meal_plan['dinner']}")
    print(f"Snacks: {meal_plan['snacks']}")

    print("\nRecommended Exercise Routine:")
    print(f"Cardio: {exercise_routine['cardio']}")
    print(f"Strength: {exercise_routine['strength']}")
    print(f"Flexibility: {exercise_routine['flexibility']}")

def main():
    user_data = get_user_data()
    meal_plan = recommend_meal_plan(user_data)
    exercise_routine = recommend_exercise_routine(user_data)

    display_recommendations(meal_plan, exercise_routine)

if __name__ == "__main__":
    main()
