def add_or_sub(number, finaltotal):
	if number >= 0:
		return number - finaltotal
	else: 
		return number + finaltotal

class Player(object):
	def __init__(self, name):
		self.name = name
		self.round = [name]
	def newround(self, rnumb):
		self.round.append(Round(rnumb))

class Round(object):
	def __init__(self, rnumb):
		self.rnumb = rnumb
		self.trades = []
		self.profit = 1337
	def addtrade(self, amount):
		self.trades.append(int(amount))
	def findprofit(self, finaltotal):
		self.profit = sum(map(lambda x: add_or_sub(x, finaltotal), self.trades))
		return self.profit

def nextround():
	global currentround 
	currentround += 1
	for p in players:
		allscores[p].newround(currentround)
	print "Round %i" % currentround

def buysell(buyer, seller, price):
	allscores[buyer].round[currentround].addtrade(int(price)*-1)
	allscores[seller].round[currentround].addtrade(int(price))

def isitint(str2check):
    try: 
        int(str2check)
        return True
    except ValueError:
        return False

players = ['kent','will','kiran']
allscores = {}
currentround = 0

for p in players:
	allscores[p] = Player(p)

if raw_input('start new round? (yes): ') == 'yes':
	nextround()
	print 'Enter trades or "no" to round'
	print 'Format: buyer seller price'
	intrade = raw_input('> ')
	buyer = intrade.split()[0]
	seller = intrade.split()[1]
	c1 = intrade != 'no' 
	c2 = len(intrade.split()) == 3
	c3 = buyer in allscores
	c4 = seller in allscores
	c5 = isitint(intrade.split()[2])
	if c1 & c2 & c3 & c4 & c5:
		buysell(buyer, seller, int(intrade.split()[2]))
	else:
		print "something wrong with your input, try again"




