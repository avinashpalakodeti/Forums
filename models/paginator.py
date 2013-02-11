class Paginator(object):	
	def __init__(self,items,items_per_page,page_no):
		self.items = items
		self.items_per_page = items_per_page
		self.page_no = page_no
		#deal with the different data type		

		try:  			
			if not isinstance(self.items,list):
				raise TypeError	
		except TypeError:
			print "please pass list"
			raise SystemExit	
		self.item_count = len(self.items)

	def total_pages(self):
		if self.item_count == 0:
			return 0
		elif self.item_count > 1 and self.item_count < self.items_per_page:
			return 1
		elif self.item_count > self.items_per_page:
			pages = self.item_count%self.items_per_page
			page_count = self.item_count/self.items_per_page
			if pages == 0:
				return page_count
			else:
				return page_count+1

	""" returns first index"""	
	def first_item(self):
		if self.page_no > 0:

			total_pages =  self.total_pages()
			if self.page_no > total_pages:
				self.page_no = total_pages

			if self.page_no == 1:
				return 1
			else:
				p = (self.items_per_page * self.page_no) - self.items_per_page
				return p+1
		else:
			return 0

	""" returns last index """
	def last_item(self):
		 if self.page_no == 1:
			 return self.items_per_page
		 elif self.page_no > 1:
			 total_pages = self.total_pages()
			 if self.page_no < total_pages:
				 return self.items_per_page * self.page_no
			 elif self.page_no == total_pages or self.page_no > total_pages:
				 total = total_pages * self.items_per_page
				 if self.item_count < total:
					 return total-(total-self.item_count)
				 else:
					 return self.item_count

	""" returns whether next page exists or not """
	def is_next_page(self):
		return self.page_no < page.total_pages()

	""" returns whether previous page exists or not """
	def is_previous_page(self):
		return self.page_no not in [0,1]

	"""returns items"""	
	def page_items(self):
		if self.items_per_page == 0 or self.page_no == 0:
			return []		
		elif self.page_no == 1:
			return self.items[:self.items_per_page]
		elif self.page_no > 1:
			return self.items[self.first_item()-1:self.last_item()]
