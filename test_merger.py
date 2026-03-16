"""
Unit Tests for Excel Merger Application
Run: pytest test_merger.py -v
Or: python -m pytest test_merger.py
"""

import pandas as pd
import sys
import os
from io import BytesIO

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Mock streamlit since tests run without UI
class MockUploadedFile:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self.getvalue = lambda: self.data
    
    def read(self):
        return self.data
    
    def seek(self, pos):
        pass


def create_test_dataframe(rows=100, columns=['A', 'B', 'C']):
    """Create a simple test DataFrame"""
    data = {col: list(range(rows)) for col in columns}
    return pd.DataFrame(data)


def test_basic_merge():
    """Test: Merge two simple DataFrames"""
    df1 = create_test_dataframe(100, ['ID', 'Name', 'Age'])
    df2 = create_test_dataframe(100, ['ID', 'Name', 'City'])
    
    # Merge logic (from app.py)
    all_columns = list(dict.fromkeys(list(df1.columns) + list(df2.columns)))
    
    for col in all_columns:
        if col not in df1.columns:
            df1[col] = ""
        if col not in df2.columns:
            df2[col] = ""
    
    merged = pd.concat([df1[all_columns], df2[all_columns]], ignore_index=True)
    
    # Assertions
    assert len(merged) == 200, f"Expected 200 rows, got {len(merged)}"
    assert len(merged.columns) == 4, f"Expected 4 columns, got {len(merged.columns)}"
    assert set(merged.columns) == {'ID', 'Name', 'Age', 'City'}, f"Unexpected columns: {merged.columns}"
    
    print("✅ test_basic_merge PASSED")


def test_column_mismatch():
    """Test: Merge DataFrames with different columns"""
    df1 = create_test_dataframe(50, ['A', 'B', 'C'])
    df2 = create_test_dataframe(50, ['A', 'D', 'E'])
    
    all_columns = list(dict.fromkeys(list(df1.columns) + list(df2.columns)))
    
    for col in all_columns:
        if col not in df1.columns:
            df1[col] = ""
        if col not in df2.columns:
            df2[col] = ""
    
    merged = pd.concat([df1[all_columns], df2[all_columns]], ignore_index=True)
    
    assert set(merged.columns) == {'A', 'B', 'C', 'D', 'E'}, f"Column union failed: {merged.columns}"
    assert len(merged) == 100, f"Expected 100 rows, got {len(merged)}"
    
    print("✅ test_column_mismatch PASSED")


def test_no_data_loss():
    """Test: Ensure no rows are dropped during merge"""
    sizes = [50, 75, 100, 150, 200]
    
    for size1 in sizes:
        for size2 in sizes:
            df1 = create_test_dataframe(size1)
            df2 = create_test_dataframe(size2)
            
            all_columns = list(dict.fromkeys(list(df1.columns) + list(df2.columns)))
            
            for col in all_columns:
                if col not in df1.columns:
                    df1[col] = ""
                if col not in df2.columns:
                    df2[col] = ""
            
            merged = pd.concat([df1[all_columns], df2[all_columns]], ignore_index=True)
            
            expected_rows = size1 + size2
            assert len(merged) == expected_rows, \
                f"Data loss detected: {size1}+{size2}={expected_rows}, got {len(merged)}"
    
    print("✅ test_no_data_loss PASSED")


def test_blank_cells_preserved():
    """Test: Blank cells remain blank after merge"""
    df1 = pd.DataFrame({
        'ID': [1, 2, 3],
        'Name': ['John', '', 'Bob'],
        'Email': ['john@test.com', 'jane@test.com', '']
    })
    
    df2 = pd.DataFrame({
        'ID': [4, 5],
        'Name': ['Alice', 'Charlie'],
        'Phone': ['555-1234', '']
    })
    
    # Fill blanks with empty string
    df1 = df1.fillna("")
    df2 = df2.fillna("")
    
    all_columns = list(dict.fromkeys(list(df1.columns) + list(df2.columns)))
    
    for col in all_columns:
        if col not in df1.columns:
            df1[col] = ""
        if col not in df2.columns:
            df2[col] = ""
    
    merged = pd.concat([df1[all_columns], df2[all_columns]], ignore_index=True)
    
    # Check blank preservation
    assert merged.loc[1, 'Name'] == '', "Blank cell not preserved in Name column"
    assert merged.loc[0, 'Email'] == 'john@test.com', "Data changed"
    assert merged.loc[2, 'Email'] == '', "Blank not preserved in Email"
    
    print("✅ test_blank_cells_preserved PASSED")


def test_large_file_handling():
    """Test: Handle large files (50k+ rows)"""
    print("   (Creating large test data... this may take a few seconds)")
    
    df1 = create_test_dataframe(50000, ['A', 'B', 'C', 'D', 'E'])
    df2 = create_test_dataframe(50000, ['A', 'B', 'F', 'G'])
    
    all_columns = list(dict.fromkeys(list(df1.columns) + list(df2.columns)))
    
    for col in all_columns:
        if col not in df1.columns:
            df1[col] = ""
        if col not in df2.columns:
            df2[col] = ""
    
    merged = pd.concat([df1[all_columns], df2[all_columns]], ignore_index=True)
    
    assert len(merged) == 100000, f"Expected 100k rows, got {len(merged)}"
    assert len(merged.columns) == 7, f"Expected 7 columns, got {len(merged.columns)}"
    
    print("✅ test_large_file_handling PASSED")


def test_column_order_preservation():
    """Test: Column order is preserved from first file"""
    df1 = pd.DataFrame({
        'ID': [1, 2],
        'Name': ['A', 'B'],
        'Age': [25, 30]
    })
    
    df2 = pd.DataFrame({
        'City': ['NYC', 'LA'],
        'ID': [3, 4],
        'Phone': ['555-1234', '555-5678']
    })
    
    all_columns = list(dict.fromkeys(list(df1.columns) + list(df2.columns)))
    expected_order = ['ID', 'Name', 'Age', 'City', 'Phone']
    
    assert all_columns == expected_order, \
        f"Column order not preserved. Got {all_columns}, expected {expected_order}"
    
    print("✅ test_column_order_preservation PASSED")


def test_empty_dataframe_handling():
    """Test: Handle empty columns gracefully"""
    df1 = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['', '', '']
    })
    
    df2 = pd.DataFrame({
        'A': [4, 5],
        'C': ['x', 'y']
    })
    
    df1 = df1.fillna("")
    df2 = df2.fillna("")
    
    all_columns = list(dict.fromkeys(list(df1.columns) + list(df2.columns)))
    
    for col in all_columns:
        if col not in df1.columns:
            df1[col] = ""
        if col not in df2.columns:
            df2[col] = ""
    
    merged = pd.concat([df1[all_columns], df2[all_columns]], ignore_index=True)
    
    assert len(merged) == 5, f"Expected 5 rows, got {len(merged)}"
    assert merged.loc[0, 'B'] == '', "Empty column not preserved"
    
    print("✅ test_empty_dataframe_handling PASSED")


def test_duplicate_column_names():
    """Test: Handle duplicate column names"""
    df1 = pd.DataFrame({
        'ID': [1, 2],
        'Name': ['A', 'B'],
        'Value': [10, 20]
    })
    
    df2 = pd.DataFrame({
        'ID': [3, 4],
        'Name': ['C', 'D'],
        'Value': [30, 40]
    })
    
    all_columns = list(dict.fromkeys(list(df1.columns) + list(df2.columns)))
    # Remove duplicates by keeping unique (dict.fromkeys maintains order)
    assert len(all_columns) == 3, f"Duplicate columns not handled"
    
    print("✅ test_duplicate_column_names PASSED")


# ============================================================================
# Run Tests
# ============================================================================

def run_all_tests():
    """Run all tests"""
    tests = [
        test_basic_merge,
        test_column_mismatch,
        test_no_data_loss,
        test_blank_cells_preserved,
        test_large_file_handling,
        test_column_order_preservation,
        test_empty_dataframe_handling,
        test_duplicate_column_names,
    ]
    
    print("="*60)
    print("🧪 Running Excel Merger Tests")
    print("="*60)
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            print(f"\n▶️  {test.__name__}")
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} ERROR: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"📊 Results: {passed} passed, {failed} failed")
    print("="*60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
