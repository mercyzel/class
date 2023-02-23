results = {"brock": "80", "nuna": "93", "bryan": "99", "ugo": "89", "nicole": "85"}
results.update({"sam": "78", "marie": "92", "ria": "88"})
print(results)

results_values = list(map(int, (results.values())))
print(results_values)

sum=0
for i in results_values:
    sum+=i
    
results_avgs=(sum/len(results))
print(results_avgs)

above_avg=0
for i in results_values:
    if i >85:
        above_avg+=1
print(above_avg)

top_mark=max(results_values)
top_student=max(results, key=lambda k:results[k])
print(top_student,top_mark)
