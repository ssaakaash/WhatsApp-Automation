from tabulate import tabulate
from auto import numberOfMembers

#Insert your group names here
groups = ["PRP107", "VVIP LOUNGE"]

head = ["Group Name", "Number of Participants"]
members = numberOfMembers(groups)

data = []
for i in range(len(groups)):
    data.append([groups[i], members[i]])

print(tabulate(data, headers=head, tablefmt="github"))
