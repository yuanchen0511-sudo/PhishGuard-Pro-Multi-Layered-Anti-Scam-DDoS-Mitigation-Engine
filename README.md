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
### 1. Dashboard & Content Analysis (Detection Tier)
We use an intelligent scoring engine (with an 85/100 risk score default for non-HTTPS or high-density scam sites) to "fingerprint" scam content. This text-based threat is then visualized into an intuitive "Word Cloud."
<img width="811" height="303" alt="scoring_engine_screenshot" src="https://github.com/user-attachments/assets/35d4e52b-cdfc-404b-8c16-43e7a6750bf6" />
* In this screenshot, the dashboard successfully identifies and visualizes high-risk terms like "investment," "profit," and "join LINE."*
## 2. Performance Monitoring & Stress Testing (Data Tier)
PhishGuard supports simulating multi-threaded shadow requests to test how servers handle massive automated traffic. We plot server response times to visualize attack pressure.
<img width="801" height="249" alt="data_layer_screenshot" src="https://github.com/user-attachments/assets/54d8ace4-9113-4a45-b706-80312fde717f" />
* Notice how the latency curve spikes during the simulated attack, illustrating the overhead required for the server to process automated requests.*

### 3. Automated Mitigation Logic (Defense Tier)
Our active defense system uses a PHP-based firewall to protect server resources. When abnormal traffic is detected, the system automatically triggers an **HTTP 429 (Too Many Requests)** response.
<img width="390" height="250" alt="defense_layer_screenshot" src="https://github.com/user-attachments/assets/e8248761-5115-4dcb-b62b-6e48e3b6c313" />
* This view confirms the back-end defense in action. When an IP exceeds our defined limit (e.g., 5 requests per second), PhishGuard successfully blacklists the IP and issues a mitigation response.*

## 🚀 How to Run
1. Start the local PHP server:
   ```bash
   php -S 127.0.0.1:8080
2. Launch the Streamlit dashboard:
   ```bash
   python -m streamlit run app.py


