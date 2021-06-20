class SavingsAccount:
  annual_interest_rate = 5
  
  
def MonthlyInterest(balance):
  monthlyInterest= balance * SavingsAccount.annual_interest_rate /1200
  return monthlyInterest+balance
  
  
saver1 = SavingsAccount()
saver1.saving_balance = 2000

saver2 = SavingsAccount()
saver2.saving_balance = 3000

s1= MonthlyInterest(saver1.saving_balance)
print(s1)

s2= MonthlyInterest(saver2.saving_balance)
print(s2)

SavingsAccount.annual_interest_rate= 7

s1_= MonthlyInterest(s1)
print("After change of annual interest the next month to pay is ",s1_)

s2_= MonthlyInterest(s2)
print("After change of annual interest the next month to pay is ",s2_)

