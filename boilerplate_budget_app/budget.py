'''
Complete the "Category" class in "budget.py".
It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment.
When objects are created, they are passed in the name of the category. The class should have an instance variable called "ledger" that is a list.
The class should also contain the following methods:

    - a "deposit" method that accepts an amount and description. If no description is given, it should default to an empty string.
      The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    - a "withdraw" method that is similar to the "deposit" method, but the amount passed in should be stored in the ledger as a negative number.
      If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
    - a "get_balance" method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    - a "transfer" method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and
      the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and
      the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers.
      This method should return True if the transfer took place, and False otherwise.
    - a "check_funds" method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and
      returns True otherwise. This method should be used by both the "withdraw" method and "transfer" method.

When the budget object is printed it should display:

    - a title line of 30 characters where the name of the category is centered in a line of "*" characters.
    - a list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed,
      then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    - a line displaying the category total.

Here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Besides the "Category" class, create a function (outside of the class) called "create_spend_chart" that takes a list of categories as an argument.
It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and
not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character.
The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar.
Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
'''


class Category:
    category_name = ""
    ledger = []

    # Object constructor
    def __init__(self, name):
        self.category_name = name
        self.ledger = []
    
    # Method that adds a deposit operation to the ledger
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # Method that adds a withdraw operation to the ledger (if there are enough funds)
    # Return True if the withdrawal took place, False otherwise
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    # This method returns the algebraic sum between deposits and withdrawals present in the ledger
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance = balance + item["amount"]
        return balance
    
    # Method that transfers funds from a category to another one
    # Return True if the transfer took place, False otherwise
    def transfer(self, amount, newCategory):
        if self.withdraw(amount, "Transfer to " + newCategory.category_name):
            newCategory.deposit(amount, "Transfer from " + self.category_name)
            return True
        else:
            return False
    
    # This method returns False if an amount exceeds the ledger balance, else returns True
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    
    # Define what to show when the object is printed
    def __str__(self):
        # Calculate number of asterisks in the title (left and right)
        category_len = len(self.category_name)
        tot_asterisks = 30 - category_len
        left_asterisks = (30 - category_len) // 2
        if tot_asterisks % 2:
            right_asterisks = left_asterisks + 1
        else:
            right_asterisks = left_asterisks
        
        # Title string
        title = ""
        for i in range(left_asterisks):
            title = title + "*"
        title = title + self.category_name
        for i in range(right_asterisks):
            title = title + "*"
        title = title + "\n"
        
        # Ledger items
        items = ""
        total = 0
        for item in self.ledger:
            # Description
            desc = item["description"][:23]
            if len(desc) < 23:
                add_spaces = 23 - len(desc)
                for i in range(add_spaces):
                    desc = desc + " "
            
            # Amount
            total = total + item["amount"]
            amnt = str("%.2f" % item["amount"])
            if len(amnt) < 7:
                add_spaces = 7 - len(amnt)
                for i in range(add_spaces):
                    amnt = " " + amnt
            
            # Final string single item
            items = items + desc + amnt + "\n"
        
        # Total string
        total = "Total: " + str("%.2f" % float(total))

        # Return final string
        return title + items + total


def create_spend_chart(categories):
    '''
    Description:
        This function takes a list of categories as an argument and return a string that is a bar chart representing the percentage spent in each category passed in.
    
    Args:
        - categories: a list of categories for which to show the bar chart
    
    Returns:
        Returns the string containing the bar chart
    '''

    # Calculate and save in a dictionary the category name and related expenses
    # For each category will be calculated the percentage spent and the rounded down percentage spent, initialized here to 0
    spent_for_categories = {}
    spent_sum = 0
    max_length_category = 0
    for category in categories:
        name = category.category_name
        if len(name) > max_length_category:
            max_length_category = len(name)
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent -= item["amount"]
        # For each category save the expense and initialize the percentage spent and the rounded down percentage spent to 0
        spent_for_categories[name] = [spent, 0, 0]
        spent_sum += spent
    
    # Initialize a list where to save rows to print
    rows = []

    # Rows 0-12 (bar charts)
    rows.append("Percentage spent by category\n") #Row 0
    rows.append("100|")    #Row 1
    rows.append(" 90|")    #Row 2
    rows.append(" 80|")    #Row 3
    rows.append(" 70|")    #Row 4
    rows.append(" 60|")    #Row 5
    rows.append(" 50|")    #Row 6
    rows.append(" 40|")    #Row 7
    rows.append(" 30|")    #Row 8
    rows.append(" 20|")    #Row 9
    rows.append(" 10|")    #Row 10
    rows.append("  0|")    #Row 11
    rows.append("    ")    #Row 12
    
    # Rows 13+ (category names)
    for i in range(max_length_category):
        # Initialize row
        rows.append("    ")
        # For each category, take i-th letter of category name (if exists)
        for k in spent_for_categories.keys():
            try:
                rows[13+i] = rows[13+i] + " " + k[i] + " "
            except:
                rows[13+i] = rows[13+i] + "   "
    
    # Calculate the percentage spent for each category and create the bar charts
    for k,v in spent_for_categories.items():
        rows[12] = rows[12] + "---"
        # Calculate percentage spent
        v[1] = v[0]/spent_sum
        # Round down the percentage spent to calculate the number of "o" that make up the bar in the chart
        v[2] = int(v[1]*10) + 1
        # Create the bar chart inserting the "o" char in the correct rows
        for i in range(1, 12):
            if v[2] > 11-i:
                rows[i] = rows[i] + " o "
            else:
                rows[i] = rows[i] + "   "
    
    # Finalize all the rows handling particular cases and build the final string
    retstring = rows[0]
    for r in range(1, len(rows)):
        # Append a blank space to the last rows
        if r == len(rows)-1:
            rows[r] = rows[r] + " "
        # Append a "-" char to the row 12 and start a new line
        elif r == 12:
            rows[r] = rows[r] + "-" + "\n"
        # In all other rows append a blank space and start a new line
        else:
            rows[r] = rows[r] + " " + "\n"
        # Build the final string
        retstring = retstring + rows[r]
    
    # Return final string
    return retstring
