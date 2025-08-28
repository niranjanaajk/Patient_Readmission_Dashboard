# Patient Readmission Dashboard Demo

import pandas as pd

# Mock patient dataset
data = pd.DataFrame({
    'patient_id': [1, 2, 3, 4],
    'age': [65, 50, 80, 45],
    'previous_admissions': [2, 0, 3, 1],
    'readmission_risk': [1, 0, 1, 0]  # 1=High risk, 0=Low risk
})

# Example: filter high-risk patients
high_risk = data[data['readmission_risk'] == 1]

print("High-risk patients:")
print(high_risk)
