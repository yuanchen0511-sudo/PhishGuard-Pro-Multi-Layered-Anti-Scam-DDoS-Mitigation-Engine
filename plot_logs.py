import matplotlib.pyplot as plt
import csv

def draw_chart():
    times = []
    latencies = []

    try:
        with open('attack_log.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # 跳過標題行 (如果你有標題的話)
            next(reader, None) 
            
            for row in reader:
                if len(row) >= 3:
                    # row[0] 是時間, row[2] 是延遲秒數
                    latencies.append(float(row[2]))
                    times.append(len(latencies)) # 簡單用序號當橫軸

        # 開始畫圖
        plt.figure(figsize=(10, 5))
        plt.plot(times, latencies, marker='o', linestyle='-', color='b')
        
        plt.title('Attack Response Time (Latency)')
        plt.xlabel('Request Number')
        plt.ylabel('Time (seconds)')
        plt.grid(True)
        
        # 儲存圖表
        plt.savefig('performance_chart.png')
        print("🎉 圖表已生成！請查看資料夾中的 performance_chart.png")
        plt.show()

    except Exception as e:
        print(f"畫圖失敗，可能 CSV 格式還不完整: {e}")

if __name__ == "__main__":
    draw_chart()