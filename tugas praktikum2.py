import random  # Mengimpor modul random untuk menghasilkan angka acak

# Kelas Robot
class Robot:
    def __init__(self, name, hp, attack, accuracy):
        """
        Konstruktor kelas Robot untuk menginisialisasi objek robot.

        :param name: Nama robot
        :param hp: Jumlah HP (Health Points) robot
        :param attack: Kekuatan serangan robot
        :param accuracy: Akurasi serangan dalam persentase (1-100)
        """
        self.name = name
        self.hp = hp
        self.attack = attack
        self.accuracy = accuracy  # Persentase kemungkinan serangan mengenai target

    # Metode untuk menyerang musuh
    def attack_enemy(self, enemy):
        """
        Metode untuk menyerang robot lawan. Serangan memiliki peluang untuk meleset
        tergantung pada nilai akurasi robot.

        :param enemy: Robot lawan yang akan diserang
        """
        hit_chance = random.randint(1, 100)  # Menghasilkan angka acak antara 1 hingga 100
        if hit_chance <= self.accuracy:  # Jika angka yang dihasilkan dalam batas akurasi, serangan berhasil
            damage = self.attack  # Damage yang diberikan sebesar nilai attack robot
            enemy.hp -= damage  # Mengurangi HP lawan sesuai damage yang diberikan
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} gagal menyerang!")  # Jika serangan meleset

    # Metode untuk melakukan regenerasi HP
    def regen_health(self):
        """
        Metode untuk memulihkan HP secara acak antara 10 hingga 30 poin.
        """
        regen = random.randint(10, 30)  # Menghasilkan jumlah HP yang diregenerasi secara acak
        self.hp += regen  # Menambah HP robot
        print(f"{self.name} melakukan regenerasi dan mendapat {regen} HP!")

# Kelas Game
class Game:
    def __init__(self, robot1, robot2):
        """
        Konstruktor kelas Game untuk menginisialisasi permainan.

        :param robot1: Robot pertama dalam permainan
        :param robot2: Robot kedua dalam permainan
        """
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1  # Menandakan ronde keberapa permainan berlangsung

    # Menampilkan status robot
    def print_status(self):
        """
        Metode untuk mencetak status HP dan attack kedua robot di setiap ronde.
        """
        print(f"Round-{self.round} ======================================================")
        print(f"{self.robot1.name} [{self.robot1.hp}|{self.robot1.attack}]")
        print(f"{self.robot2.name} [{self.robot2.hp}|{self.robot2.attack}]")

    # Memulai pertarungan
    def start_game(self):
        """
        Metode utama untuk menjalankan permainan hingga salah satu robot kalah
        atau menyerah.
        """
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            self.print_status()  # Menampilkan status robot

            # Pilihan aksi untuk robot1
            print(f"\n1. Attack     2. Defense     3. Giveup")
            action1 = int(input(f"{self.robot1.name}, pilih aksi: "))
            if action1 == 1:
                self.robot1.attack_enemy(self.robot2)  # Robot1 menyerang robot2
            elif action1 == 2:
                self.robot1.regen_health()  # Robot1 melakukan regenerasi HP
            elif action1 == 3:
                print(f"{self.robot1.name} menyerah!")  # Jika robot1 menyerah
                print(f"{self.robot2.name} menang!")
                break

            if self.robot2.hp <= 0:  # Jika HP robot2 habis, robot1 menang
                print(f"{self.robot1.name} menang!")
                break

            # Pilihan aksi untuk robot2
            print(f"\n1. Attack     2. Defense     3. Giveup")
            action2 = int(input(f"{self.robot2.name}, pilih aksi: "))
            if action2 == 1:
                self.robot2.attack_enemy(self.robot1)  # Robot2 menyerang robot1
            elif action2 == 2:
                self.robot2.regen_health()  # Robot2 melakukan regenerasi HP
            elif action2 == 3:
                print(f"{self.robot2.name} menyerah!")  # Jika robot2 menyerah
                print(f"{self.robot1.name} menang!")
                break

            if self.robot1.hp <= 0:  # Jika HP robot1 habis, robot2 menang
                print(f"{self.robot2.name} menang!")
                break

            self.round += 1  # Menambah jumlah ronde permainan

# Menyiapkan robot dan permainan
robot1 = Robot(name="Atreus", hp=500, attack=50, accuracy=80)  # Membuat robot pertama
robot2 = Robot(name="Daedalus", hp=750, attack=40, accuracy=70)  # Membuat robot kedua

game = Game(robot1, robot2)  # Membuat objek permainan dengan dua robot
game.start_game()  # Memulai permainan
