import pandas as pd 


path = 'F:/PythonForDS/ProjectPython/JeuxOlympiques/datasets/'
athletes = pd.read_csv(path+'athlete_events.csv') 
regions = pd.read_csv(path+'noc_regions.csv')

display(athletes)