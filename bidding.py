# from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidding={}
def add_bid(name,amount):
    bidding[name]=amount
    return bidding
check=True
while check==True:
    n = input("Enter Your Name: ")
    amt = int(input("Enter The Amount: "))
    add_bid(name=n,amount=amt)
    o_bid = input("Is There Any Bidder:")
    #clear()
    if o_bid == 'no':
        check = False
        max_amount=max(bidding.values())
        winner=[key for key, value in bidding.items() if value == max_amount]
        print(f"\n\n{winner[0]} Won The Bid With A Maximum Amount Of {max_amount}")