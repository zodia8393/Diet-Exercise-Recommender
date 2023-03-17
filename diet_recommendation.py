import random

def recommend_meal_plan(user_data):
    # You can define various meal plans or diets based on user_data.
    # For simplicity, here are some example meal plans:
    meal_plans = [
        {
            'name': 'Weight Loss',
            'breakfast': 'Oatmeal with fruits and nuts',
            'lunch': 'Grilled chicken salad with vinaigrette',
            'dinner': 'Baked salmon with quinoa and steamed vegetables',
            'snacks': 'Greek yogurt with honey and almonds'
        },
        {
            'name': 'Muscle Building',
            'breakfast': 'Egg and avocado toast',
            'lunch': 'Turkey and cheese sandwich with mixed greens',
            'dinner': 'Grilled steak with sweet potatoes and green beans',
            'snacks': 'Protein shake with banana and peanut butter'
        },
        {
            'name': 'Maintenance',
            'breakfast': 'Smoothie with spinach, berries, and protein powder',
            'lunch': 'Whole grain pasta with marinara sauce and vegetables',
            'dinner': 'Stir-fried tofu with rice and mixed vegetables',
            'snacks': 'Hummus with carrot sticks'
        },
    ]

    # This is a simple example of selecting a meal plan based on user_data.
    # You can implement more complex logic based on the user's information.
    if user_data['obesity_degree'] > 1:
        recommended_meal_plan = meal_plans[0]
    elif user_data['skeletal_muscle_mass'] < user_data['weight'] * 0.3:
        recommended_meal_plan = meal_plans[1]
    else:
        recommended_meal_plan = meal_plans[2]

    return recommended_meal_plan

