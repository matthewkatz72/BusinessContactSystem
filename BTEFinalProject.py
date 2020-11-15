import mysql.connector
cnx = mysql.connector.connect(user='matt', password='Minimans1!',
                              host='35.185.26.116',
                              database='finalproject')
cursor = cnx.cursor()

def displayMenu():
    print("\n\n**************")
    print("Welcome to the Business Contact Interaction Tracking System\n")
    print("Please select an option below by typing its number: ")
    print("**************")
    print("1-Find all particular interactions associated with a specific name")
    print("2-List all the interaction events made during a particular time period")
    print("3-List the information for all contacts available in a particular company")
    print("4-List the total number of phone interactions made during a particular time period")
    print("5-List the name of the manager of a specific contact")
    print("6-List all contacts with greater than 1 interaction events.")
    print("8-Back to location Selection")
    #print(">> ",end="")
#14
def getChoice():
    choice = eval(input(">>"))
    return choice
def main():
    displayMenu()
    choice = getChoice()
    while(choice!=9):
        if (choice == 1):
            print("====================================")
            print("Please type the name of the person who's interactions you are looking for.\nMake sure the name is spelled correctly")
            print("====================================")
            name = input("Name: ")
            print ("Name, Date, Interaction Type, Comments")
            result=cursor.execute("""SELECT c.name, i.date, i.interactionType, i.comment FROM Interaction i
JOIN ContactInfo c ON i.contactID = c.contactID WHERE c.name = (%s)""",(name,))
            for (hotelName) in cursor:
                print(hotelName)
            main()
            break
        elif (choice==2):
            print("====================================")
            print("Please type the date you are looking from and the date you are looking to in the following format: YYYY-MM-DD")
            print("====================================")
            date1 = input("Date From: ")
            date2 = input("Date To: ")
            print("InteractionID, contactId, InteractionType, date, comments")
            cursor.execute("""SELECT * from Interaction WHERE date >= (%s) AND date <= (%s)""",(date1,date2,))
            for (location) in cursor:
                print(location)
            main()
            break
        elif (choice==3):
            print("====================================")
            print("Please type the name of a company, for example 'Google'")
            print("====================================")
            name = input("Company Name: ")
            print("InteractionID, contactId, InteractionType, date, comments")
            cursor.execute("""SELECT c.name, i.date, i.interactionType, i.comment FROM Interaction i
JOIN ContactInfo c ON i.contactID = c.contactID WHERE employerName = (%s)""",(name,))
            for (process) in cursor:
                print(process)
            main()
        elif (choice==4):
            print("====================================")
            print("Please type the date you are looking from and the date you are looking to in the following format: YYYY-MM-DD")
            print("====================================")
            date1 = input("Date From: ")
            date2 = input("Date To: ")
            print("Total Number of phone calls from", date1, "to", date2)
            cursor.execute("SELECT COUNT(interactionID) FROM Interaction WHERE interactionType = 'phone'")
            for (process) in cursor:
                print(process)
            main()
        elif (choice == 5):
            print("====================================")
            print("Please type the name of the person who's superior you are looking for.\nMake sure the name is spelled correctly")
            print("====================================")
            name = input("Name: ")
            print ("Name, Superior")
            result=cursor.execute("""SELECT Name, mangerName FROM ContactInfo WHERE name = (%s)""",(name,))
            for (hotelName) in cursor:
                print(hotelName)
            main()
            break
        elif (choice == 6):
            print("====================================")
            print("Listing all contacts with greater than 1 interaction events...")
            print("====================================")
            print("Number of Interactions, Contact Name")
            result=cursor.execute("""
SELECT COUNT(interactionID) as count, name FROM Interaction i, ContactInfo c 
WHERE i.contactID = c.contactID GROUP BY i.contactID
HAVING count > 1""")
            for (hotelName) in cursor:
                print(hotelName)
            main()
            break
        elif (choice==8):
            break
            
if __name__ == "__main__":
    main()
