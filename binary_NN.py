from matplotlib import pyplot as plt
import numpy as np

data = [[3, 1.5, 1],
        [2, 1, 0],
        [4, 1.5, 1],
        [3, 1, 0],
        [3.5, .5, 1],
        [2, .5, 0],
        [5.5, 1, 1],
        [1, 1, 0]]

mystery_flower = [4.5, 1]

w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))

# scatter data
plt.axis([0, 6, 0, 6])
plt.grid()
for i in range(len(data)):
    point = data[i]
    color = 'r'
    if point[2] == 0:
        color = 'b'
    plt.scatter(point[0], point[1], c = color)


#Training Loop

learning_rate = 0.2
costs = []

for i in range(5000):
    ri = np.random.randint(len(data))
    point = data[ri]
    
    z = point[0] * w1 + point[1] * w2 + b
    pred = sigmoid(z)

    target = point[2]
    cost = np.square(pred - target)

    costs.append(cost)

    dcost_pred = 2 * (pred - target)
    dPred_z = sigmoid_p(z)
    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_db = 1

    dcost_dz = dcost_pred * dPred_z

    dcost_dw1 = dcost_dz * dz_dw1
    dcost_dw2 = dcost_dz * dz_dw2
    dcost_db = dcost_dz * dz_db

    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    b = b - learning_rate * dcost_db

    plt.plot(costs)

file = open("data.txt", "w")
file.write("w1 = " + str(w1) + "\n w2 = " + str(w2) + "\n bias = " + str(b))
file.close()



from win32com.client import Dispatch
from data import w1, w2, bias

speak = Dispatch("SAPI.SpVoice").Speak

def which_flower(length, width):
    z = length * w1 + width * w2 + bias
    pred = sigmoid(z)
    if pred < .5:
        speak("Blue")
    else:
        speak("Red")

which_flower(3, 1.5)