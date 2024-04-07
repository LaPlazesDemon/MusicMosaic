import math

def msToTimestamp(milliseconds):
    totalSeconds = milliseconds/1000
    totalMinutes = totalSeconds/60
    totalHours = totalMinutes/60

    if totalHours == 0:
        durationSeconds = math.floor(totalSeconds%60)
        durationMinutes = math.floor(totalMinutes)
        
        # Ensure there are 2 digits of the timestamp for seconds
        if durationSeconds >= 10: cleanSeconds = f"{durationSeconds}"
        else: cleanSeconds = f"0{durationSeconds}"

        return f"{durationMinutes}:${cleanSeconds}"

    else:
        durationSeconds = math.floor(totalSeconds%60)
        durationMinutes = math.floor(totalMinutes%60)
        durationHours = math.floor(totalMinutes/60)

        # Ensure there are 2 digits of the timestamp for seconds
        if durationSeconds >= 10: cleanSeconds = f"{durationSeconds}"
        else: cleanSeconds = f"0{durationSeconds}"

        # Ensure there are 2 digits of the timestamp for minutes
        if durationMinutes >= 10: cleanMinutes = f"{durationMinutes}"
        else: cleanMinutes = f"0{durationMinutes}"

        return f"{durationHours}:{cleanMinutes}:{cleanSeconds}"
