import os
import genanki

# Danh sách 100 từ vựng và định nghĩa tương ứng
terms = [
    ("Jakarta EE Platform", "Nền tảng Jakarta EE"),
    ("Application Server", "Máy chủ ứng dụng"),
    ("Container", "Bộ chứa"),
    ("Deployment Descriptor", "Mô tả triển khai"),
    ("Annotation", "Chú thích"),
    ("Enterprise Application", "Ứng dụng doanh nghiệp"),
    ("Jakarta EE Specification", "Đặc tả Jakarta EE"),
    ("Jakarta EE Community", "Cộng đồng Jakarta EE"),
    ("Jakarta EE Tutorial", "Hướng dẫn Jakarta EE"),
    ("Jakarta EE APIs", "Các API của Jakarta EE"),

    ("Jakarta Servlet", "Servlet Jakarta"),
    ("Jakarta Server Pages (JSP)", "Trang máy chủ Jakarta"),
    ("Jakarta Faces (JSF)", "Giao diện Jakarta"),
    ("Jakarta Expression Language (EL)", "Ngôn ngữ biểu thức Jakarta"),
    ("Jakarta Standard Tag Library (JSTL)", "Thư viện thẻ chuẩn Jakarta"),
    ("Jakarta RESTful Web Services (JAX-RS)", "Dịch vụ web RESTful Jakarta"),
    ("Jakarta XML Web Services (JAX-WS)", "Dịch vụ web XML Jakarta"),
    ("Jakarta WebSocket", "WebSocket Jakarta"),
    ("Jakarta JSON Processing (JSON-P)", "Xử lý JSON Jakarta"),
    ("Jakarta JSON Binding (JSON-B)", "Liên kết JSON Jakarta"),

    ("Jakarta Persistence (JPA)", "Lưu trữ Jakarta"),
    ("Entity", "Thực thể"),
    ("Persistence Unit", "Đơn vị lưu trữ"),
    ("Entity Manager", "Trình quản lý thực thể"),
    ("Jakarta Persistence Query Language (JPQL)", "Ngôn ngữ truy vấn lưu trữ Jakarta"),
    ("Object-Relational Mapping (ORM)", "Ánh xạ đối tượng-quan hệ"),
    ("Jakarta Transactions (JTA)", "Giao dịch Jakarta"),
    ("Jakarta Connectors (JCA)", "Kết nối Jakarta"),
    ("Resource Adapter", "Bộ điều hợp tài nguyên"),
    ("DataSource", "Nguồn dữ liệu"),

    ("Jakarta Messaging (JMS)", "Nhắn tin Jakarta"),
    ("Message", "Tin nhắn"),
    ("Queue", "Hàng đợi"),
    ("Topic", "Chủ đề"),
    ("Message-Driven Bean (MDB)", "Bean điều khiển tin nhắn"),
    ("Jakarta Mail", "Thư Jakarta"),
    ("Jakarta Batch", "Xử lý hàng loạt Jakarta"),
    ("Jakarta Concurrency", "Đồng thời Jakarta"),
    ("Jakarta Web Services", "Dịch vụ web Jakarta"),
    ("Jakarta XML Binding (JAXB)", "Liên kết XML Jakarta"),

    ("Jakarta Security", "Bảo mật Jakarta"),
    ("Authentication", "Xác thực"),
    ("Authorization", "Ủy quyền"),
    ("Role", "Vai trò"),
    ("Principal", "Chính"),
    ("Jakarta Authentication", "Xác thực Jakarta"),
    ("Jakarta Authorization", "Ủy quyền Jakarta"),
    ("Jakarta Identity Store", "Kho lưu trữ danh tính Jakarta"),
    ("Jakarta Security Context", "Ngữ cảnh bảo mật Jakarta"),
    ("Jakarta Security API", "API bảo mật Jakarta"),

    ("Jakarta Enterprise Beans (EJB)", "Bean doanh nghiệp Jakarta"),
    ("Stateless Session Bean", "Bean phiên không trạng thái"),
    ("Stateful Session Bean", "Bean phiên có trạng thái"),
    ("Singleton Bean", "Bean đơn"),
    ("Interceptor", "Bộ chặn"),
    ("Lifecycle Callback", "Gọi lại vòng đời"),
    ("Dependency Injection", "Tiêm phụ thuộc"),
    ("Contexts and Dependency Injection (CDI)", "Ngữ cảnh và tiêm phụ thuộc"),
    ("Managed Bean", "Bean được quản lý"),
    ("Bean Validation", "Xác thực Bean"),

    ("Integrated Development Environment (IDE)", "Môi trường phát triển tích hợp"),
    ("Build Tool", "Công cụ xây dựng"),
    ("Maven", "Maven"),
    ("Gradle", "Gradle"),
    ("Jakarta EE SDK", "Bộ phát triển phần mềm Jakarta EE"),
    ("Jakarta EE Runtime", "Thời gian chạy Jakarta EE"),
    ("Jakarta EE Profile", "Hồ sơ Jakarta EE"),
    ("Jakarta EE Web Profile", "Hồ sơ web Jakarta EE"),
    ("Jakarta EE Full Profile", "Hồ sơ đầy đủ Jakarta EE"),
    ("Jakarta EE Compatibility", "Tương thích Jakarta EE"),

    ("Unit Test", "Kiểm thử đơn vị"),
    ("Integration Test", "Kiểm thử tích hợp"),
    ("System Test", "Kiểm thử hệ thống"),
    ("TestNG", "TestNG"),
    ("JUnit", "JUnit"),
    ("Arquillian", "Arquillian"),
    ("Mocking", "Giả lập"),
    ("Debugging", "Gỡ lỗi"),
    ("Logging", "Ghi nhật ký"),
    ("Jakarta EE Testing", "Kiểm thử Jakarta EE"),

    ("Frontend", "Giao diện người dùng"),
    ("Backend", "Phần xử lý phía sau"),
    ("Model-View-Controller (MVC)", "Mô hình-Hiển thị-Điều khiển"),
    ("REST API", "API REST"),
    ("SOAP", "SOAP"),
    ("HTTP", "HTTP"),
    ("HTTPS", "HTTPS"),
    ("URL", "URL"),
    ("URI", "URI"),
    ("JSON", "JSON"),

    ("Jakarta EE Documentation", "Tài liệu Jakarta EE"),
    ("Jakarta EE Specification Documents", "Tài liệu đặc tả Jakarta EE"),
    ("Jakarta EE Examples", "Ví dụ Jakarta EE"),
    ("Jakarta EE Samples", "Mẫu Jakarta EE"),
    ("Jakarta EE Guides", "Hướng dẫn Jakarta EE"),
    ("Jakarta EE Tutorials", "Hướng dẫn học Jakarta EE"),
    ("Jakarta EE Community Forums", "Diễn đàn cộng đồng Jakarta EE"),
    ("Jakarta EE Mailing Lists", "Danh sách thư Jakarta EE"),
    ("Jakarta EE Blogs", "Blog Jakarta EE"),
    ("Jakarta EE Events", "Sự kiện Jakarta EE")
]

# Tạo thư mục đầu ra
output_dir = "/mnt/data/j2ee"
os.makedirs(output_dir, exist_ok=True)

# Tạo các file .apkg, mỗi file chứa 10 từ
for i in range(0, len(terms), 10):
    deck_id = 160000 + i
    deck_title = f"Jakarta EE Vocabulary Part {i//10 + 1}"
    deck = genanki.Deck(deck_id, deck_title)
    model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Term'},
            {'name': 'Definition'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Term}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Definition}}',
            },
        ])

    for term, definition in terms[i:i+10]:
        note = genanki.Note(model=model, fields=[term, definition])
        deck.add_note(note)

    package = genanki.Package(deck)
    package.write_to_file(os.path.join(output_dir, f"j2ee_part_{i//10 + 1}.apkg"))

output_dir
