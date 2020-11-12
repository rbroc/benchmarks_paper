import pandas as pd
from pathlib import Path
import re
import numpy as np

DATA_PATH = Path('manylabs1_data')
df = pd.read_spss(str(DATA_PATH / 'raw_data.sav'))
del_cols = [0,1,2,3,4,5,6,7,8,9,12,13] + list(set([*range(176, len(df.columns))]) - set([357, 355, 356]))
df = df.drop(df.columns[del_cols], axis=1)
df = df.replace(to_replace=r'^\.$', 
                value='', regex=True)
df = df.drop(['user_id', 'session_status', 'previous_session_id', 
              'previous_session_schema', 'user_agent', 'task_status', 
              'task_sequence', 'session_created_by', 
              'study_url', 'study_name'],
             axis=1)
df.to_csv(str(DATA_PATH / 'preprocessed_data.txt'), '\t', index=False)