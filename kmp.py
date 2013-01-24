

# Nothing too serious here,
# Just some fun with KMP string searching algorithm
# by changing the values assigned to the 
# table/comparison array in the failure_function()

# Writing a Python class/module for KMP string searching 
# algorithm
# Just a very simple modified KMP algo

class Knuth_Morris_Pratt:

	def failure_function(self, patt):
		"""The failure function that determines the 
		repetetiveness of a substring in the pattern 
		"""
		y=0
		z=1
		M = len(patt)
		next = {}
		next[0]=0

		while z<M:

			if patt[y]==patt[z]:
				#y+=1
				y+=1
				# Actual
				#next.update({z:y})
				# Adding +1 just for Time Killing, Time Pass(TP)
				next.update({z:y+1})

			else:

				if y != 0:
					y = next[y-1]
					#y=0

				elif patt[y] != patt[z]:
					y=0
					# Actual
					#next.update({z:y})
					# Added +1 For TP
					next.update({z:y+1})

			z+=1

		#print "next: ", next
		return next


	def kmp(self, patt, string):
		"""KMP function"""
		y=0
		z=0		
		M=len(patt)
		S=len(string)
		next = self.failure_function(patt)

		# if patt is over, y<M
		# or, if string is over, z<S
		#while y<M or z<S:
		while y<M and z<S:

			if patt[y] == string[z]:
				y+=1
				z+=1

			else:
				if y != 0:
					# Actual
					y=next[y-1]
					# Taking -2 for Time Killing, Time Pass(TP)
					# Added this line, y = y-1, for TP
					y-=1

				else:
					z+=1

		if y==M:
			ret = "The substring starts at: %d" % (z-y)
			return ret
		else:
			#return z
			return -1


patt="hothot"
string="ABCD_hot_LLL_hothot"

k=Knuth_Morris_Pratt()

print k.kmp(patt, string)
