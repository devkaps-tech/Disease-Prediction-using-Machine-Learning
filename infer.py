import pickle
import pandas as pd
import numpy as np
from joblib import load


if __name__ == '__main__':
  symptoms = {'Itching' : 0 , 'Muscle_weakness':0 , 'Scurring' : 0 , 
               'Stomach_bleeding':1 , 'Slurred_speech':0 , 
               'Knee_pain': 0 , 'Loss_of_balance':0 ,
               'Depression':1 , 'Obesity':1 , 'Foul_smell_of urine':0}
  
  df_test = pd.DataFrame(columns=list(symptoms.keys()))
  df_test.loc[0] = np.array(list(symptoms.values()))
  clf = pickle.load(open('model.pkl', 'rb'))
  result = clf.predict(df_test)
  print(f"Predicted Disease: {result}")