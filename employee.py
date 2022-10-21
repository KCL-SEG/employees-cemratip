class Employee:
  def __init__(self, name, **kwargs):
    self.name = name
    self.contract = kwargs.get('contract')
    self.pay = kwargs.get('pay')
    self.hours = kwargs.get('hours')
    self.contracts = kwargs.get('contracts')
    self.commission = kwargs.get('commission')
    self.bonus = kwargs.get('bonus')
    if (self.hours == None):
      self.hours = 0
    if (self.contracts == None):
      self.contracts = 0
    if (self.commission == None):
      self.commission = 0
    if (self.bonus == None):
      self.bonus = 0

  def get_pay(self):
    if (self.contract == 'monthly'):
      return self.pay + self.bonus + (self.contracts * self.commission)
    elif (self.contract == 'hourly'):
      return self.bonus + (self.hours * self.pay) + (self.contracts * self.commission)

  def __str__(self):
    if self.contract == 'monthly':
      contractFill = f'monthly salary of {self.pay}'
    else:
      contractFill = f'contract of {self.hours} hours at {self.pay}/hour'
    if self.commission != 0:
      commissionFill = f' and receives a commission for {self.contracts} contract(s) at {self.commission}/contract'
    else:
      commissionFill = ''
    if self.bonus != 0:
      bonusFill = f' and receives a bonus commission of {self.bonus}'
    else:
      bonusFill = ''
    return f"{self.name} works on a {contractFill}{commissionFill}{bonusFill}. Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', contract='monthly', pay=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract='hourly', hours=100, pay=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', contract='monthly', pay=3000, contracts=4, commission=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contract='hourly', hours=150, pay=25, contracts=3, commission=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', contract='monthly', pay=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract='hourly', hours=120, pay=30, bonus=600)
