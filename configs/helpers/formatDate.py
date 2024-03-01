from datetime import datetime
import pandas as pd

def formatDate(date_value):
    if pd.isnull(date_value) or date_value == 'NaT':
      return None
    return date_value