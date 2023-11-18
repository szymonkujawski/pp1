article_number = str(input("Enter EAN-13 article number: "))

if len(article_number)==13:
    print("Article number is correct")
    if article_number[:3]=="590":
        print("Article manufactured in Poland")
    else:
        print("Article wasn't manufactured in Poland")
else:
    print("Article number is NOT correct")