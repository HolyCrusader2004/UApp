# UApp  

UApp is a full-stack student portal designed to simplify and enhance everyday student life. With UApp, users can communicate with others, reserve parking spots and washing machines, and stay informed through an admin-only forum.  

## Features  
- **Conversations:** Enables real-time messaging functionality for users.  
- **Reservation System:** Allows users to book parking spots and washing machines seamlessly.  
- **Admin Forum:** Provides important updates and announcements from the admin.  
- **Automated Modifications:** Parking reservations are automatically updated in the database when they are completed.  

## Technology Stack  
UApp leverages a robust technology stack to deliver an efficient and scalable solution:  

- **Frontend:** Built using **Next.js**, offering a responsive and interactive user interface.  
- **Backend:** Powered by **Django**, a high-performance Python web framework.  
- **Authentication:** Implements **JSON Web Tokens (JWT)** and cookie-based authentication for secure user sessions.  
- **State Management:** Uses **Redux** to store and manage user details across the app.  
- **Messaging:** Connects to **Firebase** for real-time communication between users.  
- **Database:** Utilizes **MySQL** for storing all application data.  
- **Task Scheduling:** Employs **Django APScheduler** to automate database modifications, ensuring efficient reservation management.  

## Key Highlights  
- **Seamless Integration:** Combines modern frontend and backend technologies for a seamless user experience.  
- **Real-Time Features:** Messaging powered by Firebase ensures quick and reliable communication.  
- **Automation:** Scheduled tasks improve efficiency by handling reservation updates automatically.  
