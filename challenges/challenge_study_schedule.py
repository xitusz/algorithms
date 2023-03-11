def study_schedule(permanence_period, target_time):
    count = 0

    try:
        for index in permanence_period:
            if index[0] <= target_time <= index[1]:
                count += 1
    except Exception:
        return None

    return count


p_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
print(study_schedule(p_periods, 5))
print(study_schedule(p_periods, 3))