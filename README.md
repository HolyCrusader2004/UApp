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

## My Contributions  

I worked on several key features of UApp, contributing to both the frontend and backend development. Below are the details of my contributions:

### 1. **Sign-In/Register Page**  
- Developed the frontend functionality for the sign-in and registration process.  
- Created and integrated the **Redux store** to manage user state across the app.  
- Implemented **cookie-based logic** with **JWT authentication** for secure user sessions.  
- Integrated **Firebase login** to enable seamless authentication.  

**Screenshot:**  
![Screenshot 2025-01-24 215803](https://github.com/user-attachments/assets/fdedb25d-9fd7-475b-9e31-5336d12962ef)


---

### 2. **Chat Application**  
- Worked on the **frontend development** of the chat app, enabling real-time messaging functionality.  
- Integrated Firebase to ensure smooth and responsive communication between users.  

**Screenshot:**  
![Screenshot 2025-01-24 232847](https://github.com/user-attachments/assets/c2fdc74f-7a5b-4cdc-9298-7f97f98611bf)


---

### 3. **Parking Reservation Backend Functionality**  
- Developed the **backend logic** for the parking reservation feature.  
- Wrote an automated script using **Django APScheduler** that checks the status of parking slots every X minutes.  
- Implemented logic to **automatically update slot statuses** in the database when reservations are completed.  

