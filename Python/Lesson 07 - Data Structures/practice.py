###
### Variable ###
signals = []

with open('preclass_problem1_data.txt', 'r') as in_file:
    lines = in_file.readlines()
    for line in lines:
        #print(line)
        signal = int(line)
        signals.append(signal)
signals_sorted = sorted(signals, reverse=True)
high_5 = signals_sorted[:5]
coordinate = sum(high_5) / 10.0


 
print(f"coordinate is {coordinate}")