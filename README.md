my_social_network/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── posts.py
│   │   ├── groups.py
│   │   ├── friends.py
│   │   └── admin.py
├── alembic/
│   └── (alembic migration files)
├── alembic.ini
├── requirements.txt
└── README.md





 

 

Social network: 

 Users can register and setup a profile 

 Users can add activities to their 'wall' (like facebook) 

Users can send a friend request 

 Users can approve/deny a friend request 

 Users can see their 'wall' 

 Users can see an aggregated 'wall' with posts of their friends 

 Users can create groups and become admin group. 

Users can request to join groups. 

Group admins can accept or reject requests to join the group. 

Group admins can decide the rules of the groups. 

Group admins can dismiss members from the group. 

 Friends can message/chat with each other 

 Think of some admin functionality. 

------------------------------------------------------------------------------------------------------------- 

Admin can post some advertisements (New events, activities, een dagje uit). 

 

 

 

 

 

User Stories for Social Network Web Application 

User Registration and Profile Setup 

Story: As a user, I want to register by providing my email, username, and password so that I can create an account. 

Story: As a user, I want to set up my profile with details like my name, bio, profile picture, and contact information so that other users can know more about me. 

Adding Activities to Wall 

Story: As a user, I want to post activities or updates to my wall so that my friends can see what I’m up to. 

Sending Friend Requests 

Story: As a user, I want to send a friend request to another user so that we can connect and interact with each other. 

Approving/Denying Friend Requests 

Story: As a user, I want to approve or deny friend requests that I receive so that I can control who I connect with. 

Viewing Own Wall 

Story: As a user, I want to see all my posts and activities on my wall so that I can manage and reflect on my updates. 

Viewing Aggregated Wall 

Story: As a user, I want to see an aggregated wall with posts from all my friends so that I can stay updated with their activities. 

Creating Groups and Becoming Admin 

Story: As a user, I want to create a group and become its admin so that I can gather people with similar interests and manage group activities. 

Requesting to Join Groups 

Story: As a user, I want to request to join groups that interest me so that I can participate in discussions and activities. 

Accepting/Rejecting Group Join Requests 

Story: As a group admin, I want to accept or reject requests from users to join my group so that I can control the membership and maintain the group’s standards. 

Setting Group Rules 

Story: As a group admin, I want to set rules for my group so that members understand the guidelines and expectations for participation. 

Dismissing Group Members 

Story: As a group admin, I want to dismiss members from my group if they violate rules or behave inappropriately so that I can maintain a positive environment. 

Messaging/Chatting with Friends 

Story: As a user, I want to send messages to my friends so that we can communicate privately. 

Admin Functionality 

User Management 

Story: As an admin, I want to view, enable, or disable user accounts so that I can manage the user base and address any issues. 

Content Moderation 

Story: As an admin, I want to monitor and moderate posts and activities on the platform to ensure compliance with community standards. 

Group Management 

Story: As an admin, I want to view and manage groups, including the ability to remove groups that violate policies. 

Activity Logs 

Story: As an admin, I want to access activity logs to review user actions and platform usage for security and auditing purposes. 

Notification System 

Story: As an admin, I want to send notifications to users about important updates, changes, or alerts to keep them informed. 

Technical Backlog 

Database Schema Design 

Story: As a developer, I want to design the database schema to support user profiles, friend relationships, messages, and groups. 

API Documentation 

Story: As a developer, I want to provide comprehensive API documentation using tools like Swagger or Postman. 

Authentication and Security 

Story: As a developer, I want to implement authentication and security measures to protect user data and ensure secure access to the platform. 

These user stories provide a comprehensive overview of the functionalities required for a social network web application, covering both user-facing features and administrative controls. Each story should be broken down into specific tasks for development, testing, and deployment. 

 

 

 

Acceptance Criteria for Social Network Web Application 

1. User Registration and Profile Setup 

User Registration 

Given a user is on the registration page 

When they provide a valid email, username, and password 

Then the system should create a new account and send a confirmation email 

And the user should be redirected to the profile setup page 

Profile Setup 

Given a registered user is on the profile setup page 

When they provide their name, bio, profile picture, and contact information 

Then the system should save the profile information 

And display a confirmation message 

2. Adding Activities to Wall 

 

                    Acceptance Criteria 

Given a logged-in user is on their wall page 

When they enter and submit a new activity or post 

Then the system should display the new post on their wall 

And notify their friends about the new activity 

3. Sending Friend Requests 

                        

                    Acceptance Criteria: 

Given a logged-in user is on their wall page 

When they enter and submit a new activity or post 

Then the system should display the new post on their wall 

And notify their friends about the new activ 

Given a logged-in user is viewing another user's profile 

When they click the "Send Friend Request" button 

Then the system should send a friend request notification to the other user 

And display a confirmation message to the requester 

4. Approving/Denying Friend Requests 

 

                    Acceptance Criteria: 

Given a logged-in user has received a friend request 

When they view their friend requests 

Then they should see the option to approve or deny each request 

And the system should update the friendship status accordingly 

And notify both users of the decision 

5. Viewing Own Wall 

                    Acceptance Criteria: 

Given a logged-in user is on their profile page 

When they navigate to their wall 

Then the system should display all their posts and activities in chronological order 

6. Viewing Aggregated Wall 

 

 

                                Acceptance Criteria: 

Given a logged-in user is on the home page 

When they navigate to the aggregated wall 

Then the system should display posts from all their friends in chronological order 

7. Creating Groups and Becoming Admin 

 

                                 Acceptance Criteria: 

Given a logged-in user is on the groups page 

When they click the "Create Group" button and fill out the group details 

Then the system should create the group and assign the user as the group admin 

And display the new group in the user's list of groups 

8. Requesting to Join Groups 

                                Acceptance Criteria: 

Given a logged-in user is viewing a group they are not a member of 

When they click the "Request to Join" button 

Then the system should send a join request to the group admin 

And notify the user that their request is pending approval 

9. Accepting/Rejecting Group Join Requests 

                              Acceptance Criteria: 

Given a group admin is viewing their group's join requests 

When they choose to accept or reject a request 

Then the system should update the membership status accordingly 

And notify the user of the admin’s decision 

10. Setting Group Rules 

                             Acceptance Criteria: 

Given a group admin is on the group's settings page 

When they enter and save the group rules 

Then the system should display the rules to all group members 

11. Dismissing Group Members 

                   Acceptance Criteria:   

                    Given a group admin is viewing the list of group members 

When they select a member to dismiss and confirm the action 

Then the system should remove the member from the group 

And notify the member of their dismissal 

12. Messaging/Chatting with Friends 

                   Acceptance Criteria: 

                     Given two users are friends 

When one user sends a message to the other 

Then the system should deliver the message in real-time 

And notify the recipient of the new message 

Admin Functionality 

13. User Management 

                                Acceptance Criteria: 

                      Viewing Users 

Given an admin is on the admin dashboard 

When they navigate to the user management section 

Then the system should display a list of all users 

Enabling/Disabling User Accounts 

Given an admin is on the user management page 

When they select a user and choose to enable or disable their account 

Then the system should update the user’s status accordingly 

And notify the user of the change 

14. Content Moderation 

                            Acceptance Criteria: 

                      Given an admin is on the admin dashboard 

When they navigate to the content moderation section 

Then the system should display recent posts and activities 

And provide options to approve, flag, or remove content 

15. Group Management 

                               Acceptance Criteria: 

                   Given an admin is on the admin dashboard 

When they navigate to the group management section 

Then the system should display a list of all groups 

And provide options to remove groups that violate policies 

16. Activity Logs 

              Acceptance Criteria: 

                      Given an admin is on the admin dashboard 

When they navigate to the activity logs section 

Then the system should display logs of user actions and platform activities 

17. Notification System 

                                Acceptance Criteria: 

                     Given an admin is on the admin dashboard 

When they compose and send a notification 

Then the system should deliver the notification to all users 

And display a confirmation message to the admin 

Technical Backlog 

18. Database Schema Design 

                                 Acceptance Criteria: 

                    Given the database schema is designed 

When it is implemented 

Then it should support user profiles, friend relationships, messages, and groups without errors 

19. API Documentation 

                             Acceptance Criteria: 

                     Given the API is developed 

When the documentation is created 

Then it should comprehensively cover all endpoints and their usage 

And be accessible to developers 

20. Authentication and Security 

                                Acceptance Criteria: 

                   Given the authentication middleware is implemented 

When a user attempts to access protected routes 

Then the system should verify their credentials and provide access if valid 

And deny access if invalid 

 