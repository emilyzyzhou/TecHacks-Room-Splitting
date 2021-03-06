# TecHacks-Room-Splitting
This project was submitted to TechHacks 2020.

We added functionalities to this spreadsheet for part of the project: https://docs.google.com/spreadsheets/d/1ilNLQiQ6GHY5aFmHLlx2xoMX4QFgdmoPe-r2vbMwvbc/edit?usp=sharing

  We would like to submit this project to the finance track.
  
  Have you ever had to try to venmo everyone back for a complicated pandemic grocery run for your neighbors? The Rochesters, Yangs, and Kims are splitting toilet paper with you, but the Kims, Parks, and Lees are splitting hand sanitizer with you? Costco is great for buying in bulk, but that is just too much to keep track of!
  
  Our project is a cost splitting tool that can be used by groups for events and instances where multiple things are being bought for only part of the group. For this specific example, we used the event of a group of girls moving into an apartment splitting the cost of all of their new furniture and appliances. This could also be used in applications such as friends and family vacations, big nights out, and family Christmas gifts!
  
  We used the rooms the girls lived in and bathrooms they used to identify the payment groups they belonged to. Specifically for this example, we were looking at a 3 bedroom, 2 bathroom apartment where the bedrooms ranged from singles to triples. We also covered the case in which one roommate bought an item to be used in another roommate’s room or bathroom. This created the “other” category in order to make sure the buyer didn’t end up paying for a portion of the item. We used regex matching to determine if the item applies to each roommate. If you wish to add more items, the topmost row can be copied to maintain the formulas we used.
  
  Another added function was that we added charts to evaluate the final expected costs to see how much someone would expect from someone else- we grayed out the negative values since that would mean that the current person owes the other person money, instead of other way around. The chart may be a bit confusign so the graph below shows a better form of the net gain/net loss expected per person. Also, it better visualizes if a specific person is more in debt or is expecting to receive more money.


  We also created a program using Python using the Google API to access the final calculations in this spreadsheet which we organized using a custom class we created called “Roommates”. With this program, we generated a final “To-Do list” for each roommate for how much they should be paying another roommate and how much they should be expecting from each roommate. This list was also summarized at the end with how much they should be expecting to be paid or how much they will be paying in the end.
  
  As you can see in our Roommates class, we did explore the Venmo API and figured out how to utilize it to request the amounts that we generated from each roommate. The venmo passwords and usernames would be collected using the addVenmo function and we would encrypt the input when they type the password by masking the characters with asterisks. However, for this project, we decided not to test this feature because of the possible security breaches and potential financial issues. 
 
 In the future, we could add a web and/or mobile interface that utilizes a form functionality to add rows to the Receipt sheet similar to how a Google forms works. The python code could be integrated with the website to request the proper Venmo totals once the users determine that they have finished adding all the items bought to their Receipts.
