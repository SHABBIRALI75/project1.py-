import pandas as pd
import os


# --- Step 1: RescuePet Class ---
class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False  # Default attribute

    def process_adoption(self):
        self.is_adopted = True


# --- Step 2: Combining Data (Pandas) ---
df_a = pd.read_csv("shelter_A.csv")
df_b = pd.read_csv("shelter_B.csv")

# Dono databases ko combine kerna
combined_df = pd.concat([df_a, df_b], ignore_index=True)

# --- Step 3: Data Cleaning ---
# Missing data (Bella ki khali age) wali row delete kerna
cleaned_df = combined_df.dropna()

# Sirf Dogs ko filter kerna
dogs_df = cleaned_df[cleaned_df["Animal_Type"] == "Dog"]

# --- Step 4: Integration ---
# Kisi ek dog ko adoption ke liye pick kerna (e.g., Lucy)
if not dogs_df.empty:
    # Hum Lucy ko select kerte hain jo index 3 per thi (Cleaned data mein se)
    selected_row = dogs_df.iloc[2]  # Max ya koi bhi dog choose karein

    pet_obj = RescuePet(selected_row["Pet_Name"], selected_row["Animal_Type"], selected_row["Age_Years"])

    # Adoption process run kerna
    pet_obj.process_adoption()

    # --- Step 5: Exporting (Append Mode) ---
    new_data = {
        "Pet_Name": [pet_obj.name],
        "Animal_Type": [pet_obj.species],
        "Age_Years": [pet_obj.age],
        "Is_Adopted": [pet_obj.is_adopted]
    }

    final_report = pd.DataFrame(new_data)

    # Mode='a' (Append) taakay file overwrite na ho
    file_exists = os.path.isfile("successful_adoptions.csv")
    final_report.to_csv("successful_adoptions.csv", mode='a', index=False, header=not file_exists)

    print(f"Success: {pet_obj.name} ko adopt ker liya gaya hai!")
    print("\nMerged and Cleaned Dog List:\n", dogs_df)
else:
    print("Koi dog adoption ke liye mojud nahi.")