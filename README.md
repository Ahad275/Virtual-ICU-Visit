# 🏥 Virtual Patient Monitoring System for Hospitals

A Django-based web application designed to bridge the communication gap between hospitalized patients and their families through secure, real-time virtual video monitoring using Zoom integration.

## 📌 Project Overview

The Virtual Patient Monitoring System allows family members to monitor their loved ones admitted in hospitals through secure video calls and virtual access. Especially during pandemics or critical health conditions where in-person visits are restricted, this system provides a reliable and secure solution for remote monitoring.

## 🚀 Features

- 🔐 Secure User Authentication  
- 📝 Patient Registration and Record Management  
- 🎥 Zoom SDK Integration for Video Monitoring  
- 📧 Automatic Email Notifications with Meeting Credentials  
- 📊 Admin Dashboard for Hospital Staff  
- 🕒 Real-Time Monitoring Access  
- 🗃️ Secure Storage of Patient Data  
- 🔄 Password Recovery System

## ScreenShot
![Screenshot 2025-04-08 220337](https://github.com/user-attachments/assets/2e16d890-bf22-47c7-8bb8-7a65014d5e73)
![Screenshot 2025-04-08 220348](https://github.com/user-attachments/assets/518762c4-86f2-4e26-ba5d-af11cd42d7bf)
![Screenshot 2025-04-08 220407](https://github.com/user-attachments/assets/e0a8d441-de75-4baf-8f8c-98679c68fa58)
![Screenshot 2025-04-08 220422](https://github.com/user-attachments/assets/b8f3c2e3-565a-4843-8356-4d9d84fa6c18)
![Screenshot 2025-04-08 220434](https://github.com/user-attachments/assets/e1bb36d7-608c-4b21-8bcb-ff0ab3826a84)
![Screenshot 2025-04-08 220537](https://github.com/user-attachments/assets/a443c9ec-922b-4737-9a11-850f2354c90e)
![Screenshot 2025-04-08 220600](https://github.com/user-attachments/assets/f546707b-40da-41f4-9714-419580d1f635)
![Screenshot 2025-04-08 220616](https://github.com/user-attachments/assets/3ab1f14b-cc15-4944-8235-7c9b6cd30690)
![Uploading Screenshot 2025-04-08 220630.png…]()




## 🛠️ Technology Stack

- **Backend:** Django (Python)  
- **Database:** SQLite / MySQL  
- **Frontend:** HTML5, CSS3, Bootstrap, JavaScript  
- **Video SDK:** Zoom SDK (Web Integration)  
- **Email Services:** Django’s SMTP for password reset & meeting ID sharing  

## 📁 Project Structure

virtual-monitoring/ ├── monitoring/ # Django app ├── templates/ # HTML templates ├── static/ # CSS, JS, image assets ├── db.sqlite3 # Database (or configure MySQL) ├── manage.py # Django management script └── requirements.txt # Python dependencies



## ⚙️ Setup Instructions

1. **Clone the repository**  
   `git clone https://github.com/your-username/virtual-patient-monitoring.git`  
   `cd Virtual ICU Visit`

2. **Create a virtual environment**  
   `python -m venv env`  
   `source env/bin/activate` *(or on Windows: `env\Scripts\activate`)*

3. **Install dependencies**  
   `pip install -r requirements.txt`

4. **Run migrations**  
   `python manage.py makemigrations`  
   `python manage.py migrate`

5. **Run the server**  
   `python manage.py runserver`

6. **Access the app**  
   Visit `http://127.0.0.1:8000/` in your browser

## 🔐 Zoom SDK Configuration

- Create a Zoom JWT or SDK App at [Zoom Marketplace](https://marketplace.zoom.us/)  
- Add your Zoom API Key and Secret in your `.env` file or Django settings  
- Setup meeting creation and joining flow via SDK/API  

## 🧩 Future Enhancements

- 📱 Mobile App Support (Flutter or React Native)  
- 🧠 AI Alerts for Critical Patient Movements  
- 🎥 Hospital CCTV Integration  
- 📅 Patient Visit Scheduling  

## 🤝 Contributing

Feel free to open issues or pull requests! Contributions are welcome to improve features, fix bugs, or expand this system.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

Thanks to all contributors and hospital staff who helped shape the requirements for this project.

> Developed with ❤️ to make healthcare more connected and accessible.
