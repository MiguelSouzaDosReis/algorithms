def study_schedule(permanence_period, target_time):
    count = 0
    for firstNumber, secondNumber in permanence_period:
        if (
            target_time is None
            or not isinstance(firstNumber, (int))
            or not isinstance(secondNumber, (int))
        ):
            return None
        if target_time == firstNumber or target_time == secondNumber:
            count += 1
        if target_time > firstNumber and target_time < secondNumber:
            count += 1
    return count
