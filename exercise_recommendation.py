def recommend_exercise_routine(user_data):
    exercise_purpose = user_data['exercise_purpose'].lower()
    exercise_routines = {
        'weight_loss': {
            'cardio': '30 minutes of jogging or brisk walking',
            'strength': 'Full-body resistance training 3 times a week',
            'flexibility': 'Daily stretching routine',
        },
        'muscle_building': {
            'cardio': '20 minutes of high-intensity interval training (HIIT) 3 times a week',
            'strength': 'Split routine focusing on major muscle groups 4-5 times a week',
            'flexibility': 'Dynamic stretching before workouts and static stretching after workouts',
        },
        'maintenance': {
            'cardio': '30 minutes of moderate-intensity cardio 3-4 times a week',
            'strength': 'Total-body strength training 2-3 times a week',
            'flexibility': 'Regular stretching and mobility exercises',
        },
    }

    if exercise_purpose in ['weight loss', 'lose weight']:
        recommended_routine = exercise_routines['weight_loss']
    elif exercise_purpose in ['muscle building', 'build muscle', 'gain muscle']:
        recommended_routine = exercise_routines['muscle_building']
    else:
        recommended_routine = exercise_routines['maintenance']

    return recommended_routine
