# CSC 461 Exam I Fall 2024
**Record your answers using the QUIZ FOR Exam 1.**
You will just be given the Letter a, b, c,... to choose from for each (not the question from exam)
### Q1 (4 pts)
I claim that the following grammar is **ambiguous**.
```
<assign> → <id> = <term>
<expr> → id | <term> - <expr> | ( <expr> ) | <term> + <expr>
<term> → <expr>
<id> → X|Y
```
**Is the grammar above Ambiguous?**
- [ ] a) YES
- [ ] b) NO
### Q2 (4 pts)
A rightmost, leftmost, or neither right nor leftmost approach can be used in the derivation of a sentence in an unambiguous grammar. If each of these is used on the same sentence of such a language, how many possible different parse trees could be involved?
- [ ] a) 1
- [ ] b) 2
- [ ] c) 3
- [ ] d) More than 3 are possible
---
### Q [3-7] (10 pts, 2 each)
Given the following Extended BNF, which strings are **valid** or **invalid** "LINE"?
- `*` is zero or more
- `+` is one or more
```
<run>       → {0|1}* 
<squeeze>   → {010}* | {101}+
<LINE>      → <squeeze> <run> <squeeze>    (NOTE: This is the LINE to check)
```
**Valid/Invalid "LINE" (V or I)**
#### Q3: `10111010`
#### Q4: `101101`
#### Q5: `010110101101`
#### Q6: `000111101`
#### Q7: `101111100000`
---
### Assume you are using a new language called 'L' that is **imperative** and the **only storage type** for variables is "static" and is **implied**. 
Names are statically bound to variables. Initialization of variables is done only when created. You are asked to supply a print list function. You go find both a recursive and a non-recursive version of algorithms that print lists out in other languages on the internet. You can use the logic to try and write them in 'L' and are now trying to decide which one might be the best to use. 'L' uses **Static scoping** and there is a global variable called `LIST` that holds the list. `LIST` is an array of integers and the location after the last number in the list is a `-1` and can be used to know you are out of numbers.

**NOTE**: the answers to both question Q8 and Q9 should be in the context of the definition of the language 'L' given above and our study of languages in this class.
### Q8 (4 pts)
Of the two functions below, which function can you dismiss **without even doing analysis** (so by just simply looking at it without having to work through the logic in the code itself) of the two because you are using language L? 
- `Printlist()` 
- `recursive_printlist()`
**Why?**
- [ ] a) Dismiss `Recursive_printlist()` because 'L' can’t do recursion.
- [ ] b) Dismiss `Printlist()` because Static scoping can’t handle a Global List variable declaration.
- [ ] c) Dismiss `recursive_printlist()` because it is much harder to understand recursive logic.
- [ ] d) Not given enough initial information about 'L' to dismiss one without looking at how each works in more detail.
### Q9 (4 pts)
You decide to implement the other algorithm (**the one you did not dismiss in Q8**) and when you call it the first time, it works fine and prints the numbers in `LIST`. However, when you call it more than once in the same program, you get no output, or strange output, or the program crashes. **Why?**
- [ ] a) The while loop logic does not work even though `LIST` does have a `-1` at end of numbers.
- [ ] b) `t` is only initialized to `0` one time.
- [ ] c) There is not a good ground condition to end the function.
- [ ] d) There is no way to tell from the def of 'L' given why the code has issues during execution.
#### **Function code for Q8 and Q9**
```c
//========= Non-recursive ======================
void printlist() 
{
    int t = 0;
    while (LIST[t] != -1)   // while not equal to the -1 marker
    {
        cout << LIST[t] << endl;  // output value
        t = t+1;
    }
}

//========== Recursive ==================
void recursive_printlist(int t)  // assumes first call will pass in value 0 into t
{
    if (LIST[t] == -1)  // exit if -1 marker found
        return;
    cout << LIST[t] << endl;  // output value
    recursive_printlist(t+1);  // recursively call to move through the list
}
```
---
### Q 10 (3 pts)
Absolute Addressing can cause issues when if used while programming because:
- [ ] a) It is inefficient when executed.
- [ ] b) Inserting new code above the targeted address can change the location.
- [ ] c) Inserting code below the targeted address can change the location.
- [ ] d) It loses precision when truncated.
---
### Q 11 (3 pts)
LABEL statements were implemented to break from the Absolute Addressing approach to:
- [ ] a) Make the source code more readable.
- [ ] b) Make the source code more writable.
- [ ] c) Make the source code more reliable when executed.
- [ ] d) All of the other answers.
---
### Q 12 (3 pts)
An **unambiguous grammar** will have:
- [ ] a) Meaningful variable names.
- [ ] b) Will be well commented to help understand the code.
- [ ] c) Only one distinct parse tree.
- [ ] d) Will have a well-balanced parse tree.
---
### Q 13 (3 pts)
The declaration of a local variable with the same name as a non-local variable can **ONLY** hide the non-local variable in the local scope when:
- [ ] a) Static scoping is used.
- [ ] b) Dynamic scoping is used.
- [ ] c) If the non-local would be in the referencing environment if not for the local with the same name.
- [ ] d) All of the others.
---
### Q 14 (3 pts)
A **globally declared static variable** will always be visible everywhere in a program:
- [ ] a) Only if static scoping is used.
- [ ] b) Only if dynamic scoping is used.
- [ ] c) Only if not hidden by a local variable of the same name.
- [ ] d) Off and on as it is bound and unbound from a memory cell during execution.
---
### Q 15 (3 pts)
The usefulness of a **Language Generator** is:
- [ ] a) To generate useful syntactically correct code for a given language (like a button to be pushed).
- [ ] b) To determine if a statement is syntactically correct for a given language.
- [ ] c) Provide a set of rules for syntactically correct statements to help users understand the language.
- [ ] d) To generate an unambiguous grammar for a language.
---
### Q 16 (3 pts)
If the programmer wants to use an array, but 1) have the system manage it and 2) have it reuse memory when it can, they should choose what type of storage binding?
- [ ] a) A fixed stack-dynamic Array
- [ ] b) A static Array
- [ ] c) Explicit heap-dynamic Array
- [ ] d) Static scoping
---
### Something for each variable storage binding
### Q 17 (3 pts)
For which variable storage binding is the variable’s **LIFETIME** the execution of the program for start to finish?
- [ ] a) Static
- [ ] b) Stack-Dynamic
- [ ] c) Implicit Heap-Dynamic
- [ ] d) Explicit Heap-Dynamic
---
### Q 18 (3 pts)
For which variable storage binding is the variable’s **LIFETIME** from function invocation to the end of the function?
- [ ] a) Static
- [ ] b) Stack-Dynamic
- [ ] c) Implicit Heap-Dynamic
- [ ] d) Explicit Heap-Dynamic
---
### Q 19 (3 pts)
For which variable storage binding is the variable’s **LIFETIME** dependent on the programmer for allocation and deallocation?
- [ ] a) Static
- [ ] b) Stack-Dynamic
- [ ] c) Implicit Heap-Dynamic
- [ ] d) Explicit Heap-Dynamic
---
### Q 20 (3 pts)
For which variable storage binding is the variable’s **LIFETIME** a condition for recursion?
- [ ] a) Static
- [ ] b) Stack-Dynamic
- [ ] c) Implicit Heap-Dynamic
- [ ] d) Explicit Heap-Dynamic
---
### Q 21 (6 pts)
Our pseudo-code language we developed at the start of the semester has an increment and test statement (+7). Given the **limited number of statements** our design allowed (only 20), why was such a statement included since what it does could be accomplished without its inclusion?
- [ ] a) We had some left-over open statements so why not.
- [ ] b) It helped when implementing loop logic which is done a lot.
- [ ] c) It was the inverse logic of the -7 statement.
- [ ] d) It got away from absolute Addressing.
---
### Q 22 (6 pts)
Our pseudo-code language we developed at the start of the semester has an increment and test statement (+7). Given the **limited number of statements** our design allowed (only 20), what design principle was the decision to include the increment and test a very good example of?
- [ ] a) Impossible Error
- [ ] b) Regularity
- [ ] c) Reliability
- [ ] d) Abstraction
---
### Q 23 (3 pts)
When you begin to learn a new language, it often seems strange, and although eventually it may help you be more productive, at first it actually slows your coding down. How would our understanding of **Tools** in general explain this?
- [ ] a) We have yet to reach the Objectification phase.
- [ ] b) We have yet to reach the Embodiment phase.
- [ ] c) We are more of a Dystopian than a Utopian.
- [ ] d) We are lazy.
---
### Q 24 (3 pts)
When learning programming, one is often taught to use meaningful **Variable Names**. Why?
- [ ] a) To help with the readability of the source code.
- [ ] b) To help the compiler parse the syntax.
- [ ] c) Because the language usually enforces that you do.
- [ ] d) All of the others.
---
### Q 25 (3 pts)
Early programming languages often only implemented **Static variable storage binding**, which:
- [ ] a) Limited the number of characters a variable name could have.
- [ ] b) Did not allow for recursion.
- [ ] c) Made things run less efficiently.
- [ ] d) All of the others.
---
![](Scope%20Diagram%20for%20Program%20P..png)
Assume program P always starts in MAIN !
### Figure 1: Scope Diagram for Program P

The diagram represents a **scope hierarchy** for a computer program labeled "Program P." It is designed to illustrate the concept of **variable scoping**—both **static** and **dynamic**—in programming, which dictates which variables are accessible in different parts of the code during execution.

#### Structure of the Diagram

1. **Global Scope:**
    
    - At the top of the diagram, there is a large rectangle labeled **GLOBAL**.
    - Inside this global scope, there are three variables listed vertically:
        - **X**
        - **A**
        - **B**
    - These variables are considered **global variables** and are accessible from anywhere within the program, depending on the scoping rules (static or dynamic).
2. **Function F1:**
    
    - Inside the global scope, there is a box representing **Function F1**.
        
    - It contains one variable:
        
        - **W**
    - **Function F1** itself contains two nested functions: **F3** and **F4**.
        
    - **Function F3:**
        
        - Within the scope of **F1**, there is a smaller rectangle representing **Function F3**.
        - This scope contains a single variable:
            - **A**
        - **F3** can access its own local variable **A**, as well as the variable **W** from **F1** and any global variables, depending on the scoping rules.
    - **Function F4:**
        
        - Also nested within **F1** is a rectangle representing **Function F4**.
        - It has one variable:
            - **B**
        - **F4** can access its own local variable **B**, the variable **W** from **F1**, and global variables, depending on the scoping rules.
3. **Function F2:**
    
    - At the same level as **F1** but separate from it, there is another box representing **Function F2**.
    - It contains two variables:
        - **A**
        - **B**
    - **F2** can access its own variables **A** and **B**, along with global variables depending on the scoping rules. However, it does not have access to variables in **F1**, **F3**, or **F4** unless the scoping mechanism permits.
4. **Main Function:**
    
    - At the bottom of the diagram, there is a box labeled **MAIN**.
    - Inside this box, there is one variable:
        - **X**
    - **MAIN** represents the starting point of the program execution, and it can access the global variable **X** as well as any other global variables, depending on the scoping rules.
### Q 26 (4 pts)
In Fig 1, using **STATIC** Scoping, what is the referencing environment if in F4?
- [ ] a) {Global: (X and A and B), F1:W, F4:B}
- [ ] b) {MAIN: X, F1:W, F3:A, F4:B}
- [ ] c) {Global: A, MAIN: X, F1:W, F4:B}
- [ ] d) {Global: (X and A), F1:W, F4:B}
- [ ] e) Can't tell by looking at fig 1.

### Q 27 (4 pts)
In Fig 1, assuming the program starts executing in MAIN and then calls F2, which then calls F1 which then calls F3 that then calls F4. Using **STATIC** Scoping, what is the referencing environment if in F4?
- [ ] a) {Global: (X and A and B), F1:W, F4:B}
- [ ] b) {MAIN: X, F1:W, F3:A, F4:B}
- [ ] c) {Global: A, MAIN: X, F1:W, F4:B}
- [ ] d) {Global: (X and A), F1:W, F4:B}
- [ ] e) Can't tell by looking at fig 1.

### Q 28 (4 pts)
In Fig 1, assuming the program starts executing in MAIN and then calls F2, which then calls F1 which then calls F3 that then calls F4. Using **DYNAMIC** Scoping, what is the referencing environment if in F4?
- [ ] a) {Global: (X and A and B), F1:W, F4:B}
- [ ] b) {MAIN: X, F1:W, F3:A, F4:B}
- [ ] c) {Global: A, MAIN: X, F1:W, F4:B}
- [ ] d) {Global: (X and B), F1:W, F4:B}
- [ ] e) Can't tell by looking at fig 1.

---
### Q 29 (4 pts)
In Fig 1, assuming the program starts executing in MAIN and then calls F2, which then calls F1 which then calls F3 that then calls F4. Using **STATIC** Scoping, what variables are **ALIVE** if in F4?
- [ ] f) {Global: (X and A and B), F1:W, F4:B}
- [ ] g) {Global: (X and A and B), MAIN:X, F2(A and B), F1:W, F3:A, F4:B}
- [ ] h) {Global: A, MAIN: X, F1:W, F4:B}
- [ ] i) {Global: (X and A), F1:W, F4:B}
- [ ] j) Can't tell by looking at fig 1.
### Q 30 (4 pts)
In Fig 1, assuming the program starts executing in MAIN and then calls F2, which then calls F1 which then calls F3 that then calls F4. Using **DYNAMIC** Scoping, what variables are **ALIVE** if in F4?
- [ ] a) {Global: (X and A and B), F1:W, F4:B}
- [ ] b) {Global: (X and A and B), MAIN:X, F2(A and B), F1:W, F3:A, F4:B}
- [ ] c) {Global: A, MAIN: X, F1:W, F4:B}
- [ ] d) {Global: (X and B), F1:W, F4:B}
- [ ] e) Can't tell by looking at fig 1.

---

---



## **1. User Management System**

The **User Management System** is the backbone of the WealthWise platform, enabling users to register, log in, manage their profiles, and interact with other components. This system must ensure seamless functionality, security, and scalability.

### **1.1 User Registration**

- **Form Presentation**:
    - A new user shall be able to create an account by clicking on the “register” button on the login page; entering an email, which will double as a username; and choosing a password.
    - The registration page should presents a clean, easy-to-use form with fields for email, password, and basic user information including a phone number.
    - Additional fields, such as financial goals, should be included as optional for clients, while advisors should have fields for certifications or specializations in the registration page.
- **Data Validation**:
    - The data from this interaction shall be encrypted using TLS to ensure the password remains secure.
    - Frontend validation checks shall be performed to ensure the email format is correct, passwords meet the complexity requirements, and required fields are filled.
    - The password shall be at least 12 characters and include at least one capital letter, lowercase letter, number, and special character.
    - The system shall also check for duplicate emails, displaying an error message if a user attempts to register with an already existing account.
    - Stored password hashes shall be salted to make them less vulnerable to brute-force attacks.
- **Email Verification**:
    - Upon submitting the form, a verification email is sent to the provided email address. This email includes a unique, time-sensitive token that users must click to verify their account.
    - The system should then use SendGrid to send a verification email to the user. The user clicks the link in the email to prove they can access the email they entered.
    - If users do not verify within a specified timeframe (e.g., 24 hours), their account remains inactive. Reminders will be sent periodically to encourage verification.
    - Verification links will be encrypted and set to expire within a fixed duration to minimize security risks.

### **1.2 User Login**

The user shall be able to access their account using the email and password they created the account with. The user shall enter their credentials on the login page and click login. The password shall be encrypted using TLS to ensure it remains secure. The user will be authenticated and allowed to access the website if the credentials match. Should the user fail to log in 3 times, their account will be locked out for 3 minutes. Once authenticated, the system should establish JWT with the client for easy authentication. This effectively allows “remember me”.

### **1.3 Password Recovery**

If the user wishes to reset their password, either whether it was forgotten or not, they shall be able to click “reset password” at which point SendGrid shall be used to send the user a password reset link that expires in 10 minutes. The user can then choose a new password using the same requirements seen in 1.1.

- **Password Reset Request**:
    - Users can initiate a password reset by entering their registered email. The system then generates a **password reset token**, which is sent via email.
    - This token is valid for 10 minutes, with a countdown timer displayed on the reset page to inform users of the expiration.
- **Token Validation**:
    - Upon clicking the reset link, the system verifies the token’s validity. If valid, users are prompted to set a new password that meets the original registration requirements.
    - After resetting the password, all active sessions will be terminated, forcing users to log in again using the new credentials to ensure complete security.

---

### **1.4 Profile Management**

The user shall be able to enter their profile from the website and update their personal information. The user shall be able to edit their name, phone number, email address, profile picture, financial goals, and privacy settings (allowing other users to view account details). The system shall verify the validity of address fields (only letters in city, state, county, etc.), phone numbers (XXX-XX-XXX format), and the validity of characters (only letters) in the name field.

Should the account belong to an advisor, the advisor shall be able to upload certifications and licenses via SFTP and edit their bio and area(s) of expertise. The advisor account shall also display the ratings from previous clients.

- **Profile Viewing and Editing**:
    - Users can access their profile from the dashboard, where they see an overview of their information, including name, contact details, financial goals, and privacy settings.
    - Each field can be edited independently, with real-time validation ensuring that only valid inputs are accepted.
- **Advisor-Specific Fields**:
    - Advisors have additional fields, such as certifications, licenses, bio, and specialization areas.
    - The system supports secure file uploads for certifications, which are reviewed by admins for verification.
    - Advisors can update their bios to better market themselves to potential clients, making it easier for users to find a suitable match.
- **Privacy Settings**:
    - Users can control which details are visible to others, including financial goals and contact information.
    - Users can choose to make certain data public (visible to other users) or private (visible only to advisors during consultations).

---

### **1.5 Subscription Management**

**1.5.1 Subscription Viewing**

The user shall be able to view subscription information from their profile including whether they have an active subscription, the date until subscription expiration, previous subscription/payment history, and previous receipts of payments.

- **Current Subscription Details**:
    - Users can view their current plan, benefits, billing cycle, expiration date, and renewal status.
    - Active subscriptions show available features, while inactive subscriptions prompt users to renew.
- **Transaction History**:
    - A detailed history of past transactions, including payment dates, amounts, and methods used, is available for user reference.
    - Each transaction entry includes downloadable receipts, which users can use for personal record-keeping or expense tracking.

**1.5.2 Subscription Modification**

The user shall be able to view all subscription packages, pricing options, and features. The user shall be able to cancel their subscription and renew or purchase a subscription. Current subscription options include monthly pricing at $10 per month or yearly pricing at $100 per year. A subscription allows access to the budget planning tool. Upon subscription, the user shall have immediate access to said features.

- **Plan Selection Interface**:
    - Users can view different plans side-by-side, with a detailed breakdown of features, benefits, and pricing.
    - For upgrades, users gain immediate access to new features, while downgrades become effective at the end of the current billing cycle.
- **Plan Changes**:
    - The system ensures that no data is lost during plan changes. For example, when downgrading, users retain access to saved data from premium features, even if those features become restricted.
    - Users can also cancel their subscription mid-term, with prorated refunds applied according to the platform’s policy.

**1.5.3 Payment Management**

The user shall be able to purchase a subscription using PayPal, Stripe, or credit cards (Master Card or Visa). Data shall be secured using the vendor’s security options (ex. PayPal uses 128-bit SSL). History of payment amount, date, relevant payment information(credit card information, PayPal information, etc.), and subscription shall be recorded in the database. The user shall be able to set up automatic renewal via a checkbox in the menu. This will allow the website to automatically use stored payment information to purchase subscriptions in the future. This can be disabled by unchecking the same auto-renew box.

- **Multiple Payment Options**:
    - Users can pay with credit cards, PayPal, or Stripe, ensuring flexibility.
    - Payments are processed using secure gateways, with sensitive card data never stored directly on the platform.
- **Auto-Renewal Settings**:
    - Users can opt into auto-renewal during purchase or enable it later from their account settings.
    - Automatic payments are processed at the end of each billing cycle, with users receiving notification emails before charges are made.
- **Payment Security**:
    - Transactions are secured with **PCI-DSS compliance**, ensuring user data protection.
    - In case of payment failures, users receive prompts to update payment information to maintain their subscription.

---

### **1.6 Interaction History**

**1.6.1 Consultation History**

Following an advisor meeting, the date, time, advisor name, and advisor rating shall be stored in the database for future viewing in the user’s profile. The user shall be able to rate the advisor on a scale of 1-10, which will be visible from the advisor’s profile and the specific user’s profile (private). Any files the advisor generates and uploads via SFTP to the server shall be downloadable from the consultation history entry in the user profile.

**1.6.2 Event Participation History**

Following an event attendance, the date, time, and event name shall be stored in the database for future viewing in the user’s profile. Any posted files uploaded by the event organizer via SFTP shall be downloadable from the event history entry in the user profile.

---

### **1.7 Advisor Management**

The **Advisor Management System** provides tools for financial advisors to manage their profiles, interact with clients, and maintain availability. It ensures that advisors can offer effective consultations and users can connect with the right financial professionals.

**1.7.1 Advisor Account Creation**

Advisors apply for accounts by submitting personal information and credentials, which are verified by administrators. Approved advisors gain access to advisor-specific functionalities, such as managing availability, viewing client details, and setting consultation rates.

Advisors have a more complex onboarding process than regular users, ensuring that they meet specific qualifications and certifications to provide financial advice.

- **Registration Process**:
    - The advisor registration form includes additional fields such as certifications, licenses, areas of specialization, and professional bio.
    - Advisors must upload scanned copies of their certifications, which are reviewed manually by the platform administrators for authenticity.
    - After submission, the advisor profile enters a **"Pending Approval"** state, during which admins validate the provided credentials.
- **Verification by Administrators**:
    - Administrators can access a dashboard where they can review advisor applications, verify credentials, and approve or reject advisor accounts.
    - Once approved, advisors are granted access to advisor-specific features like profile customization, client search, consultation scheduling, and messaging.
    - Rejected applications trigger an automated email response detailing the reason for rejection and next steps (e.g., re-submission of valid documents).

**1.7.2 Advisor Availability Management**

Advisors use a dedicated calendar to manage their consultation schedules and availability.

- **Calendar Interface**:
    - The system provides a calendar view where advisors can set available slots for consultations. They can mark time as "Available," "Busy," or "Out of Office" for specific dates and times.
    - Advisors can also add recurring availability slots (e.g., "Every Monday from 10 AM to 2 PM"), making it easier to manage regular working hours.
- **Real-Time Updates**:
    - Any changes to availability (e.g., adding or removing slots) are immediately reflected on the client-side booking interface, ensuring up-to-date scheduling options.
    - The system uses a real-time sync mechanism to prevent double bookings, providing immediate feedback to advisors when a slot is booked or canceled by a client.
- **Sync with External Calendars**:
    - Advisors can optionally integrate their platform calendar with external services (e.g., Google Calendar, Outlook) to maintain consistency across all scheduling systems. This integration supports two-way syncing, where updates from the external calendar also reflect on the platform.

---

### **1.6 Messaging and Notifications**

**1.6.1 In-App Messaging**

The in-app messaging system enables secure communication between clients and advisors, supporting both text and file sharing.

- **Chat Features**:
    - The chat interface allows users to send and receive real-time messages with typing indicators, read receipts, and message timestamps.
    - Users can share documents or images within the chat, which are automatically scanned for security (e.g., file type validation and virus checks).
- **Message Encryption**:
    - Messages are end-to-end encrypted to protect user privacy, ensuring that only the intended recipient can read the message content.
    - Chat history is stored securely, with options for users to search and filter conversations by date, keyword, or sender.
- **Message Management**:
    - Users can archive or delete conversations, while advisors can manage message threads based on client interactions.
    - Archived conversations can be retrieved from the "Archived Messages" tab, providing users with the ability to revisit past communications.

**1.6.2 Notifications and Alerts**

Notifications ensure users and advisors stay informed about relevant updates and reminders.

- **Notification Types**:
    - The system sends notifications for various events, including appointment reminders, new messages, subscription renewals, and upcoming events.
    - Users receive notifications via in-app alerts, email, or SMS, depending on their preferences. This flexibility ensures users can stay informed regardless of their preferred communication method.
- **Customization Options**:
    - Users can customize notification settings to opt in or out of specific alerts. For instance, users can choose to receive reminders for consultations but not marketing emails.
    - Advisors can set custom reminders for scheduled consultations or messages from clients, ensuring they stay prepared for each session.
- **Event-Based Notifications**:
    - Notifications are also triggered by events, such as when a user registers for a seminar or workshop. Event reminders include details like event date, time, and virtual or physical location.