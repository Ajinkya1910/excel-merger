"""
Sample Data Generator for Testing
Run: python generate_sample_data.py
"""

import pandas as pd
import random
import sys

def generate_sample_files():
    """Generate sample Excel files for testing"""
    
    print("Generating sample files for testing...")
    
    # Sample File 1 - Patient Demographics
    print("\n📊 Creating sample_file_1.xlsx...")
    
    patient_ids_1 = list(range(10001, 11001))
    first_names = ['John', 'Jane', 'Robert', 'Mary', 'Michael', 'Patricia', 'James', 'Jennifer']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis']
    
    df1 = pd.DataFrame({
        'Patient_ID': patient_ids_1,
        'First_Name': [random.choice(first_names) for _ in range(1000)],
        'Last_Name': [random.choice(last_names) for _ in range(1000)],
        'Age': [random.randint(18, 85) for _ in range(1000)],
        'Gender': [random.choice(['M', 'F']) for _ in range(1000)],
        'Phone': [f"555-{random.randint(1000, 9999)}" for _ in range(1000)],
        'Address': [f"{random.randint(100, 9999)} Main St" for _ in range(1000)],
    })
    
    df1.to_excel('sample_file_1.xlsx', index=False)
    print(f"   ✅ Created: {len(df1)} rows × {len(df1.columns)} columns")
    
    # Sample File 2 - Patient Medical Info
    print("\n📊 Creating sample_file_2.xlsx...")
    
    patient_ids_2 = list(range(11001, 12001))
    blood_types = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    
    df2 = pd.DataFrame({
        'Patient_ID': patient_ids_2,
        'First_Name': [random.choice(first_names) for _ in range(1000)],
        'Last_Name': [random.choice(last_names) for _ in range(1000)],
        'Age': [random.randint(18, 85) for _ in range(1000)],
        'Email': [f"patient_{i}@example.com" for i in range(1000)],
        'Blood_Type': [random.choice(blood_types) for _ in range(1000)],
        'Last_Visit': [f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}" for _ in range(1000)],
    })
    
    df2.to_excel('sample_file_2.xlsx', index=False)
    print(f"   ✅ Created: {len(df2)} rows × {len(df2.columns)} columns")
    
    # Sample File 3 - Large File for Performance Testing
    print("\n📊 Creating sample_large_file.xlsx...")
    
    large_size = 50000
    patient_ids_large = list(range(20001, 20001 + large_size))
    
    df_large = pd.DataFrame({
        'Patient_ID': patient_ids_large,
        'First_Name': [random.choice(first_names) for _ in range(large_size)],
        'Last_Name': [random.choice(last_names) for _ in range(large_size)],
        'Age': [random.randint(18, 85) for _ in range(large_size)],
        'Phone': [f"555-{random.randint(1000, 9999)}" for _ in range(large_size)],
        'Status': [random.choice(['Active', 'Inactive', 'Pending']) for _ in range(large_size)],
    })
    
    df_large.to_excel('sample_large_file.xlsx', index=False)
    print(f"   ✅ Created: {len(df_large):,} rows × {len(df_large.columns)} columns")
    
    # Sample CSV File
    print("\n📊 Creating sample_file_csv.csv...")
    
    df_csv = pd.DataFrame({
        'ID': range(1, 501),
        'Name': [f"Person_{i}" for i in range(1, 501)],
        'Score': [random.randint(50, 100) for _ in range(500)],
        'Notes': [f"Note_{i}" for i in range(1, 501)],
    })
    
    df_csv.to_csv('sample_file_csv.csv', index=False)
    print(f"   ✅ Created: {len(df_csv)} rows × {len(df_csv.columns)} columns")
    
    print("\n" + "="*50)
    print("✅ Sample files generated successfully!")
    print("="*50)
    print("\nTest files created:")
    print("  • sample_file_1.xlsx (1,000 rows)")
    print("  • sample_file_2.xlsx (1,000 rows)")
    print("  • sample_large_file.xlsx (50,000 rows)")
    print("  • sample_file_csv.csv (500 rows)")
    print("\nYou can now:")
    print("  1. Run: streamlit run app.py")
    print("  2. Upload any two sample files")
    print("  3. Merge them")
    print("  4. Download the result")
    print("\n")

if __name__ == "__main__":
    try:
        import pandas as pd
        generate_sample_files()
    except ImportError:
        print("❌ pandas is not installed")
        print("Install it with: pip install pandas openpyxl")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
