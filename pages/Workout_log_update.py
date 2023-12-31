import streamlit as st
import datetime as dt
import numpy as np
import pandas as pd

st.set_page_config(page_title="Enter Meals", page_icon="📈")

diary = pd.read_csv("Workout.csv")
Excercise = ["Bar Dip", "Bench Press", "Cable Chest Press", "Close-Grip Bench Press", "Close-Grip Feet-Up Bench Press", "Decline Bench Press", "Dumbbell Chest Fly", "Dumbbell Chest Press", "Dumbbell Decline Chest Press", "Dumbbell Floor Press", "Dumbbell Pullover", "Feet-Up Bench Press", "Floor Press", "Incline Bench Press", "Incline Dumbbell Press", "Incline Push-Up", "Kneeling Incline Push-Up", "Kneeling Push-Up", "Machine Chest Fly", "Machine Chest Press", "Pec Deck", "Push-Up", "Push-Up Against Wall", "Push-Ups With Feet in Rings", "Resistance Band Chest Fly", "Smith Machine Bench Press", "Smith Machine Incline Bench Press", "Standing Cable Chest Fly", "Standing Resistance Band Chest Fly", "Band External Shoulder Rotation", "Band Internal Shoulder Rotation", "Band Pull-Apart", "Barbell Front Raise", "Barbell Rear Delt Row", "Barbell Upright Row", "Behind the Neck Press", "Cable Lateral Raise", "Cable Rear Delt Row", "Dumbbell Front Raise", "Dumbbell Horizontal Internal Shoulder Rotation", "Dumbbell Horizontal External Shoulder Rotation", "Dumbbell Lateral Raise", "Dumbbell Rear Delt Row", "Dumbbell Shoulder Press", "Face Pull", "Front Hold", "Lying Dumbbell External Shoulder Rotation", "Lying Dumbbell Internal Shoulder Rotation", "Machine Lateral Raise", "Machine Shoulder Press", "Monkey Row", "Overhead Press", "Plate Front Raise", "Power Jerk", "Push Press", "Reverse Cable Flyes", "Reverse Dumbbell Flyes", "Reverse Machine Fly", "Seated Dumbbell Shoulder Press", "Seated Barbell Overhead Press", "Seated Smith Machine Shoulder Press", "Snatch Grip Behind the Neck Press", "Squat Jerk", "Split Jerk", "Barbell Curl", "Barbell Preacher Curl", "Bodyweight Curl", "Cable Curl With Bar", "Cable Curl With Rope", "Concentration Curl", "Dumbbell Curl", "Dumbbell Preacher Curl", "Hammer Curl", "Incline Dumbbell Curl", "Machine Bicep Curl", "Spider Curl", "Barbell Standing Triceps Extension", "Barbell Lying Triceps Extension", "Bench Dip", "Close-Grip Push-Up", "Dumbbell Lying Triceps Extension", "Dumbbell Standing Triceps Extension", "Overhead Cable Triceps Extension", "Tricep Bodyweight Extension", "Tricep Pushdown With Bar", "Tricep Pushdown With Rope", "Air Squat", "Barbell Hack Squat", "Barbell Lunge", "Barbell Walking Lunge", "Belt Squat", "Body Weight Lunge", "Box Squat", "Bulgarian Split Squat", "Chair Squat", "Dumbbell Lunge", "Dumbbell Squat", "Front Squat", "Goblet Squat", "Hack Squat Machine", "Half Air Squat", "Hip Adduction Machine", "Landmine Hack Squat", "Landmine Squat", "Leg Extension", "Leg Press", "Lying Leg Curl", "Pause Squat", "Romanian Deadlift", "Safety Bar Squat", "Seated Leg Curl", "Shallow Body Weight Lunge", "Side Lunges (Bodyweight)", "Smith Machine Squat", "Squat", "Step Up", "Back Extension", "Barbell Row", "Barbell Shrug", "Block Snatch", "Cable Close Grip Seated Row", "Cable Wide Grip Seated Row", "Chin-Up", "Clean", "Clean and Jerk", "Deadlift", "Deficit Deadlift", "Dumbbell Deadlift", "Dumbbell Row", "Dumbbell Shrug", "Floor Back Extension", "Good Morning", "Hang Clean", "Hang Power Clean", "Hang Power Snatch", "Hang Snatch", "Inverted Row", "Inverted Row with Underhand Grip", "Jefferson Curl", "Kettlebell Swing. Lat Pulldown With Pronated Grip", "Lat Pulldown With Supinated Grip", "One-Handed Cable Row", "One-Handed Lat Pulldown", "Pause Deadlift", "Pendlay Row", "Power Clean", "Power Snatch", "Pull-Up", "Rack Pull", "Seal Row", "Seated Machine Row", "Snatch", "Snatch Grip Deadlift", "Stiff-Legged Deadlift", "Straight Arm Lat Pulldown", "Sumo Deadlift", "T-Bar Row", "Trap Bar Deadlift With High Handles", "Trap Bar Deadlift With Low Handles", "Banded Side Kicks", "Cable Pull Through", "Clamshells", "Dumbbell Romanian Deadlift", "Dumbbell Frog Pumps", "Fire Hydrants", "Frog Pumps", "Glute Bridge", "Hip Abduction Against Band", "Hip Abduction Machine", "Hip Thrust", "Hip Thrust Machine", "Hip Thrust With Band Around Knees", "Lateral Walk With Band", "Machine Glute Kickbacks", "One-Legged Glute Bridge", "One-Legged Hip Thrust", "Romanian Deadlift", "Single Leg Romanian Deadlift", "Standing Glute Kickback in Machine", "Step Up", "Cable Crunch", "Crunch", "Dead Bug", "Hanging Leg Raise", "Hanging Knee Raise", "Hanging Sit-Up", "High to Low Wood Chop with Band", "Horizontal Wood Chop with Band", "Kneeling Ab Wheel Roll-Out", "Kneeling Plank", "Kneeling Side Plank", "Lying Leg Raise", "Lying Windshield Wiper", "Lying Windshield Wiper with Bent Knees", "Machine Crunch", "Mountain Climbers", "Oblique Crunch", "Oblique Sit-Up", "Plank", "Side Plank", "Sit-Up", "Eccentric Heel Drop", "Heel Raise", "Seated Calf Raise", "Standing Calf Raise", "Barbell Wrist Curl", "Barbell Wrist Curl Behind the Back", "Bar Hang", "Dumbbell Wrist Curl", "Farmers Walk", "Fat Bar Deadlift", "Gripper", "One-Handed Bar Hang", "Plate Pinch", "Plate Wrist Curl", "Towel Pull-Up", "Barbell Wrist Extension", "Dumbbell Wrist Extension"]

def update_user_diary(date, exname, amount, sets, reps, diary):
 RepMax = 0.0333*reps*amount+amount
 volume = amount*sets*reps
 diary.loc[len(diary.index)] = [date, exname, amount, reps, sets, volume, RepMax]
 diary.to_csv('Workout.csv')


st.markdown("# Workout Log")
st.sidebar.header("Workout Log")
st.write(
    """Add your current workout to the log."""
)


st.write("## Add Excercise")
date = st.date_input('Select Date', dt.date.today())
exname = st.selectbox( 'What did you train Today', Excercise)
sets = st.number_input('How many sets did you do?',  min_value=0.0, max_value=10000.0, value=0.0, step=0.1)
amount = st.number_input('How much weight did you lift (in kg)?', min_value=0.0, max_value=10000.0, value=0.0, step=0.1)
reps = st.number_input('How many reps in a set?', min_value=0.0, max_value=10000.0, value=0.0, step=0.1)
if st.button("Add to Diary"):
    update_user_diary(date, exname, amount, sets, reps, diary)
    st.success("Excercise added to diary!")
else:
    st.info("Click on 'Add to Diary' to add your excercise to the diary.")



# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")