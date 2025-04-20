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
