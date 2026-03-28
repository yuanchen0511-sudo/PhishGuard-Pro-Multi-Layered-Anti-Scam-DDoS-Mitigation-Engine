import datetime

import json

import random

import string

import threading

import uuid

import time

import csv

import requests

from requests.exceptions import SSLError



class CredentialGenerator:

    def __init__(self):

        self.chars = string.ascii_letters + string.digits

        # 為了簡化，如果找不到檔案，我們就用預設清單 (避免你沒準備好 JSON 報錯)

        try:

            self.emails = json.loads(open('assets/emails.json').read())

            self.common_passwords = json.loads(open('assets/common_passwords.json').read())

            self.dictionary = json.loads(open('assets/dictionary.json').read())

            self.extensions = ["com", "net", "org"]

            self.surname = ["Smith", "Chen", "Lee"]

            self.firstname_male = ["John", "Mike"]

            self.firstname_female = ["Mary", "Jane"]

        except:

            # 如果你還沒準備好 JSON 檔，先用這些預設值跑跑看

            self.emails = ["gmail", "yahoo", "outlook"]

            self.common_passwords = ["123456", "password", "admin"]

            self.dictionary = ["apple", "dog", "sun"]

            self.extensions = ["com", "tw"]

            self.surname = ["Wang", "Li"]

            self.firstname_male = ["Kevin"]

            self.firstname_female = ["Rose"]



    def generate_random_email(self):

        return f"{random.choice(self.dictionary)}{random.randint(1,99)}@{random.choice(self.emails)}." + random.choice(self.extensions)



    def generate_random_password(self):

        return random.choice(self.common_passwords) + str(random.randint(10, 99))



    def generate_random_ip(self):

        return f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'



class CredentialTester:

    def __init__(self, target_url, login_form_data):

        self.url = target_url

        self.form_data = login_form_data

        self.gen = CredentialGenerator()



    def log_to_csv(self, status, r_time, email, ip):

        # 這是我們討論的 CSV 紀錄功能

        file_exists = False

        try:

            with open('attack_log.csv', 'r') as f: file_exists = True

        except FileNotFoundError: pass



        with open('attack_log.csv', 'a', newline='') as f:

            writer = csv.writer(f)

            if not file_exists:

                writer.writerow(['timestamp', 'status_code', 'response_time', 'email', 'ip'])

            writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, round(r_time, 3), email, ip])



    def try_credentials(self):

        try:

            # 準備假資料

            fake_email = self.gen.generate_random_email()

            fake_pass = self.gen.generate_random_password()

            payload = {"email": fake_email, "password": fake_pass}



            # --- 開始計時 ---

            start = time.time()

            r = requests.post(self.url, data=payload, timeout=5)

            end = time.time()

            # --- 結束計時 ---



            r_time = end - start

            print(f"成功發送! 狀態碼: {r.status_code}, 耗時: {round(r_time, 3)}秒")



            # 存入 CSV

            self.log_to_csv(r.status_code, r_time, fake_email, self.gen.generate_random_ip())



        except Exception as e:

            print(f"發生錯誤: {e}")



if __name__ == '__main__':

    target = input('請輸入模擬釣魚網址 (例如 http://localhost:8080/login.php): ')

    num_threads = int(input('請輸入執行緒數量 (建議先填 1): '))



    tester = CredentialTester(target, {})

    

    for _ in range(num_threads):

        # 為了測試方便，我們讓它跑一次就好，不要 while True 停不下來

        t = threading.Thread(target=tester.try_credentials)

        t.start()