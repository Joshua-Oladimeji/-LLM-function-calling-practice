#1. create_order(customer: {name: string, email: string},
#  items : [{product:string, quantity: number}],
#  total_price : number)

json_file_1 = {
    "name" : "create_order",
    "arguments": {"customer" : {"name": "Jotron",
                                 "email" : "jotron@gmail.com"},
                    "items" : [{"product" :"Laptop", "quantity" : 1},
                                {"product" : "Mouse", "quantity" : 2}], 
                                "total_price" : 1500}
}

#2. register_event(title: string, date: string, location:string, description? : string)
#title: AI Conference
#  date: 2026-06-10 
# location: Lagos
json_file2 = {
    'name': "register_event", 
    "arguments" : {"title" : "AI Conference", 
                   "date" : "2026-06-10",
                   "location" : "Lagos"}
                     
              }

#3. process_payment(amount: number, currency: string, completed: bolean)
#amount : 2500 
# currency : NGN 
# completed : yes
json_file_3 = { 
    "name" : "process_payment",
    "arguments" : {"amount" : 2500, 
                   "currency" : "NGN",
                   "completed" : true}                   
}

#4. create_user(name: string, age: number) 
# name: Ada 
# age: 25 
# email: ada@gmail.com
json_file_4 = {
    "name": "create_user",
    "arguments" : {"name" : "Ada",
                   "age" : 25,
                   "email": "ada@gmail.com"} #wrong - no extra field allowed in json
}

#5. log_transactions(transaction: [{id :number, amount: number, type: string}])
#Transcation1: id=1, amount = 500, type="credit"
#Transaction2 : id=2, amount= 200, type="debit"
json_file_5 = {
    "name" : "log_transactions",
    "arguments" : {"transactions" : [{"id" : 1, "amount" : 500, "type" : "credit"},
                                    {"id" : 2, "amount" : 200, "type" : "debit"}]}
}

#6. write an email to a client confirming their payment of N5000 has been received.
#DECISION ---> NATURAL
# subject: PAYMENT CONFIRMATION
#Dear Client, 
#Thank you for using our platform. Sequel to the payment iniated by you few hours ago through our payment system, 
# we are please to confirm that your payment of #5000 has been recieved. 

#Kind Regards
#Customer service

#7. extract_user_info(name : string, age:number)
#my name is David and i a 29 years old
json_file_6 = {
    "name" : "extract_user_info",
    "arguments" : {"name" : "David",
                   "age" : 29}

}

#8. store the following user and then send them a welcome email.
#user:
#name: Zara
#age: 23
#email: zara@gmail.com
json_file_6 = {{
    "name" : "create_user",
    "arguments" : {"name": "Zara",
                    "age" : 23,
                      "email": "zara@gmail.com"}}, 
    {
        "name": "send_email",
        "arguments": {"to" : "zara@gmail.com", 
                      "subject" : "welcome",
                      "body" : "Dear Zara"} #CHAINING IS NOT SUPPORTED UNLESS EXPLICITLY SPECIFIED
    }}

#9. update_user(name: string, age?: number, eamil?: string)
#name : David
#ONLY email : david@gmail.com
json_file_7 = {
    "name" : "update_user",
    "arguments" : {"name" : "David"}
}

#10. submit_score(student: string, score: number, passed: boolean)
#student: Ada
#score: 85
#passed : true
json_file_8 = {
    "name" : "submit_score",
    "arguments" : {"student" : "Ada", "score" : 85, "passed" : true}

}

#11. create_invoice(customer: string, items[{name: string,  price : number}], total:number)
#items: Book - 500
#pen - 0
#Laptop - 1500
#total = 2000
#rule: ignore items with price zero 
json_file_10 = {
    "name" : "create_invoice",
    "arguments": {"items": [{"name": "Book", "price" : 500},
                               {"name" : "Laptop", "price": 1500}, "total" :2000 ]}
}

