def get_user_data():
    user_data = {}

    user_data['height'] = float(input("Enter your height (cm): "))
    user_data['weight'] = float(input("Enter your weight (kg): "))
    
    # Body Composition Analysis
    user_data['body_fat_percentage'] = float(input("Enter your body fat percentage: "))
    user_data['lean_body_mass'] = float(input("Enter your lean body mass (kg): "))
    
    # Skeletal Muscle Fat Analysis
    user_data['skeletal_muscle_mass'] = float(input("Enter your skeletal muscle mass (kg): "))
    user_data['body_fat_mass'] = float(input("Enter your body fat mass (kg): "))
    
    # Obesity Analysis
    user_data['bmi'] = float(input("Enter your BMI: "))
    user_data['percent_body_fat'] = float(input("Enter your percent body fat: "))
    
    # Muscle Analysis by Region
    user_data['arm_muscle_mass'] = float(input("Enter your arm muscle mass (kg): "))
    user_data['leg_muscle_mass'] = float(input("Enter your leg muscle mass (kg): "))
    user_data['trunk_muscle_mass'] = float(input("Enter your trunk muscle mass (kg): "))
    
    # Extracellular Water Secretion Analysis
    user_data['extracellular_water'] = float(input("Enter your extracellular water (L): "))
    
    # Weight Control
    user_data['weight_control_target'] = float(input("Enter your weight control target (kg): "))
    
    # Obesity Evaluation
    user_data['obesity_degree'] = float(input("Enter your obesity degree: "))
    
    # Body Balance Evaluation
    user_data['body_balance'] = float(input("Enter your body balance evaluation: "))
    
    user_data['exercise_purpose'] = input("Enter the purpose of your exercise: ")

    return user_data
