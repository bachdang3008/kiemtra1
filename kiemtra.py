import matplotlib.pyplot as plt

# Nhập số lượng từ bàn phím
nam = int(input("Nhập số lượng Nam: "))
nu = int(input("Nhập số lượng Nữ: "))

gender = ['Nam', 'Nữ']
count = [nam, nu]
colors = ['#3498db', '#e74c3c']

plt.figure(figsize=(6, 5))
plt.bar(gender, count, color=colors, width=0.5)

plt.title('Tỷ lệ Nam/Nữ trong lớp học', fontsize=14, fontweight='bold')
plt.xlabel('Giới tính', fontsize=12)
plt.ylabel('Số lượng học sinh', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Điều chỉnh giới hạn trục Y để nhãn số liệu không bị đè/mất
if max(count) > 0:
    plt.ylim(0, max(count) * 1.15)

# Thêm nhãn số liệu trên đỉnh mỗi cột
for i, v in enumerate(count):
    plt.text(i, v + (max(count) * 0.02 if max(count) > 0 else 0.5), str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('bieu_do_nam_nu.png', dpi=300, bbox_inches='tight')
print("Đã lưu biểu đồ thành công vào file 'bieu_do_nam_nu.png'!")
# Hiển thị biểu đồ ra màn hình
plt.show()
