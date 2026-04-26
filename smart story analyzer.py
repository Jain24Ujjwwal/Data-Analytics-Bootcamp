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

def generate_story(file):
    df = pd.read_csv(file)

    print("\nData Preview:\n")
    print(df.head())

    # Total & Percentage
    df['Total'] = df.select_dtypes(include='number').sum(axis=1)
    df['Percentage'] = df['Total'] / (len(df.columns) - 2)

    # Ranking
    df = df.sort_values(by='Total', ascending=False).reset_index(drop=True)
    df['Rank'] = df.index + 1

    print("\nStudent Rankings:\n")
    print(df[['Name', 'Total', 'Rank']])

    print("\nIndividual Performance Analysis:\n")

    for _, row in df.iterrows():
        print(f"{row['Name']} (Rank {row['Rank']}):")

        for subject in df.columns:
            if subject not in ['Name', 'Total', 'Percentage', 'Rank']:
                feedback = generate_feedback(row[subject])
                print(f"  {subject}: {row[subject]} - {feedback}")

        print()

    # Class Insights
    print("\nClass-Level Insights:\n")
    avg = df.mean(numeric_only=True)

    for subject in avg.index:
        if subject not in ['Total', 'Percentage', 'Rank']:
            if avg[subject] >= 75:
                print(f"{subject} is performing well across the class.")
            elif avg[subject] >= 60:
                print(f"{subject} shows average performance.")
            else:
                print(f"{subject} needs improvement across students.")

    # Final Suggestions
    print("\nSuggestions:\n")

    weak_subjects = [sub for sub in avg.index if avg[sub] < 60]

    if weak_subjects:
        print("Students should focus more on:", ", ".join(weak_subjects))
    else:
        print("Overall performance across subjects is balanced.")

if __name__ == "__main__":
    file = input("Enter CSV file name: ")
    generate_story(file)