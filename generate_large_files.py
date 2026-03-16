"""
Generate large sample files for realistic testing
- 2 files
- 70,000-80,000 rows each
- 30 columns each
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_large_sample_files():
    """Generate two large realistic sample files"""
    
    print("Generating large sample files for realistic testing...")
    print("This may take 1-2 minutes...\n")
    
    # Define 30 columns for patient data
    columns = [
        'PatientID', 'FirstName', 'LastName', 'Age', 'Gender',
        'DateOfBirth', 'Phone', 'Email', 'Address', 'City',
        'State', 'ZipCode', 'BloodType', 'Allergies', 'Medications',
        'PrimaryDoctor', 'LastVisitDate', 'VisitReason', 'Diagnosis', 'Treatment',
        'Insurance', 'InsuranceID', 'EmergencyContact', 'EmergencyPhone', 'MedicalHistory',
        'Height', 'Weight', 'BMI', 'Notes', 'Status'
    ]
    
    # Generate File 1 (75,000 rows)
    print("📊 Creating large_file_1.xlsx (75,000 rows × 30 columns)...")
    
    first_names = ['John', 'Jane', 'Robert', 'Mary', 'Michael', 'Patricia', 'James', 'Jennifer',
                   'William', 'Linda', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica',
                   'Thomas', 'Sarah', 'Charles', 'Karen', 'Christopher', 'Nancy', 'Daniel', 'Lisa',
                   'Matthew', 'Betty', 'Anthony', 'Margaret', 'Donald', 'Sandra']
    
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
                  'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
                  'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'White', 'Harris',
                  'Martin', 'Thompson', 'Robinson', 'Clark', 'Scott', 'Green', 'Hill']
    
    blood_types = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    doctors = ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams', 'Dr. Brown', 'Dr. Jones', 'Dr. Garcia']
    statuses = ['Active', 'Inactive', 'Pending', 'Completed']
    
    rows_file1 = 75000
    
    # Generate base date for DoB calculations
    base_date = datetime(1950, 1, 1)
    
    data1 = {
        'PatientID': range(10001, 10001 + rows_file1),
        'FirstName': [random.choice(first_names) for _ in range(rows_file1)],
        'LastName': [random.choice(last_names) for _ in range(rows_file1)],
        'Age': [random.randint(18, 95) for _ in range(rows_file1)],
        'Gender': [random.choice(['M', 'F']) for _ in range(rows_file1)],
        'DateOfBirth': [(base_date + timedelta(days=random.randint(0, 365*70))).strftime('%Y-%m-%d') 
                        for _ in range(rows_file1)],
        'Phone': [f"+1-{random.randint(200, 999)}-{random.randint(200, 999)}-{random.randint(1000, 9999)}" 
                  for _ in range(rows_file1)],
        'Email': [f"patient_{i}@example.com" for i in range(rows_file1)],
        'Address': [f"{random.randint(100, 9999)} {random.choice(['Main', 'Oak', 'Elm', 'Pine', 'Maple'])} St" 
                    for _ in range(rows_file1)],
        'City': [random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 
                               'San Antonio', 'San Diego', 'Dallas', 'San Jose']) for _ in range(rows_file1)],
        'State': [random.choice(['NY', 'CA', 'TX', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI']) 
                 for _ in range(rows_file1)],
        'ZipCode': [f"{random.randint(10000, 99999)}" for _ in range(rows_file1)],
        'BloodType': [random.choice(blood_types) for _ in range(rows_file1)],
        'Allergies': [random.choice(['None', 'Penicillin', 'Latex', 'Peanuts', 'Shellfish', 'Multiple', '']) 
                     for _ in range(rows_file1)],
        'Medications': [random.choice(['Aspirin', 'Metformin', 'Lisinopril', 'Atorvastatin', 'Omeprazole', 'None', '']) 
                       for _ in range(rows_file1)],
        'PrimaryDoctor': [random.choice(doctors) for _ in range(rows_file1)],
        'LastVisitDate': [(datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d') 
                         for _ in range(rows_file1)],
        'VisitReason': [random.choice(['Checkup', 'Follow-up', 'Consultation', 'Lab Work', 'Vaccination', '']) 
                       for _ in range(rows_file1)],
        'Diagnosis': [random.choice(['Hypertension', 'Diabetes', 'Asthma', 'COPD', 'Healthy', 'Unknown', '']) 
                     for _ in range(rows_file1)],
        'Treatment': [random.choice(['Medication', 'Therapy', 'Surgery', 'Monitoring', 'Lifestyle', 'None', '']) 
                     for _ in range(rows_file1)],
        'Insurance': [random.choice(['Aetna', 'BlueCross', 'Cigna', 'Humana', 'UnitedHealth', 'Uninsured']) 
                     for _ in range(rows_file1)],
        'InsuranceID': [f"INS{random.randint(100000, 999999)}" for _ in range(rows_file1)],
        'EmergencyContact': [f"{random.choice(first_names)} {random.choice(last_names)}" 
                            for _ in range(rows_file1)],
        'EmergencyPhone': [f"+1-{random.randint(200, 999)}-{random.randint(200, 999)}-{random.randint(1000, 9999)}" 
                          for _ in range(rows_file1)],
        'MedicalHistory': [random.choice(['Clear', 'Significant', 'Family History', 'Complex', '']) 
                          for _ in range(rows_file1)],
        'Height': [f"{random.randint(60, 80)}\"" for _ in range(rows_file1)],
        'Weight': [f"{random.randint(110, 250)} lbs" for _ in range(rows_file1)],
        'BMI': [f"{round(random.uniform(18, 35), 1)}" for _ in range(rows_file1)],
        'Notes': [random.choice(['Regular monitoring', 'Needs follow-up', 'Stable condition', 'Under treatment', '']) 
                 for _ in range(rows_file1)],
        'Status': [random.choice(statuses) for _ in range(rows_file1)]
    }
    
    df1 = pd.DataFrame(data1)
    df1.to_excel('large_file_1.xlsx', index=False, sheet_name='Patients')
    print(f"   ✅ Created: {len(df1):,} rows × {len(df1.columns)} columns")
    
    # Generate File 2 (80,000 rows) - slightly different columns to test merge
    print("\n📊 Creating large_file_2.xlsx (80,000 rows × 30 columns)...")
    
    rows_file2 = 80000
    
    data2 = {
        'PatientID': range(85001, 85001 + rows_file2),
        'FirstName': [random.choice(first_names) for _ in range(rows_file2)],
        'LastName': [random.choice(last_names) for _ in range(rows_file2)],
        'Age': [random.randint(18, 95) for _ in range(rows_file2)],
        'Gender': [random.choice(['M', 'F']) for _ in range(rows_file2)],
        'DateOfBirth': [(base_date + timedelta(days=random.randint(0, 365*70))).strftime('%Y-%m-%d') 
                        for _ in range(rows_file2)],
        'Phone': [f"+1-{random.randint(200, 999)}-{random.randint(200, 999)}-{random.randint(1000, 9999)}" 
                  for _ in range(rows_file2)],
        'Email': [f"patient_{i}@example.com" for i in range(rows_file2)],
        'Address': [f"{random.randint(100, 9999)} {random.choice(['Main', 'Oak', 'Elm', 'Pine', 'Maple'])} St" 
                    for _ in range(rows_file2)],
        'City': [random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 
                               'San Antonio', 'San Diego', 'Dallas', 'San Jose']) for _ in range(rows_file2)],
        'State': [random.choice(['NY', 'CA', 'TX', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI']) 
                 for _ in range(rows_file2)],
        'ZipCode': [f"{random.randint(10000, 99999)}" for _ in range(rows_file2)],
        'BloodType': [random.choice(blood_types) for _ in range(rows_file2)],
        'Allergies': [random.choice(['None', 'Penicillin', 'Latex', 'Peanuts', 'Shellfish', 'Multiple', '']) 
                     for _ in range(rows_file2)],
        'Medications': [random.choice(['Aspirin', 'Metformin', 'Lisinopril', 'Atorvastatin', 'Omeprazole', 'None', '']) 
                       for _ in range(rows_file2)],
        'PrimaryDoctor': [random.choice(doctors) for _ in range(rows_file2)],
        'LastVisitDate': [(datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d') 
                         for _ in range(rows_file2)],
        'VisitReason': [random.choice(['Checkup', 'Follow-up', 'Consultation', 'Lab Work', 'Vaccination', '']) 
                       for _ in range(rows_file2)],
        'Diagnosis': [random.choice(['Hypertension', 'Diabetes', 'Asthma', 'COPD', 'Healthy', 'Unknown', '']) 
                     for _ in range(rows_file2)],
        'Treatment': [random.choice(['Medication', 'Therapy', 'Surgery', 'Monitoring', 'Lifestyle', 'None', '']) 
                     for _ in range(rows_file2)],
        'Insurance': [random.choice(['Aetna', 'BlueCross', 'Cigna', 'Humana', 'UnitedHealth', 'Uninsured']) 
                     for _ in range(rows_file2)],
        'InsuranceID': [f"INS{random.randint(100000, 999999)}" for _ in range(rows_file2)],
        'EmergencyContact': [f"{random.choice(first_names)} {random.choice(last_names)}" 
                            for _ in range(rows_file2)],
        'EmergencyPhone': [f"+1-{random.randint(200, 999)}-{random.randint(200, 999)}-{random.randint(1000, 9999)}" 
                          for _ in range(rows_file2)],
        'MedicalHistory': [random.choice(['Clear', 'Significant', 'Family History', 'Complex', '']) 
                          for _ in range(rows_file2)],
        'Height': [f"{random.randint(60, 80)}\"" for _ in range(rows_file2)],
        'Weight': [f"{random.randint(110, 250)} lbs" for _ in range(rows_file2)],
        'BMI': [f"{round(random.uniform(18, 35), 1)}" for _ in range(rows_file2)],
        'Notes': [random.choice(['Regular monitoring', 'Needs follow-up', 'Stable condition', 'Under treatment', '']) 
                 for _ in range(rows_file2)],
        'Status': [random.choice(statuses) for _ in range(rows_file2)]
    }
    
    df2 = pd.DataFrame(data2)
    df2.to_excel('large_file_2.xlsx', index=False, sheet_name='Patients')
    print(f"   ✅ Created: {len(df2):,} rows × {len(df2.columns)} columns")
    
    print("\n" + "="*60)
    print("✅ Large sample files generated successfully!")
    print("="*60)
    print(f"\nTest files created:")
    print(f"  • large_file_1.xlsx ({len(df1):,} rows × {len(df1.columns)} columns)")
    print(f"  • large_file_2.xlsx ({len(df2):,} rows × {len(df2.columns)} columns)")
    print(f"\nCombined result will have:")
    print(f"  • {len(df1) + len(df2):,} rows")
    print(f"  • {len(df1.columns)} columns")
    print(f"\nYou can now:")
    print(f"  1. Upload large_file_1.xlsx")
    print(f"  2. Upload large_file_2.xlsx")
    print(f"  3. Click 'Merge Files'")
    print(f"  4. Download the result")
    print(f"\nExpected merge time: ~3-5 seconds")

if __name__ == "__main__":
    try:
        import pandas as pd
        generate_large_sample_files()
    except ImportError:
        print("❌ pandas is not installed")
        print("Install it with: pip install pandas openpyxl")
    except Exception as e:
        print(f"❌ Error: {e}")
