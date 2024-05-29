import streamlit as st
import plotly.graph_objects as go

def evaluate_sleep_apnea(recording_time, lowest_spo2, num_drops_per_hour):
    """
    Evaluates sleep apnea severity based on recording time, lowest SpO2, and drops per hour.

    Parameters:
    recording_time (float): Total recording time in hours.
    lowest_spo2 (int): The lowest recorded SpO2 value.
    num_drops_per_hour (float): Number of drops (desaturations) per hour.

    Returns:
    tuple: A tuple containing the severity message and severity level.
    """

    if num_drops_per_hour < 5:
        severity = "No Sleep Apnea Likely"
        severity_level = 0
    elif 5 <= num_drops_per_hour < 15:
        severity = "Mild Sleep Apnea"
        severity_level = 1
    elif 15 <= num_drops_per_hour < 30:
        severity = "Moderate Sleep Apnea"
        severity_level = 2
    else:
        severity = "Severe Sleep Apnea"
        severity_level = 3

    return severity, severity_level


def main():
    st.set_page_config(page_title="Sleep Apnea Detection")
    st.title("Sleep Apnea Detection")

    st.write(
        "The standard overnight pulse oximeter test is an effective initial screening tool for detecting signs of sleep apnea. "
        "In simple terms, a pulse oximeter measures the oxygen level in your blood. Oxygen-rich blood is essential for brain function, "
        "and maintaining an oxygen saturation level above 94% during sleep indicates that your brain is receiving sufficient oxygen, "
        "helping you wake up refreshed. However, if the brain does not consistently receive enough oxygen during sleep, you may exhibit signs of sleep apnea, "
        "such as morning headaches, excessive daytime tiredness, insomnia, snoring, gasping for air during sleep, and dry mouth.\n\n"
        "When reviewing the pulse oximeter report, focus on the following key items:\n\n"
        "1. The duration of the recording during the night.\n"
        "2. The SpO2 Summary, which estimates the amount of oxygen in your blood.\n"
        "3. The SpO2 Distribution.\n\n"
        "Please note that this site is for informational purposes only and is not intended for medical evaluation. "
        "Review the information from your pulse oximeter test and enter the values into the input fields below."
    )

    st.write("")

    recording_time = st.number_input("Enter the recording time in hours:", min_value=0.0, format="%.2f")
    lowest_spo2 = st.number_input("Enter the lowest SpO2 percentage:", min_value=0, max_value=100)
    num_drops_per_hour = st.number_input("Enter the number of drops (desaturations) per hour:", min_value=0.0, format="%.2f")

    if st.button("Evaluate"):
        severity, severity_level = evaluate_sleep_apnea(recording_time, lowest_spo2, num_drops_per_hour)
        st.write(f"Severity: {severity}")

        # Generate the bar chart
        fig = go.Figure(go.Bar(
            x=["No Sleep Apnea", "Mild Sleep Apnea", "Moderate Sleep Apnea", "Severe Sleep Apnea"],
            y=[1 if severity_level == 0 else 0, 1 if severity_level == 1 else 0, 1 if severity_level == 2 else 0, 1 if severity_level == 3 else 0],
            marker_color=['green', 'yellow', 'orange', 'red']
        ))

        fig.update_layout(
            title="Sleep Apnea Severity",
            xaxis_title="Severity Level",
            yaxis_title="Presence",
            yaxis=dict(tickvals=[0, 1], ticktext=['Absent', 'Present']),
            showlegend=False
        )

        st.plotly_chart(fig)


if __name__ == "__main__":
    main()


# import streamlit as st
#
#
# def evaluate_sleep_apnea(recording_time, lowest_spo2, num_drops_per_hour):
#     """
#     Evaluates sleep apnea severity based on recording time, lowest SpO2, and drops per hour.
#
#     Parameters:
#     recording_time (float): Total recording time in hours.
#     lowest_spo2 (int): The lowest recorded SpO2 value.
#     num_drops_per_hour (float): Number of drops (desaturations) per hour.
#
#     Returns:
#     str: A message indicating the likelihood of sleep apnea.
#     """
#
#     if num_drops_per_hour < 5:
#         severity = "No Sleep Apnea Likely"
#     elif 5 <= num_drops_per_hour < 15:
#         severity = "Mild Sleep Apnea"
#     elif 15 <= num_drops_per_hour < 30:
#         severity = "Moderate Sleep Apnea"
#     else:
#         severity = "Severe Sleep Apnea"
#
#     # Return the results
#     result = f"Severity: {severity}\n"
#     return result
#
#
# def main():
#     st.set_page_config(page_title="Sleep Apnea Detection")
#     st.title("Sleep Apnea Detection")
#
#     st.write(
#         "The standard overnight pulse oximeter test is an effective initial screening tool for detecting signs of sleep apnea. "
#         "In simple terms, a pulse oximeter measures the oxygen level in your blood. Oxygen-rich blood is essential for brain function, "
#         "and maintaining an oxygen saturation level above 94% during sleep indicates that your brain is receiving sufficient oxygen, "
#         "helping you wake up refreshed. However, if the brain does not consistently receive enough oxygen during sleep, you may exhibit signs of sleep apnea, "
#         "such as morning headaches, excessive daytime tiredness, insomnia, snoring, gasping for air during sleep, and dry mouth.\n\n"
#         "When reviewing the pulse oximeter report, focus on the following key items:\n\n"
#         "1. The duration of the recording during the night.\n"
#         "2. The SpO2 Summary, which estimates the amount of oxygen in your blood.\n"
#         "3. The SpO2 Distribution.\n\n"
#         "Please note that this site is for informational purposes only and is not intended for medical evaluation. "
#         "Review the information from your pulse oximeter test and enter the values into the input fields below."
#     )
#
#     recording_time = st.number_input("Enter the recording time in hours:", min_value=0.0, format="%.2f")
#     lowest_spo2 = st.number_input("Enter the lowest SpO2 percentage:", min_value=0, max_value=100)
#     num_drops_per_hour = st.number_input("Enter the number of drops (desaturations) per hour:", min_value=0.0,
#                                          format="%.2f")
#
#     if st.button("Evaluate"):
#         result = evaluate_sleep_apnea(recording_time, lowest_spo2, num_drops_per_hour)
#         st.write(result)
#
#
# if __name__ == "__main__":
#     main()
