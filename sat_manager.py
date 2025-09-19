import json
import os

DATA_FILE = 'sat_data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print("Data saved.")



def find_by_name(data, name):
    for record in data:
        if record['name'].lower() == name.lower():
            return record
    return None



def insert_data(data):
    
    while True:
        name = input("Enter Name (unique, letters only): ")
        if not name.isalpha():
            print("Invalid name. Only letters are allowed.")
            continue
        if find_by_name(data, name):
            print("Record already exists!")
            return
        break

    address = input("Enter Address: ")

    
    while True:
        city = input("Enter City: ")
        if city.isalpha():
            break
        else:
            print("Invalid city. Only letters are allowed.")

    
    while True:
        country = input("Enter Country: ")
        if country.isalpha():
            break
        else:
            print("Invalid country. Only letters are allowed.")
            
    while True:
        pincode = input("Enter Pincode (numbers only): ")
        if pincode.isdigit():
            break
        else:
            print("Invalid pincode. Only numbers are allowed.")

    
    while True:
        try:
            score = float(input("Enter SAT Score (0 - 100): "))
            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    
    passed = "Pass" if score > 30 else "Fail"

    # Create and add record
    record = {
        "name": name,
        "address": address,
        "city": city,
        "country": country,
        "pincode": pincode,
        "satScore": score,
        "passed": passed
    }
    data.append(record)
    print(" Record inserted.")



# View all records
def view_all(data):
    if not data:
        print("No records to show.")
    else:
        print(json.dumps(data, indent=4))


# Show rank of a student based on score
def get_rank(data):
    name = input("Enter Name: ")
    target = find_by_name(data, name)
    if not target:
        print("No such record found.")
        return

    scores = sorted([r['satScore'] for r in data], reverse=True)
    rank = scores.index(target['satScore']) + 1
    print(f"{name} scored {target['satScore']} and rank is {rank}")



def update_score(data):
    name = input("Enter Name: ")
    target = find_by_name(data, name)
    if not target:
        print("No record found.")
        return

    try:
        new_score = float(input("Enter new SAT Score: "))
    except ValueError:
        print("Invalid score.")
        return

    target['satScore'] = new_score
    target['passed'] = "Pass" if new_score > 30 else "Fail"
    print("Score updated.")



def delete_record(data):
    name = input("Enter Name: ")
    target = find_by_name(data, name)
    if not target:
        print("No record found.")
        return

    data.remove(target)
    print("Record deleted.")



def average_score(data):
    if not data:
        print("No records.")
        return

    avg = sum(r['satScore'] for r in data) / len(data)
    print(f"Average Score = {avg:.2f}")


# Filter records by pass/fail
def filter_records(data):
    choice = input("Enter choice (1=Pass, 2=Fail): ")
    if choice not in ['1', '2']:
        print("Invalid choice.")
        return

    status = "Pass" if choice == "1" else "Fail"
    filtered = [r for r in data if r['passed'] == status]
    if filtered:
        print(json.dumps(filtered, indent=4))
    else:
        print(f"No records with status: {status}")


def main():
    data = load_data()
    while True:
        print("\nSAT Results Manager")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Calculate Average SAT Score")
        print("7. Filter records by Pass/Fail")
        print("8. Save data to file")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            insert_data(data)
        elif choice == '2':
            view_all(data)
        elif choice == '3':
            get_rank(data)
        elif choice == '4':
            update_score(data)
        elif choice == '5':
            delete_record(data)
        elif choice == '6':
            average_score(data)
        elif choice == '7':
            filter_records(data)
        elif choice == '8':
            save_data(data)
        elif choice == '9':
            save_data(data)
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()