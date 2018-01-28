from time import sleep, time
from threading import Thread
from random import randint

class Proposal:
	pid = 0
	pvalue = None
	
	def __init__(self, pid, pvalue):
		self.pid = pid
		self.pvalue = pvalue
		
class PreProposal:
	ppid = 0
	
	def __init__(self, proposal):
		self.ppid = proposal.pid
	
class Proposer:
	name = "Proposer 0"
	proposal = Proposal(0, None)
	accepters = []
	
	def __init__(self, nameid, proposal, accepters):
		self.name = "Proposer %d" % nameid
		self.proposal = proposal
		self.accepters = accepters
	
	def submit_proposal(self):
		# try pre-proposal
		total_accept = 0
		accepted_accepter = []
		for accepter in self.accepters:
			res = accepter.accept_pre_proposal(PreProposal(self.proposal))
			if res[0] == "Accept":
				total_accept += 1
				accepted_accepter.append(accepter)
				if res[1] is not None:
					self.proposal.pvalue = res[1]
					print(">> Pre-Accepted and updated by %s" % self.name)
				else:
					print(">> Pre-Accepted by %s" % self.name)
			elif res[0] == "Refuse":
				print(">> Pre-Refused by %s" % self.name)
			print("%s: %3d, %s\n" % (accepter.name, accepter.maxid, str(accepter.value)))
		# try proposal	
		total_lock = 0
		if total_accept > (len(self.accepters) / 2) + 1:
			for accepter in accepted_accepter:
				res = accepter.accept_proposal(self.proposal)
				if res[0] == "Locked":
					total_lock += 1
					print(">> Locked by %s" % self.name)
				elif res[0] == "Error":
					print(">> Error: %s by %s" % (res[1], self.name))
				elif res[0] == "Refuse":
					print(">> Refused by %s" % self.name)
				print("%s: %3d, %s\n" % (accepter.name, accepter.maxid, str(accepter.value)))
		# broadcast
		if total_lock > (len(self.accepters) / 2) + 1:
			for accepter in self.accepters:
				res = accepter.accept_result(self.proposal)
				if res[0] == "Accept":
					print(">> %s by %s" % (res[1], self.name))
				elif res[0] == "Error":
					print(">> Error: %s by %s" % (res[1], self.name))
				print("%s: %3d, %s\n" % (accepter.name, accepter.maxid, str(accepter.value)))
				
		
class Accepter:
	name = "Accepter 0"
	maxid = -1
	value = None
	delay = 100
	
	def __init__(self, nameid, delay = 100):
		self.name = "Accepter %d" % nameid
		self.maxid = -1
		self.value = None
		self.delay = delay
		
	def __self_delay(self):
		sleep(randint(0, self.delay) * 0.001)
		
	def accept_pre_proposal(self, pre_proposal):
		self.__self_delay()
		if pre_proposal.ppid > self.maxid:
			self.maxid = pre_proposal.ppid
			return ("Accept", self.value)
		else:
			return ("Refuse",)
			
	def accept_proposal(self, proposal):
		self.__self_delay()
		if proposal.pid >= self.maxid:
			if self.value is None:
				self.value = proposal.pvalue
				return ("Locked",)
			else:
				return ("Error", "Can not edited at accept_proposal")
		else:
			return ("Refuse",)
	
	def accept_result(self, proposal):
		self.__self_delay()
		if self.value is None:
			self.value = proposal.pvalue
			return ("Accept", "Broadcast accept")
		else:
			if self.value == proposal.pvalue:
				return ("Accept", "Broadcast already accept")
			else:
				return ("Error", "Can not edited at accept_result")
				
def demo(n):
	
	def make_proposal(proposer):
		proposer.submit_proposal()
	
	accepters = []
	for i in range(0, n):
		accepters.append(Accepter(i))
		
	proposers = []
	for i in range(0,n):
		pid = randint(0, n * 100)
		pvalue = "Content-%d" % randint(10000, 100000)
		proposers.append(Proposer(i, Proposal(pid, pvalue), accepters))
		print("Proposer %d: %3d, %s" % (i, pid, pvalue))
	print()
	
	threads = []	
	for i in range(0, n):
		proposer = proposers[i]
		threads.append(Thread(target=make_proposal, args=(proposer,)))
	start_time = time()
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()	
	end_time = time()
	print("Time: %.6fs" % (end_time - start_time))
	for accepter in accepters:
		print("%s: %3d, %s" % (accepter.name, accepter.maxid, str(accepter.value)))
				
if __name__ == "__main__":
	demo(3)			
			 
