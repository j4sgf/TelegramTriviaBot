import sqlite3

def setup_database():
    """Buat database dan isi dengan contoh pertanyaan serta jawaban."""
    conn = sqlite3.connect("family100.db")
    cursor = conn.cursor()

    # Drop existing tables if they exist
    cursor.execute("DROP TABLE IF EXISTS answers")
    cursor.execute("DROP TABLE IF EXISTS questions")

    # Buat tabel
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id INTEGER NOT NULL,
        answer TEXT NOT NULL,
        points INTEGER NOT NULL,
        FOREIGN KEY (question_id) REFERENCES questions(id)
    )
    """)

    # Contoh data
    questions = [
    ("Sebutkan sesuatu yang ada di dapur.",),  # Question 1
    ("Sebutkan sesuatu yang bisa ditemukan di sekolah.",),  # Question 2
    ("Sebutkan sesuatu yang ada di dompet.",),  # Question 3
    ("Sebutkan sesuatu yang ditemukan di kamar mandi.",),  # Question 4
    ("Sebutkan jenis kendaraan.",),  # Question 5
    ("Sebutkan sesuatu yang dilakukan sebelum tidur.",),  # Question 6
    ("Sebutkan sesuatu yang dilakukan saat hujan.",),  # Question 7
    ("Sebutkan sesuatu yang ada di meja kerja.",),  # Question 8
    ("Sebutkan nama buah tropis.",),  # Question 9
    ("Sebutkan sesuatu yang bisa dimakan saat sarapan.",),  # Question 10
    ("Sebutkan warna bendera nasional.",),  # Question 11
    ("Sebutkan nama binatang peliharaan.",),  # Question 12
    ("Sebutkan nama profesi.",),  # Question 13
    ("Sebutkan sesuatu yang ditemukan di taman.",),  # Question 14
    ("Sebutkan nama kota di Indonesia.",),  # Question 15
    ("Sebutkan sesuatu yang dilakukan saat liburan.",),  # Question 16
    ("Sebutkan nama hewan di kebun binatang.",),  # Question 17
    ("Sebutkan sesuatu yang dilakukan di pagi hari.",),  # Question 18
    ]

    # Jawaban untuk setiap pertanyaan
    answers = [
        (1, "Pisau", 30), (1, "Sendok", 20), (1, "Piring", 15), (1, "Kompor", 10), (1, "Kulkas", 25),
        (2, "Papan Tulis", 30), (2, "Kursi", 25), (2, "Buku", 20), (2, "Guru", 15), (2, "Meja", 10),
        (3, "Uang", 40), (3, "KTP", 30), (3, "Kartu Kredit", 20), (3, "Foto", 10),
        (4, "Sabun", 30), (4, "Sikat Gigi", 25), (4, "Shampo", 20), (4, "Handuk", 15), (4, "Toilet", 10),
        (5, "Mobil", 40), (5, "Motor", 30), (5, "Sepeda", 20), (5, "Bus", 10),
        (6, "Menggosok Gigi", 30), (6, "Mencuci Muka", 20), (6, "Berdoa", 15), (6, "Mengecek HP", 10), (6, "Membaca Buku", 5),
        (7, "Memakai Payung", 30), (7, "Menyalakan Wiper", 25), (7, "Berlari", 20), (7, "Berteduh", 15), (7, "Mengeluh", 10),
        (8, "Komputer", 40), (8, "Pulpen", 30), (8, "Kertas", 20), (8, "Telepon", 10),
        (9, "Mangga", 30), (9, "Pisang", 25), (9, "Durian", 20), (9, "Nanas", 15), (9, "Rambutan", 10),
        (10, "Roti", 30), (10, "Nasi Goreng", 25), (10, "Telur", 20), (10, "Bubur", 15), (10, "Sereal", 10),
        (11, "Merah", 50), (11, "Putih", 50),
        (12, "Kucing", 40), (12, "Anjing", 30), (12, "Ikan", 20), (12, "Burung", 10),
        (13, "Dokter", 40), (13, "Guru", 30), (13, "Insinyur", 20), (13, "Polisi", 10),
        (14, "Bunga", 40), (14, "Bangku", 30), (14, "Rumput", 20), (14, "Ayunan", 10),
        (15, "Jakarta", 40), (15, "Surabaya", 30), (15, "Bandung", 20), (15, "Yogyakarta", 10),
        (16, "Berenang", 30), (16, "Pergi ke Pantai", 25), (16, "Berbelanja", 20), (16, "Bersantai", 15), (16, "Memotret", 10),
        (17, "Singa", 30), (17, "Gajah", 25), (17, "Zebra", 20), (17, "Jerapah", 15), (17, "Monyet", 10),
        (18, "Olahraga", 30), (18, "Sarapan", 25), (18, "Mandi", 20), (18, "Berangkat Kerja", 15), (18, "Membuat Kopi", 10),
    ]

    # Masukkan data contoh
    cursor.executemany("INSERT INTO questions (question) VALUES (?)", questions)
    cursor.executemany("INSERT INTO answers (question_id, answer, points) VALUES (?, ?, ?)", answers)

    conn.commit()
    conn.close()
    print("Database berhasil dibuat dan diisi dengan pertanyaan serta jawaban!")
    


def get_family100_question():
    """Ambil pertanyaan acak dan jawabannya dari database."""
    conn = sqlite3.connect("family100.db")
    cursor = conn.cursor()

    # Ambil satu pertanyaan acak
    cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 1")
    question = cursor.fetchone()
    if not question:
        return None

    # Ambil semua jawaban untuk pertanyaan tersebut
    cursor.execute("SELECT answer, points FROM answers WHERE question_id = ?", (question[0],))
    answers = cursor.fetchall()

    conn.close()

    return {
        "id": question[0],
        "question": question[1],
        "answers": {answer[0].lower(): answer[1] for answer in answers}  # Normalisasi jawaban ke huruf kecil
    }
