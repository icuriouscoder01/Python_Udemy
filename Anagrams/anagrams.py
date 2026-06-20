S1 = str(input("Enter the Phrase 1: "))
S2 = str(input("Enter the Phrase 2: "))

S1 = S1.lower()
S2 = S2.lower()

for x in S1:
    if x.isalpha():
        if S1.count(x) != S2.count(x):
            print("Not anograms")
            break
    else:
        print("Anagrams")