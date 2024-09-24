input_data = open('input.txt', 'r') 
data = input_data.read()
K = int(data)
out = K * 100 + 90 + (9-K)
output_data = open('output.txt', 'w')
output_data.write(str(out))
input_data.close()
output_data.close()









