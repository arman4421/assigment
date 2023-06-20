ls=[];
i=1;
print("Enter numbers:-");
while i<=5:
    n=int(input())
    ls.append(n)
    i+=1; 
print(ls);
print(sum(ls));
print(min(ls));
print(max(ls));
ls.sort();
print(ls);
ls.sort(reverse=True);
print(ls);
print(tuple(ls));
del ls;