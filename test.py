import pandas as pd
import numpy as np
data = pd.read_csv("D:\\crime_data.csv")
f = open("D:\\input.txt", "r")
place = f.read()
f.close()
murder_in_selected_location = data.loc[data['District'] == place, 'Murder'].sum()

custodial_rape_in_selected_location =  data.loc[data['District'] == place, 'Custodial Rape'].sum()
rape_in_selected_location =   data.loc[data['District'] == place, 'Rape_Others'].sum()
rape_total = custodial_rape_in_selected_location + rape_in_selected_location
acid_attack_in_selected_location = data.loc[data['District'] == place, 'Acid attack'].sum()

dowry_death_in_selected_location = data.loc[data['District'] == place, 'Dowry Deaths'].sum()


rash_driving =  data.loc[data['District'] == place, 'Incidence of Rash Driving'].sum()


kidnapping = data.loc[data['District'] == place, 'Kidnapping for Ransom'].sum()

crimes_in_front_of_public =  data.loc[data['District'] == place, 'In Public Transport system'].sum()


Sexual_Harassment = data.loc[data['District'] == place, 'Sexual Harassment'].sum()


Theft_cases = data.loc[data['District'] == place, 'Theft'].sum()

fake_currency_cheating =  data.loc[data['District'] == place, 'Counterfeit currency & Bank notes'].sum()

other_ipc_crimes = data.loc[data['District'] == place, 'Other IPC crimes'].sum()


total_crimes = murder_in_selected_location + custodial_rape_in_selected_location + rape_total  + acid_attack_in_selected_location + dowry_death_in_selected_location + rash_driving + kidnapping + crimes_in_front_of_public + Sexual_Harassment + Theft_cases  + fake_currency_cheating + other_ipc_crimes
print(" Total no. crime in a month:")
print(total_crimes)
average = total_crimes/10
print("Average no. of crime in a month")

print(average)
print("\n")
if(average>300):
    print("The place is not safe to visit")
elif(average>200 and average<300):
    print("The place is safer to visit, but you must be careful")
else:
    print("The plce is safe to visit")
  
