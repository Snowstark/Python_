name = [];
name.append("式子墨");
print(name[0]);
print("Nice to meet you, " + name[0]);
transports = ["Bike","Car","Walk"];
print("I would like to " + transports[0]);

Guest = ["snow","stark","blue"];
print(Guest[1] + " can't be present.");
del Guest[1];
Guest.insert(1,"john");
for guest in Guest:
    print("Looking forward to your presence, " + guest.title());

Guest.insert(0,"Jerry");
Guest.insert(len(guest)//2,"Tom");
Guest.append("girl");

for guest in Guest:
    print("Welcome! "+ guest.title());

print("Quite sorry for that party is postponed.");
for guest in range(0,len(Guest) - 2):
    pop_man = Guest.pop;
    print(pop_man() + " ,sorry to tell you...");

for guest in Guest:
    print(guest.title() +" ,you're still in list.")

del Guest[0];
del Guest[0];

print(Guest);