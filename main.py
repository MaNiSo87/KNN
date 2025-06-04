import matplotlib.pyplot as plt

#KNN

group1 = [[1,1,2,2,3,3], [5,8,4,7,6,8]]
group2 = [[6,8,8,9,11], [7,7,8,8,7]]
group3 = [[8,9,9,10,10,11], [3,1,5,1,4,2]]
point = [[4],[5]]
k = 3

fig, ax = plt.subplots()
ax.set_title('FIGURE_001')
ax.set_ylabel('Y-axis')
ax.set_xlabel('X-axis')

Drawing_uncolored_circle = plt.Circle((point[0], point[1]), k , fill = False )
ax.add_artist( Drawing_uncolored_circle )
ax.plot(group1[0], group1[1], 'bo', label='group_1')
ax.plot(group2[0], group2[1], 'ro', label='group_2')
ax.plot(group3[0], group3[1], 'go', label='group_3')
ax.plot(point[0], point[1], 'o', color='black', label='point')
plt.legend()

blue_the_area = []
red_the_area = []
green_the_area = []
for i in range(len(group1[0])):
    if k**2 >= (point[0][0] - group1[0][i])**2 + (point[1][0] - group1[1][i])**2:
        blue_the_area.append((group1[0][i], group1[1][i]))
for i in range(len(group2[0])):
    if k**2 >= (point[0][0] - group2[0][i])**2 + (point[1][0] - group2[1][i])**2:
        red_the_area.append((group2[0][i], group2[1][i]))
for i in range(len(group3[0])):
    if k**2 >= (point[0][0] - group3[0][i])**2 + (point[1][0] - group3[1][i])**2:
        green_the_area.append((group3[0][i], group3[1][i]))

if max(len(blue_the_area), len(red_the_area), len(green_the_area)) == len(blue_the_area):
    print(f'\'Blue\' with {len(blue_the_area)} point(s) in the circle.')
elif max(len(blue_the_area), len(red_the_area), len(green_the_area)) == len(red_the_area):
    print(f'\'Red\' with {len(red_the_area)} point(s) in the circle.')
else:
    print(f'\'Green\' with {len(green_the_area)} point(s) in the circle.')

















plt.show()

