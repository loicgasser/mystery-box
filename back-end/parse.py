import json

def aggregate_by_week():
    with open("data.json", "r") as f:
        data = json.loads(f.read())

    week_number_to_value = {}
    week_number = 0
    for i, item in enumerate(data):
        if i % 7 == 0:
            week_number += 1
        week_number_to_value[week_number] += item

    print(week_number_to_value)


if __name__ == "__main__":
    aggregate_by_week()
