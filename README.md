# PhishGuard-Pro-Multi-Layered-Anti-Scam-DDoS-Mitigation-Engine
PhishGuard is an active defense system designed to identify and neutralize phishing threats through automated content analysis and traffic rate-limiting. It doesn't just block malicious IPs—it uses an intelligent scoring engine to "fingerprint" scam content and visualizes threats in real-time to protect end-users from financial fraud.
## 🛠️ Tech Stack
* **Frontend Dashboard:** Streamlit (Python framework)
* **Backend Detection:** Python (BeautifulSoup4, Requests)
* **Server-side Defense:** PHP (Rate-limiting logic)
* **Data Visualization:** Matplotlib, WordCloud

## ✨ Key Features
* **Scoring Engine:** Automatically evaluates URL risk based on HTTPS protocols and phishing keywords.
* **Threat Visualization:** Generates real-time word clouds to highlight scam vocabulary.
* **DDoS Mitigation:** Implements an active defense that triggers HTTP 429 when abnormal traffic is detected.
* **Performance Analytics:** Monitors and plots server latency during stress tests.

## 📸 Screenshots
### 1. Dashboard & Content Analysis
![Scam Detection Dashboard](./scam_cloud.png)
*Real-time keyword analysis and risk scoring.*

### 2. Performance Monitoring
![Latency Chart](./performance_chart.png)
*Tracking server response time during automated request simulations.*

## 🚀 How to Run
1. Start the local PHP server:
   ```bash
   php -S 127.0.0.1:8080
