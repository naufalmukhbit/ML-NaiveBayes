# Menggunakan pandas dan xlrd untuk import dan export file *.xlsx
import pandas as pd

train_data = pd.read_excel(r'TrainsetTugas1ML.xlsx')
test_data = pd.read_excel(r'TestsetTugas1ML.xlsx')
train_row = train_data.shape[0]

def calculateAmount(column_name, category):
    # Untuk menghitung jumlah kelas dalam suatu kategori
    amount = 0
    for i in range(train_row):
        if (train_data[column_name][i] == category):
            amount += 1
    return amount

def calculateAifB(column_A, A, column_B, B):
    # Untuk menghitung jumlah kelas A dalam kategori A dengan syarat B terjadi di kategori B
    amount = 0
    for i in range(train_row):
        if (train_data[column_A][i] == A) & (train_data[column_B][i] == B):
            amount += 1
    return amount

income = [] # Untuk menyimpan kelas-kelas di kategori output
for i in range(train_data.shape[0]):
    if train_data['income'][i] not in income:
        income.append(train_data['income'][i])
incomeProb = [] # Untuk menyimpan probabilitas tiap kelas output
for x in range(len(income)):
    incomeProb.append(calculateAmount('income', income[x]) / train_row)

outputData = []
for i in range(test_data.shape[0]):
    prob = []
    for j in range(len(income)):
        columns = ['age', 'workclass', 'education', 'marital-status', 'occupation', 'relationship', 'hours-per-week']
        probs = []
        for k in range(len(columns)):
            probs.append(calculateAifB(columns[k], test_data[columns[k]][i], 'income', income[j]) / calculateAmount('income', income[j]))
        prob.append(probs[0]*probs[1]*probs[2]*probs[3]*probs[4]*probs[5]*probs[6]*incomeProb[j])
    output = max(prob)
    outputPosition = [i for i, j in enumerate(prob) if j == output]
    outputData.append(income[outputPosition[0]])
TebakanTugas1 = pd.DataFrame({'income': outputData}, index=test_data['id'])
TebakanTugas1.to_excel("TebakanTugas1ML.xlsx")
print("The program has finished! Check the file 'TebakanTugas1ML.xlsx' to see the result.")