Hey Ian.

I'm using this readme to basically record all my notes and ideas for the files im manipulating. 

Follow along as you wish. 

November 7th, 2019 (6:17PM)
1) Untouched, the amazon file. I need to make some arrangements. 
	There are any columns included in the Amazon file and there are some that are irrelavant to analysis. 
	- When i created a report ofr my boss before, we only kept a few columns, not everything, _
		my boss only wanted some relevant columns for his business, and there were some columns we 
		excluded but im not sure if he excluded them because it just wasn't relevant at the time 
		for his purpose. I just made the report and listened to instructions.
		For example, for his report we kept:
		- date/time, sku, description, product sales_
			selling fees, fba fees.
		We also added a column called landing costs which we gathered
		from the companies Quick Books. We actually don't have it_
		in the repo at this time, so i'll be adding it tomorrow (friday)_
		when i get to work.
2) Other than the columns, I'm going to remove some columns beause they aren't very_
	useful to have, such as...
	- settlement id, order id, marketplace, fulfillment, and total.
	I may delete some more columns after work tomorrow once i fully understand_
		what the other columns are which my boss wanted to exclude from_
		his report.
3) In the sku column, all SKUs are fine but there's a descripency with some SKU's.
	A sku which goes by "3M-..." is suppose to actually be "3MM-...".
	In this case, i'm going to be adding an extra 'M' to every sku such that_
		it has "3M-...".
4) I am going to be seperating the date/time column so we can have date and time in seperate
	columns to analyze sales during the day and year.
	Im going to do this change on excel because python's being weird.
5) My next move is to seperate dataframes by order 'types', delete some irrelevant columns, 
	and adding the landing costs for each sku and setting them appropriate with respect 
	to the quantity purchased per order.

				