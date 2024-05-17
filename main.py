import random, time, os
Attack = ["got spanked","got drowned","got slapped","got shot","got stabbed","got slammed against a table","faced emotional damage","got 360 no-scoped","slipped and fell"]
def rollDamage(Won,Dge):
	Num = random.randrange(9)
	if Won == 1:
		print(Name2,"wins this round.")
		print(Name1,Attack[Num],"and took",Dge,"damage.\n")
	if Won == 2:
		print(Name1,"wins this round.")
		print(Name2,Attack[Num],"and took",Dge,"damage.\n")
	return Dge
def rollStats(No1,No2):
	return round(((random.randint(1,6))*(random.randint(1,No1))) / 2 + No2)
	
rdNo = 0
print("Charecter Builder\n")
time.sleep(1)
Name1 = input("Name your charecter: ")
ChTy1 = input("Charecter type (Human, Elf, Wizard, Ork, ect:): ")
os.system("clear")
time.sleep(0.5)
print(Name1)
Hp1 = rollStats(12,10)
Sp1 = rollStats(8,12)
time.sleep(0.5)
print("Type:",ChTy1)
time.sleep(0.5)
print("Health:",Hp1)
time.sleep(0.5)
print("Strength:",Sp1)
time.sleep(0.5)
print("\nMay your name go down in Legend...")
time.sleep(2)
os.system("clear")
print("Who are they battling? ")
time.sleep(0.5)
print()
Name2 = input("Name your charecter: ")
ChTy2 = input("Charecter type (Human, Elf, Wizard, Ork, ect:): ")
os.system("clear")
time.sleep(0.5)
print(Name2)
Hp2 = rollStats(12,10)
Sp2 = rollStats(8,12)
time.sleep(0.5)
print("Type:",ChTy2)
time.sleep(0.5)
print("Health:",Hp2)
time.sleep(0.5)
print("Strength:",Sp2)
time.sleep(0.5)
print()
print("May your name go down in Legend...")
time.sleep(2)
while True:
	os.system("clear")
	print("\033[?25lLet the Battle Begin!\n")
	rdNo += 1
	time.sleep(0.5)
	print("Round",rdNo,"\n")
	p1 = random.randint(1,6)
	p2 = random.randint(1,6)
	if p1 > p2:
		Hp1 -= rollDamage(1,(p1 - p2))
	elif p1 < p2:
		Hp2 -= rollDamage(2,(p2 - p1))
	else:
		rdNo -= 1
		continue
	if Hp1 <= 0:
		os.system("clear")
		print(Name2,"has won in",rdNo,"rounds.")
		break
	elif Hp2 <= 0:
		os.system("clear")
		print(Name1,"has won in",rdNo,"rounds.")
		break
	else:
		time.sleep(2)
		print(Name1)
		time.sleep(0.5)
		print("Type:",ChTy1)
		time.sleep(0.5)
		print("Health:",Hp1)
		time.sleep(0.5)
		print("Strength:",Sp1)
		time.sleep(0.5)
		print("\n")
		print(Name2)
		time.sleep(0.5)
		print("Type:",ChTy2)
		time.sleep(0.5)
		print("Health:",Hp2)
		time.sleep(0.5)
		print("Strength:",Sp2)
		time.sleep(2)
		os.system("clear")
