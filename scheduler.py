def generate_schedule(subjects):
    schedule = []
    for subject in subjects:
        schedule.append(f"Estude {subject['name']} por {subject['time']} minutos.")
    return schedule