# break:-

print("break:-");
for i in range(1,6):
    if i==3: 
        break
    else:
        print(i);

# continue:-

print("continue:-");
for i in range(1,6):
    if i==3: 
        continue
    else:
        print(i);

# pass:-
print("pass:-");
for i in range(1,6):
    if i==3:
        pass
    else:
        print(i)

# for loop with else:-
print("for loop with else:-");
for i in range(1,6):
    print(i);
else:
    print("[In else block of for loop.]");

# while loop with else:-
print("while loop with 'else':-");
i=1;
while i<=5:
    print(i);
    i+=1;
else:
        print("[In else block of while loop.]");