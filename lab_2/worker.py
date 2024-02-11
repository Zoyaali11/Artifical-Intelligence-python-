def efficiency(time):
    if 2 <= time <= 3:
        return "Worker is highly efficient."
    elif 3 < time <= 4:
        return "Worker needs to improve speed."
    elif 4 < time <= 5:
        return "Worker requires training to improve speed."
    elif time > 5:
        return "Worker needs to leave the company."

time = float(input("Enter the time taken by worker: "))
result = efficiency(time)
print("Worker's Efficiency:", result)
