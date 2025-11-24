# 🤖 Simple Gemini Agent (LangGraph-based Chatbot)

## ✨ Giới thiệu

`simple_agent` là một chatbot cơ bản được xây dựng bằng **LangGraph** để minh họa cách tạo ra một luồng xử lý (workflow) đơn giản, tuần tự, sử dụng mô hình ngôn ngữ lớn **Gemini 2.5 Flash** của Google.

Dự án này là bước đệm để hiểu về cấu trúc **LangGraph StateGraph**, các **Node** (đại diện cho hàm `chatbot`) và **Edge** (đường đi từ `START` đến `END`).

## ⚙️ Yêu cầu Hệ thống

Để chạy dự án này, bạn cần:

- Python 3.11+
- Tài khoản Google AI Studio và khóa API **Gemini API Key**.

## 🛠️ Cài đặt và Thiết lập

### 1. Cài đặt Thư viện

Sử dụng `pip` để cài đặt các thư viện cần thiết:

```bash
pip install langgraph langchain-google-genai python-dotenv
```

### 2. Thiết lập Biến môi trường

Tạo một file có tên `.env` ở thư mục gốc của dự án và thêm khóa API của bạn vào đó. Chương trình sẽ tự động tải khóa này bằng `load_dotenv()`.

```toml
# .env file
GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

## 🚀 Cách Thao tác (Usage)

Chạy file Python chính (main.py):

```bash
python main.py
```

Chương trình sẽ yêu cầu bạn nhập tin nhắn và in ra phản hồi từ Gemini.

### Cấu trúc Code Chính

Đoạn code định nghĩa luồng xử lý cốt lõi:

| **Thành phần** | **Mục đích** |
| --- | --- |
| **`class State(TypedDict)`** | Định nghĩa cấu trúc trạng thái, sử dụng `add_messages` để tự động nối lịch sử chat. |
| **`def chatbot(state)`** | Node xử lý logic: Lấy lịch sử chat từ `state`, gọi `llm.invoke()`, và trả về tin nhắn phản hồi. |
| **`graph_builder`** | Khởi tạo biểu đồ, thêm node `"chatbot"`, và thiết lập cạnh tuần tự: `START` → `"chatbot"` →`END`. |

## 🌟 Tại sao sử dụng LangGraph?

Mặc dù Agent này đơn giản và có thể được thực hiện bằng cách gọi LLM trực tiếp, LangGraph được sử dụng để:

1. **Quản lý Trạng thái:** Minh họa cách **`StateGraph`** tự động quản lý và cập nhật lịch sử chat (`messages`) giữa các bước.
2. **Khả năng mở rộng:** Cung cấp nền tảng vững chắc để dễ dàng mở rộng thành các Agent phức tạp hơn với **nhiều Node** (ví dụ: Phân loại, Tra cứu Công cụ) và **cạnh có điều kiện** trong tương lai.