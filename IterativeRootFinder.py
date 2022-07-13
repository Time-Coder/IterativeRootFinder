class IterativeRootFinder:
	class ForwardPush:
		def __init__(self, g, x0, y0):
			self.g = g
			self.__x = {}
			self.__y = {}
			self.__x[0] = x0
			self.__y[0] = y0

		def __getitem__(self, n):
			if n in self.__x:
				return self.__x[n], self.__y[n]

			if n > 0:
				xn_1, yn_1 = self[n-1]
				self.__x[n] = yn_1
				self.__y[n] = self.g(xn_1)
			else:
				xn_1, yn_1 = self[n+1]
				self.__x[n] = self.g_inv(yn_1)
				self.__y[n] = xn_1
			return self.__x[n], self.__y[n]

		def keys(self):
			return self.__x.keys()

		def g_inv(self, x):
			y = 0.5
			lb = 0
			ub = 1
			while True:
				value = self.g(y)
				if abs(value-x) < 1E-6:
					return y

				if value < x:
					lb = y
				else:
					ub = y

				y = 0.5*(lb + ub)

	def __init__(self, g, k1 = None, k2 = None, s = None):
		x0 = 0.5
		y0 = 0.5*(g(0.5)+0.5)
		if k1 is not None:
			x0 = k1
		if k2 is not None:
			y0 = k2*g(k1)+(1-k2)*k1

		self.FP = IterativeRootFinder.ForwardPush(g, x0, y0)
		self.g = g

		if s == None:
			s = lambda t: t

		self.alpha = s

	def f(self, x):
		n = 0
		xn, yn = self.FP[n]
		x0, y0 = self.FP[0]
		x1, y1 = self.FP[1]
		if abs(xn - x) < 1E-6:
			return yn

		if min(x0, x1) < x < max(x0, x1):
			return y0 + self.alpha((x-x0)/(x1-x0))*(y1-y0)

		flag1 = (1 if y0 > x0 else -1)
		flag2 = (1 if x > max(x0, x1) else -1)
		inc = flag1*flag2
		while flag2*x > flag2*xn:
			n += inc
			xn, yn = self.FP[n]
			if abs(xn - x) < 1E-6:
				return yn

		if inc > 0:
			n -= 1

		lb = x0
		ub = x1
		t = -1
		while abs(t-x) > 1E-6 and abs(lb - ub) > 1E-6:
			mi = 0.5*(lb + ub)
			k = (mi-x0)/(x1-x0)
			FP = IterativeRootFinder.ForwardPush(self.g, mi, y0+self.alpha(k)*(y1-y0))
			xn, yn = FP[n]
			t = xn

			if flag1*t < flag1*x:
				lb = mi
			else:
				ub = mi

		return yn