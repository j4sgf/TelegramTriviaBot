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

    # Create the scores table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        points INTEGER DEFAULT 0
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
    ("Sebutkan jenis olahraga.",),  # Question 19
    ("Sebutkan sesuatu yang bisa ditemukan di rumah.",),  # Question 20
    ("Sebutkan makanan yang biasa dimakan saat makan malam.",),  # Question 21
    ("Sebutkan benda yang ada di kantor.",),  # Question 22
    ("Sebutkan aktivitas yang bisa dilakukan di akhir pekan.",),  # Question 23
    ("Sebutkan jenis musik.",),  # Question 24
    ("Sebutkan tempat yang ada di mall.",),  # Question 25
    ("Sebutkan jenis bunga.",),  # Question 26
    ("Sebutkan sesuatu yang ada di taman bermain.",),  # Question 27
    ("Sebutkan makanan ringan yang sering dimakan.",),  # Question 28
    ("Sebutkan barang yang biasa dibawa saat pergi ke luar rumah.",),  # Question 29
    ("Sebutkan jenis pakaian yang biasa dipakai saat musim dingin.",),  # Question 30
    ("Sebutkan nama pulau di Indonesia.",),  # Question 31
    ("Sebutkan nama makanan khas Indonesia.",),  # Question 32
    ("Sebutkan nama lagu kebangsaan Indonesia.",),  # Question 33
    ("Sebutkan nama pahlawan nasional Indonesia.",),  # Question 34
    ("Sebutkan nama gunung tertinggi di Indonesia.",),  # Question 35
    ("Sebutkan nama tari tradisional Indonesia.",),  # Question 36
    ("Sebutkan nama bahasa daerah di Indonesia.",),  # Question 37
    ("Sebutkan nama tradisi atau upacara adat di Indonesia.",),  # Question 38
    ("Sebutkan nama danau terbesar di Indonesia.",),  # Question 39
    ("Sebutkan nama sungai terpanjang di Indonesia.",),  # Question 40
    ("Sebutkan nama film Hollywood terkenal.",),  # Question 41
    ("Sebutkan nama artis internasional terkenal.",),  # Question 42
    ("Sebutkan judul lagu populer saat ini.",),  # Question 43
    ("Sebutkan nama superhero terkenal.",),  # Question 44
    ("Sebutkan nama film animasi terkenal.",),  # Question 45
    ("Sebutkan nama seri TV populer.",),  # Question 46
    ("Sebutkan nama grup musik terkenal.",),  # Question 47
    ("Sebutkan nama video game terkenal.",),  # Question 48
    ("Sebutkan aplikasi media sosial populer.",),  # Question 49
    ("Sebutkan nama model atau influencer terkenal.",),  # Question 50
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
        (19, "Sepak Bola", 30), (19, "Basket", 25), (19, "Bulu Tangkis", 20), (19, "Renang", 15), (19, "Lari", 10),
        (20, "Sofa", 30), (20, "Meja", 25), (20, "Lampu", 20), (20, "Karpet", 15), (20, "AC", 10),
        (21, "Paket Nasi", 30), (21, "Mie Goreng", 25), (21, "Ayam Penyet", 20), (21, "Sate", 15), (21, "Sup", 10),
        (22, "Komputer", 40), (22, "Meja", 30), (22, "Printer", 20), (22, "Telepon", 10),
        (23, "Makan di Restoran", 30), (23, "Berkemah", 25), (23, "Menonton Film", 20), (23, "Bersepeda", 15), (23, "Jalan-jalan", 10),
        (24, "Pop", 30), (24, "Rock", 25), (24, "Jazz", 20), (24, "Klasik", 15), (24, "Reggae", 10),
        (25, "Restoran", 30), (25, "Toko", 25), (25, "Bioskop", 20), (25, "Supermarket", 15), (25, "ATM", 10),
        (26, "Mawar", 30), (26, "Anggrek", 25), (26, "Tulip", 20), (26, "Melati", 15), (26, "Lily", 10),
        (27, "Ayunan", 30), (27, "Perosotan", 25), (27, "Bangku", 20), (27, "Rumput", 15), (27, "Bola", 10),
        (28, "Keripik", 30), (28, "Kue Cubit", 25), (28, "Kacang", 20), (28, "Popcorn", 15), (28, "Es Krim", 10),
        (29, "Dompet", 30), (29, "Handphone", 25), (29, "Kunci", 20), (29, "Topi", 15), (29, "Payung", 10),
        (30, "Jaket", 30), (30, "Syal", 25), (30, "Sarung Tangan", 20), (30, "Sepatu Boot", 15), (30, "Kaos Kaki", 10),
        (31, "Sumatra", 30), (31, "Jawa", 25), (31, "Kalimantan", 20), (31, "Sulawesi", 15), (31, "Papua", 10),
        (32, "Nasi Goreng", 30), (32, "Sate", 25), (32, "Rendang", 20), (32, "Gado-Gado", 15), (32, "Soto", 10),
        (33, "Indonesia Raya", 50),
        (34, "Soekarno", 30), (34, "Hatta", 25), (34, "Diponegoro", 20), (34, "Kartini", 15), (34, "Bung Tomo", 10),
        (35, "Puncak Jaya", 30), (35, "Gunung Kerinci", 25), (35, "Gunung Rinjani", 20), (35, "Gunung Semeru", 15),
        (36, "Tari Pendet", 30), (36, "Tari Kecak", 25), (36, "Tari Saman", 20), (36, "Tari Reog", 15),
        (37, "Jawa", 30), (37, "Sunda", 25), (37, "Bali", 20), (37, "Batak", 15), (37, "Bugis", 10),
        (38, "Upacara Nyepi", 30), (38, "Upacara Lebaran", 25), (38, "Upacara Sekaten", 20), (38, "Upacara Galungan", 15),
        (39, "Danau Toba", 30), (39, "Danau Singkarak", 25), (39, "Danau Rawa Pening", 20), (39, "Danau Sentani", 15),
        (40, "Sungai Kapuas", 30), (40, "Sungai Mahakam", 25), (40, "Sungai Musi", 20), (40, "Sungai Barito", 15),
        (41, "Avengers: Endgame", 40), (41, "Titanic", 30), (41, "The Dark Knight", 25), (41, "Avatar", 20), (41, "Inception", 10),
        (42, "Taylor Swift", 40), (42, "Ariana Grande", 30), (42, "Beyoncé", 25), (42, "Chris Hemsworth", 20), (42, "Tom Hanks", 10),
        (43, "Bad Bunny - Vete", 30), (43, "Shakira - Hips Don't Lie", 25), (43, "Blinding Lights - The Weeknd", 20), (43, "Levitating - Dua Lipa", 15), (43, "Shape of You - Ed Sheeran", 10),
        (44, "Iron Man", 40), (44, "Spider-Man", 30), (44, "Batman", 25), (44, "Superman", 20), (44, "Wonder Woman", 10),
        (45, "Frozen", 30), (45, "Toy Story", 25), (45, "The Lion King", 20), (45, "Shrek", 15), (45, "Finding Nemo", 10),
        (46, "Stranger Things", 30), (46, "Game of Thrones", 25), (46, "Breaking Bad", 20), (46, "The Mandalorian", 15), (46, "Friends", 10),
        (47, "BTS", 40), (47, "Blackpink", 30), (47, "The Beatles", 25), (47, "One Direction", 20), (47, "Maroon 5", 10),
        (48, "Minecraft", 40), (48, "Fortnite", 30), (48, "Among Us", 25), (48, "PUBG", 20), (48, "Call of Duty", 10),
        (49, "Instagram", 40), (49, "TikTok", 30), (49, "Twitter", 25), (49, "Facebook", 20), (49, "Snapchat", 10),
        (50, "Kendall Jenner", 30), (50, "Gigi Hadid", 25), (50, "Chiara Ferragni", 20), (50, "Zoe Sugg", 15), (50, "James Charles", 10),

    ]

    # Masukkan data contoh
    cursor.executemany("INSERT INTO questions (question) VALUES (?)", questions)
    cursor.executemany("INSERT INTO answers (question_id, answer, points) VALUES (?, ?, ?)", answers)

    conn.commit()
    conn.close()
    print("Database berhasil dibuat dan diisi dengan pertanyaan serta jawaban!")
    

def update_score(user_id: int, username: str, points: int):
    conn = sqlite3.connect("family100.db")
    cursor = conn.cursor()

    # Insert or update the user's score
    cursor.execute("""
    INSERT INTO scores (user_id, username, points)
    VALUES (?, ?, ?)
    ON CONFLICT(user_id) DO UPDATE SET
    points = points + ?
    """, (user_id, username, points, points))

    conn.commit()
    conn.close()


def get_rankings():
    conn = sqlite3.connect("family100.db")
    cursor = conn.cursor()

    # Retrieve scores in descending order
    cursor.execute("SELECT username, points FROM scores ORDER BY points DESC")
    rankings = cursor.fetchall()

    conn.close()
    return rankings


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
