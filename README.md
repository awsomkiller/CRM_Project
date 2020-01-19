# CRM_Project


This project is divided on the based of functionality of CRM, each Functionality is categorize as Module or 'APPs' of the Project, there are total of 6 Django Apps

Django Apps 

        #1 Accounts :
            Maintains the record of users, the Users are mainly categorize in two form 1st "User Employee" and "User Customer", both have seperate database table, Login functionlity is provided to the User Employee.

            The User Employee is further categorize on the basis of type of staff,

            User Employee Category :

                1. Super User :
                    The Super User is the admin of the Entire project, Capable to create New tables in database, and to follow admin process, this account can be used for auditing purpose also.

                2. Manager :
                    This is the Buisness account, This label checked has the power to work in application at administration level. Rights to make other admin and Modify delete data from table.

                3. HR : 
                    This is special admin account specifically design to monitor the performance of the staff member, Generate Payroll and etc

                4. Staff :
                    The staff is active employee member, that only have rights to create  new entry and modify any entry on database on service level.

                 Active :
                    This is special tag provided, to Employee user to determine whether they are an active working member. The login features can only be utilize by the active member in the application.

        #2 Branches

        #3 Business Development

        #4 finance

        #5 SLA (Service legal agreement)

        #6 HR

# Database Model

User Employee Model :

    userName
    emailId  
    fullName
    dob 
    contactNo
    panNo 
    govIdType
    govId
    seniorId 
    password 
    superUser 
    manager 
    Hr  
    active 

User Customer Model :

    fullName
    emailId 
    contactNo 
    address
    govIdType 
    govId 
    isActive 
    creationDate 
    creator 

Service Type :

    id 
    name
    creator
    isActive

Service Plans :

    id
    serviceId 
    name
    code
    description
    cost 
    creator 
    isActive


User Service Plans :

    id 
    userId 
    planId 
    dateOfBooking
    dateOfBill 
    dueDate

User Customer Bill :

    id 
    amount 
    receipt
    connectionId

User Customer Reciept :

    id 
    transactionId 
    connectionId 
    billId 


User Customer Transaction :

    id 
    billId 
    modeOfTransaction 

User Employee Package :

    id
    userId
    amount 
    description 
    isActive

User Employee Payment Bill :

    id 
    packageId 
    totalAttendance 
    totalDays
    paymentReceipt 
    amount 

User Payment Reciept :

    id 
    amount 
    salaryMonth 
    dateOfPayment 
    modeOfPayment 
    comments
