import matplotlib.pyplot as plt
picture = plt.figure(figsize=(9.6, 5.4))
with open('/Users/andro/Downloads/DS6.txt', 'r') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
plt.scatter(y,x,color = "black")
plt.show(color = "black")
picture.savefig('/Users/andro/OneDrive/Рабочий стол/lab2_kg/lab2_kg.jpg')