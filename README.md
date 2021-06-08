# RF-COVID-19-SE-USA
Project that uses Random Forest Regression to forecast the number of COVID-19 infections and deaths in the Southeastern United States 

### SouthEast Counties:
#### SouthEast_Counties.csv: dataset that contains states and counties names (used for reference)
#### SE_Counties.csv: dataset used for Tests 1 and 2

#### Cases
##### •	SE_Cases.py: Program for Test 1 Case 1 (predicts number of cases)
##### •	results_cases.csv: Test 1 Case 1 results
#### Cases (Deaths Removed)
##### •	SE_Cases_Deaths_Removed.py: Program for Test 1 Case 2 (predicts number of cases)
##### •	results_cases_deaths_removed.csv: Test 1 Case 2 results
#### Cases (Area and Population Density Removed)
##### •	SE_Cases_A&PD_Removed.py: Program for Test 1 Case 3 (predicts number of cases)
##### •	results_cases_a&pd_removed.csv: Test 1 Case 3 results
#### Cases (Population Density Removed)
##### •	SE_Cases_PD_Removed.py: Program to predict number of cases without using population density (not in report)
##### •	results_cases_pd_removed.csv: results for above program
#### Cases (Area Removed)
##### •	SE_Cases_Area_Removed.py: Program to predict number of cases without using area (not in report)
##### •	results_cases_area_removed.csv: results for above program
#### Cases (Area and Population Removed)
##### •	SE_Cases_A&P_Removed.py: Program to predict number of cases without using area or population (not in report)
##### •	results_cases_a&P_removed.csv: results for above program
#### Deaths
##### •	SE_Deaths.py: Program for Test 2 Case 1 (predicts number of deaths)
##### •	results_deaths.csv: Test 2 Case 1 results
##### •	results_deaths_accuracy.csv: Test 2 Case 1 results with calculated accuracies
#### Deaths (Cases Removed)
##### •	SE_Deaths_Cases_Removes.py: Program for Test 2 Case 2 (predicts number of deaths)
##### •	results_deaths_cases_removed.csv: Test 2 Case 2 results
##### •	results_deaths_cases_removed_accuracy.csv: Test 2 Case 2 results with calculated accuracies
#### Deaths (Area and Population Density Removed)
##### •	SE_Deaths_A&PD_Removes.py: Program for Test 2 Case 3 (predicts number of deaths)
##### •	results_a&pd_cases_removed.csv: Test 2 Case 3 results
##### •	results_a&pd_cases_removed_accuracy.csv: Test 2 Case 3 results with calculated accuracies

### SouthEast States:
#### SE_States.csv: dataset used for Tests 3 and 4
#### Total Cases
##### •	States_Cases.py: Program for Test 3 Case 1 (predicts number of total cases)
##### •	results_tot_cases.csv: Test 3 Case 1 results
#### Total Cases (Total Deaths Removed)
##### •	States_Cases_TD_Removed.py: Program for Test 3 Case 2 (predicts number of total cases)
##### •	results_tot_cases_td_removed.csv: Test 3 Case 2 results
#### Total Cases (Optimized)
##### •	States_Cases_Optimized.py: Program for Test 3 Case 3 (predicts number of total cases)
##### •	results_tot_cases_optimized.csv: Test 3 Case 3 results
#### Total Death
##### •	States_Death.py: Program for Test 4 Case 1 (predicts number of total deaths)
##### •	results_tot_death.csv: Test 4 Case 1 results
##### •	results_tot_death_accuracy.csv: Test 4 Case 1 results with calculated accuracies
#### Total Death (Total Cases Removed)
##### •	States_Death_TC_Removed.py: Program for Test 4 Case 2 (predicts number of total deaths)
##### •	results_tot_death_tc_removed.csv: Test 4 Case 2 results
##### •	results_tot_death_tc_removed_accuracy.csv: Test 4 Case 2 results with calculated accuracies
#### Total Death (Optimized)
##### •	States_Death_Optimized.py: Program for Test 4 Case 3 (predicts number of total cases)
##### •	results_tot_death_optimized.csv: Test 4 Case 3 results
##### •	results_tot_death_optimzed_accuracy.csv: Test 4 Case 3 results with calculated accuracies
#### New Cases
##### •	States_New_Cases.csv: Program to predict the baseline number of new cases (not in report)
##### •	results_new_cases.csv: Results for above program
##### •	results_new_cases_accuracy.csv: Results for above program with calculated accuracies
#### New Cases (Optimized)
##### •	States_New_Cases_Optimized.csv: Program to predict the attempted optimization of number of new cases (not in report)
##### •	results_new_cases_optimized.csv: Results for above program
##### •	results_new_cases_optimized_accuracy.csv: Results for above program with calculated accuracies
