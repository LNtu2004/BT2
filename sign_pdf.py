from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
import datetime

# === Cấu hình đầu vào ===
signature_image = "ten.jpg"   # ảnh chữ ký của bạn
output_pdf = "signed.pdf"     # tên file xuất ra
page_width, page_height = A4

# === Thông tin người ký ===
name = "Lê Ngọc Tú"
phone = "0582007343"
student_id = "K225480106069"
sign_date = "31/10/2025"  # có thể đổi sang datetime.now().strftime("%d/%m/%Y")

# === Tạo PDF và khung chữ ký ===
def draw_signature_box(c):
    box_width = 270   # chiều rộng khung
    box_height = 110  # chiều cao khung
    margin_right = 50  # cách mép phải
    margin_bottom = 50  # cách mép dưới

    # Tính vị trí góc trái dưới của khung
    x = page_width - box_width - margin_right
    y = margin_bottom

    # Vẽ khung chữ ký
    c.setStrokeColor(colors.black)
    c.rect(x, y, box_width, box_height, stroke=1, fill=0)

    # Ảnh chữ ký bên trái
    img_width = 110
    img_height = 70
    img_x = x + 10
    img_y = y + 20

    try:
        c.drawImage(ImageReader(signature_image), img_x, img_y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')
    except Exception as e:
        print(f"Lỗi khi chèn ảnh chữ ký: {e}")

    # Thông tin bên phải
    text_x = img_x + img_width + 10
    text_y = img_y + img_height - 5

    c.setFont("Times-Roman", 12)
    c.drawString(text_x, text_y, name)
    c.drawString(text_x, text_y - 18, f"SDT: {phone}")
    c.drawString(text_x, text_y - 36, f"MSV: {student_id}")
    c.drawString(text_x, text_y - 54, f"Ngày ký: {sign_date}")

# === Tạo PDF mới ===
def create_signed_pdf():
    c = canvas.Canvas(output_pdf, pagesize=A4)
    c.setFont("Times-Roman", 14)
    c.drawString(50, page_height - 50, "BẢN KÝ XÁC NHẬN (Demo Chữ Ký Số)")
    draw_signature_box(c)
    c.showPage()
    c.save()
    print(f"✅ Đã tạo file {output_pdf} thành công!")

if __name__ == "__main__":
    create_signed_pdf()
