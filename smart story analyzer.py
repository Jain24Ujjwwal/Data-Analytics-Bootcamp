import pandas as pd

def generate_feedback(score):
    if score >= 85:
        return "Excellent performance"
    elif score >= 70:
        return "Good, but there is room for improvement"
    elif score >= 60:
        return "Average performance, needs more focus"
    else:
        return "Low performance, requires immediate attention"

def load_data(file):
    try:
        df = pd.read_csv(file)
        print("\nData loaded from file.")
    except:
        print("\nFile not found. Using default dataset.\n")

        # Default dataset (Ujjawal included)
        data = {
            "Name": ["Ujjawal", "Aman", "Riya", "Raj", "Simran"],
            "Math": [78, 70, 85, 60, 90],
            "Physics": [72, 60, 78, 55, 88],
            "Chemistry": [70, 65, 82, 58, 85],
            "English": [80, 80, 90, 65, 92]
        }
        df = pd.DataFrame(data)

    return df

def generate_story(file):
    df = load_data(file)

    print("\nData Preview:\n")
    print(df.head())

    # Subject columns
    subjects = ["Math", "Physics", "Chemistry", "English"]

    # Total & Percentage
    df['Total'] = df[subjects].sum(axis=1)
    df['Percentage'] = df['Total'] / len(subjects)

    # Ranking
    df = df.sort_values(by='Total', ascending=False).reset_index(drop=True)
    df['Rank'] = df.index + 1

    print("\nStudent Rankings:\n")
    print(df[['Name', 'Total', 'Rank']])

    print("\nIndividual Performance Analysis:\n")

    for _, row in df.iterrows():
        print(f"{row['Name']} (Rank {row['Rank']}):")

        for subject in subjects:
            feedback = generate_feedback(row[subject])
            print(f"  {subject}: {row[subject]} - {feedback}")

        print()

    # Class Insights
    print("\nClass-Level Insights:\n")
    avg = df[subjects].mean()

    for subject in subjects:
        if avg[subject] >= 75:
            print(f"{subject} is performing well across the class.")
        elif avg[subject] >= 60:
            print(f"{subject} shows average performance.")
        else:
            print(f"{subject} needs improvement across students.")

    # Suggestions
    print("\nSuggestions:\n")

    weak_subjects = [sub for sub in subjects if avg[sub] < 60]

    if weak_subjects:
        print("Students should focus more on:", ", ".join(weak_subjects))
    else:
        print("Overall performance across subjects is balanced.")

if __name__ == "__main__":
    file = input("Enter CSV file name (or press Enter to use default): ")
    generate_story(file)