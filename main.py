import streamlit as st

def evaluate_sleep_apnea(recording_time, lowest_spo2, num_drops_per_hour):
    """
    Evaluates sleep apnea severity based on recording time, lowest SpO2, and drops per hour.

    Parameters:
    recording_time (float): Total recording time in hours.
    lowest_spo2 (int): The lowest recorded SpO2 value.
    num_drops_per_hour (float): Number of drops (desaturations) per hour.

    Returns:
    str: A message indicating the likelihood of sleep apnea.
    """

    if num_drops_per_hour < 5:
        severity = "No Sleep Apnea Likely"
    elif 5 <= num_drops_per_hour < 15:
        severity = "Mild Sleep Apnea"
    elif 15 <= num_drops_per_hour < 30:
        severity = "Moderate Sleep Apnea"
    else:
        severity = "Severe Sleep Apnea"

    # Return the results
    result = (
        # f"Recording Time: {recording_time} hours\n"
        # f"Lowest SpO2: {lowest_spo2}%\n"
        # f"Drops per Hour: {num_drops_per_hour:.2f}\n"
        f"Severity: {severity}\n"
    )

    return result


def main():
    st.title("Sleep Apnea Evaluator")

    recording_time = st.number_input("Enter the recording time in hours:", min_value=0.0, format="%.2f")
    lowest_spo2 = st.number_input("Enter the lowest SpO2 percentage:", min_value=0, max_value=100)
    num_drops_per_hour = st.number_input("Enter the number of drops (desaturations) per hour:", min_value=0.0,
                                         format="%.2f")

    if st.button("Evaluate"):
        result = evaluate_sleep_apnea(recording_time, lowest_spo2, num_drops_per_hour)
        st.write(result)


if __name__ == "__main__":
    main()
