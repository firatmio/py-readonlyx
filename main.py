"""
Örnek kullanım ve testler için main.py dosyası
"""

from py_readonlyx import readonly, ReadOnlyError


class User:
    def __init__(self, name="Fırat", age=25):
        self._name = name
        self._age = age
        self._email = f"{name.lower()}@example.com"

    @readonly
    def name(self):
        """Kullanıcının adı (sadece okunabilir)"""
        return self._name

    @readonly
    def age(self):
        """Kullanıcının yaşı (sadece okunabilir)"""
        return self._age

    @readonly
    def email(self):
        """Kullanıcının email'i (sadece okunabilir)"""
        return self._email

    @property
    def status(self):
        return getattr(self, '_status', 'active')
    
    @status.setter
    def status(self, value):
        self._status = value


def test_readonly_properties():
    """Read-only özelliklerini test eder"""
    print("=== READ-ONLY PROPERTY TESTLERİ ===\n")
    
    user = User("Fırat", 30)
    
    print("✅ Okuma işlemleri:")
    print(f"user.name = {user.name}")
    print(f"user.age = {user.age}")
    print(f"user.email = {user.email}")
    print()
    
    print("✅ Normal property değiştirme:")
    user.status = "inactive"
    print(f"user.status = {user.status}")
    print()
    
    print("❌ Read-only property değiştirme testleri:")
    
    test_cases = [
        ("user.name = 'Ahmet'", lambda: setattr(user, 'name', 'Ahmet')),
        ("user.age = 35", lambda: setattr(user, 'age', 35)),
        ("user.email = 'yeni@email.com'", lambda: setattr(user, 'email', 'yeni@email.com')),
    ]
    
    for description, test_func in test_cases:
        try:
            test_func()
            print(f"  {description} → ❌ HATA: Exception fırlatılmadı!")
        except ReadOnlyError as e:
            print(f"  {description} → ✅ ReadOnlyError: {e}")
        except Exception as e:
            print(f"  {description} → ⚠️  Beklenmeyen hata: {e}")
    
    print()
    
    print("❌ Read-only property silme testleri:")
    
    delete_cases = [
        ("del user.name", lambda: delattr(user, 'name')),
        ("del user.age", lambda: delattr(user, 'age')),
    ]
    
    for description, test_func in delete_cases:
        try:
            test_func()
            print(f"  {description} → ❌ HATA: Exception fırlatılmadı!")
        except ReadOnlyError as e:
            print(f"  {description} → ✅ ReadOnlyError: {e}")
        except Exception as e:
            print(f"  {description} → ⚠️  Beklenmeyen hata: {e}")


def test_multiple_instances():
    """Birden fazla instance ile test"""
    print("\n=== MULTIPLE INSTANCE TESTİ ===\n")
    
    user1 = User("Ahmet", 25)
    user2 = User("Mehmet", 30)
    
    print("✅ Farklı instance'lar:")
    print(f"user1.name = {user1.name}, user1.age = {user1.age}")
    print(f"user2.name = {user2.name}, user2.age = {user2.age}")
    
    try:
        user1.name = "Değiştirildi"
        print("❌ HATA: user1.name değiştirilebildi!")
    except ReadOnlyError:
        print("✅ user1.name read-only korundu")
    
    try:
        user2.age = 99
        print("❌ HATA: user2.age değiştirilebildi!")
    except ReadOnlyError:
        print("✅ user2.age read-only korundu")


if __name__ == "__main__":
    test_readonly_properties()
    test_multiple_instances()
    
    print("\n=== SON KONTROL ===")
    user = User()
    print(f"Final durumu - user.name: {user.name}, user.age: {user.age}")
    print("\n🎉 Tüm testler tamamlandı!")