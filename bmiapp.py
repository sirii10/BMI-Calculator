import os

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)"""
    return round(weight / (height ** 2), 2)

def get_bmi_category(bmi):
    """Returns BMI category based on BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def log_result(weight, height_str, bmi, category):
    """Log results to a file with height in feet and inches"""
    with open("/data/bmi_results.txt", "a") as file:
        file.write(f"Weight: {weight} kg, Height: {height_str}, BMI: {bmi}, Category: {category}\n")

def main():
    print("BMI Calculator")
    weight = float(input("Enter your weight in kg: "))
    feet = int(input("Enter your height - Feet: "))
    inches = int(input("Enter your height - Inches: "))
    
    # Store height in feet and inches format
    height_str = f"{feet}'{inches}"
    
    # Convert height to meters for BMI calculation
    height_in_meters = (feet * 0.3048) + (inches * 0.0254)
    
    bmi = calculate_bmi(weight, height_in_meters)
    category = get_bmi_category(bmi)
    
    print(f"Your BMI: {bmi} ({category})")
    log_result(weight, height_str, bmi, category)
    print("Result saved to /data/bmi_results.txt")

if __name__ == "__main__":
    main()
