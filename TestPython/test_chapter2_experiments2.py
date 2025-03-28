import random
import sys
from pathlib import Path
import numpy as np
import subprocess
import importlib
import codewars_test
import pandas as pd

# Update paths and filename
path_answer = "/content/"  # changed
filename = "answer_chapter2_experiments2.py"  # changed

# Import the answer module
pc = importlib.import_module(filename[:-3], ".")
cmd = subprocess.run([sys.executable, f"{path_answer}{filename}"], capture_output=True)  # changed

@codewars_test.describe("Chapter 2 | Experiments 2")
def fixed_tests():

  @codewars_test.it("1. Test Load Data")
  def test_load_data():
      print("========================================================================")
      
          # Assuming expected columns are "Customer ID", "Age" and "Total Spent (USD)"
      expected_columns = ['BOROUGH', 'NEIGHBORHOOD', 'BUILDING CLASS CATEGORY',
                            'TAX CLASS AT PRESENT', 'BLOCK', 'LOT', 'EASE-MENT',
                            'BUILDING CLASS AT PRESENT', 'ADDRESS', 'APARTMENT NUMBER', 'ZIP CODE',
                            'RESIDENTIAL UNITS', 'COMMERCIAL UNITS', 'TOTAL UNITS',
                            'LAND SQUARE FEET', 'GROSS SQUARE FEET', 'YEAR BUILT',
                            'TAX CLASS AT TIME OF SALE', 'BUILDING CLASS AT TIME OF SALE',
                            'SALE PRICE', 'SALE DATE']
      try:
            codewars_test.assert_equals(list(pc.load_data().columns), expected_columns, "====> The URL of the dataset used is not appropriate; the columns in the dataset are different")
      except Exception as e:
            codewars_test.fail(f"====> Error loading data; There is a typo in the code: {str(e)}")
  
      expected_rows = 84548
      try:        
              codewars_test.assert_equals(len(pc.load_data()), expected_rows, "Please check the URL used again; the number of data points in the dataset is different")
      except Exception as e:
          codewars_test.fail(f"====> Error checking row count; There is a typo in the code: {str(e)}")
      print("")

  # Test data cleaning or processing (replace with your specific logic)
  @codewars_test.it('2. Test Drop Columns')
  def test_data_cleaning():
      print("========================================================================")
      try:
        
              expected_columns= 16
              codewars_test.assert_equals(len(pc.clean_columns().columns), expected_columns, "Dataframe should have expected rows")
      except Exception as e:
          codewars_test.fail(f"====> Error: {str(e)}")
      print(" ")

  @codewars_test.it('3. Test Clean Columns Name')
  def test_clean_columns_name():
      print("========================================================================")

      expected_columns = ['BOROUGH', 'NEIGHBORHOOD', 'BUILDING_CLASS_CATEGORY',
                                'BUILDING_CLASS_AT_PRESENT', 'ADDRESS', 'APARTMENT_NUMBER', 'ZIP_CODE',
                                'RESIDENTIAL_UNITS', 'COMMERCIAL_UNITS', 'TOTAL_UNITS',
                                'LAND_SQUARE_FEET', 'GROSS_SQUARE_FEET', 'YEAR_BUILT',
                                'BUILDING_CLASS_AT_TIME_OF_SALE', 'SALE_PRICE', 'SALE_DATE']
      try:

              codewars_test.assert_equals(list(pc.clean_columns_name().columns), expected_columns, "====> Column names are not as expected; Check the clean_names function again.")
      except Exception as e:
          codewars_test.fail(f"====> Error: {str(e)}")
      except AttributeError as e:
          codewars_test.fail(f"====> Error: {str(e)}")    


      print(" ")

  # @codewars_test.it("2. Test Print Clean Columns")
  # def test_total_revenue():
  #       print("========================================================================")
  #       output_lines = cmd.stdout.decode().splitlines()
  #       codewars_test.assert_equals(bool(output_lines), True, '====> Error :Tidak Menampilkan nama-nama kolom menggunakan print()')

      
       