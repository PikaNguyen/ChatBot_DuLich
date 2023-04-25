# ChatBot_DuLich
ChatBot tư vấn hỗ trợ du lịch

Tải về giải nén ra thì xóa file.rasa/cache đi cũng được

Xong thì mở CMD trong thư mục đó lun
![image](https://user-images.githubusercontent.com/85334608/233958478-4f08ad30-1dd8-4a77-8c56-b8ec3fea0899.png)

- Ghi lệnh: 
rasa train
- Chạy xong train thì ghi lệnh
rasa run --cors "*"
![image](https://user-images.githubusercontent.com/85334608/233959069-0e173a58-237d-406f-ad74-4c5ab228fd38.png)

- Mở tiếp 1 cmd trong thư mục đó ghi lệnh
rasa run actions --actions actions

Xong mở file Web3.html test

![image](https://user-images.githubusercontent.com/85334608/234189631-2da25956-64b1-48ed-886a-b8a13124426b.png)

![image](https://user-images.githubusercontent.com/85334608/234189695-e774cb5b-a563-4ac4-ab70-a2d4255d518b.png)


Hướng dẫn đơn giản: 

![image](https://user-images.githubusercontent.com/85334608/234290177-7b4a237d-bf6f-4418-811a-06fa2994f317.png)


Hướng dẫn đơn giản: 
1)tạo intent trong nlu.ym
nlu.yml:
nlu:
- intent: thac_pongour
  examples: |
    - thác pongour
    - thong tin ve thac pong gô
    - thác bông gô
    - pông ghô

2) vào domain.yml khai báo intent và tạo action trong response 
intents:
- thac_pongour

responses:
  utter_thac_pongour:
  - text: "Là một thác nước đẹp và imposant nằm khoảng 50km về phía nam của Đà Lạt. Đây là một trong những thác nước đẹp nhất ở Đông Nam Á với chiều cao 40m và chiều rộng 100m."

3) Vào rule.yml 
rules:

- rule: xem thác pongour
  steps:
  - intent: thac_pongour
  - action: utter_thac_pongour

4) train dữ liệu xong chạy


