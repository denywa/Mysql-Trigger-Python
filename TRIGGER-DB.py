import mysql.connector

# Koneksi ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="trigger"
)
cursor = conn.cursor()

# Membuat Database
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mahasiswa (
        NIM INT PRIMARY KEY,
        Nama VARCHAR(100),
        Nilai INT,
        Grade CHAR(2)
    )
""")
print("Table Created")

# Membuat Trigger Before Insert
cursor.execute("""
    CREATE TRIGGER before_insert_mahasiswa
    BEFORE INSERT ON mahasiswa
    FOR EACH ROW
    BEGIN
        SET NEW.Grade = (CASE
            WHEN NEW.Nilai >= 90 THEN 'A'
            WHEN NEW.Nilai >= 85 THEN 'A-'
            WHEN NEW.Nilai >= 80 THEN 'B+'
            WHEN NEW.Nilai >= 75 THEN 'B'
            WHEN NEW.Nilai >= 70 THEN 'B-'
            WHEN NEW.Nilai >= 60 THEN 'C+'
            WHEN NEW.Nilai >= 55 THEN 'C'
            WHEN NEW.Nilai >= 45 THEN 'D'
            ELSE 'E'
        END);
    END;
""")

print("Trigger before insert created")

# Membuat Trigger Before Update
cursor.execute("""
    CREATE TRIGGER before_update_mahasiswa
    BEFORE UPDATE ON mahasiswa
    FOR EACH ROW
    BEGIN
        SET NEW.Grade = (CASE
            WHEN NEW.Nilai >= 90 THEN 'A'
            WHEN NEW.Nilai >= 85 THEN 'A-'
            WHEN NEW.Nilai >= 80 THEN 'B+'
            WHEN NEW.Nilai >= 75 THEN 'B'
            WHEN NEW.Nilai >= 70 THEN 'B-'
            WHEN NEW.Nilai >= 60 THEN 'C+'
            WHEN NEW.Nilai >= 55 THEN 'C'
            WHEN NEW.Nilai >= 45 THEN 'D'
            ELSE 'E'
        END);
    END;
""")
print("Trigger before update created")

cursor.execute("""
    INSERT INTO mahasiswa (NIM, Nama, Nilai)
    VALUES (1, 'DENY', 90),
           (2, 'TES', 90);
""")

cursor.execute("""
    UPDATE mahasiswa SET Nilai = 70 WHERE NIM = 2;
""")
conn.commit()
# Menutup koneksi
if conn.is_connected():
    cursor.close()
    conn.close()


