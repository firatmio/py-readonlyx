<div align="center">

# 🚀 py-readonlyx

**Lightweight Python Read-Only Property Decorator**

*Periyodik görevlerinizi kolayca yönetin - Sıfır bağımlılık, maksimum performans*

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-ZERO-orange.svg)
![Threading](https://img.shields.io/badge/threading-SUPPORTED-brightgreen.svg)

[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](https://github.com/yourusername/py-readonlyx)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue)](https://github.com/yourusername/py-readonlyx)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)](https://github.com/yourusername/py-readonlyx)

</div>

---

## 📖 Genel Bakış

**py-readonlyx**, Python sınıflarında read-only (salt okunur) property'ler oluşturmak için tasarlanmış minimal ve yüksek performanslı bir decorator kütüphanesidir. Sadece **tek bir decorator** ile property'lerinizi değiştirilemez hale getirebilirsiniz.

## 🎯 Neden py-readonlyx?

### 🆚 Diğer Çözümlerle Karşılaştırma

| Özellik | py-readonlyx | Manuel Property | dataclasses.frozen | attrs.frozen |
|---------|--------------|-----------------|-------------------|--------------|
| **Basitlik** | ✅ Tek decorator | ❌ Çok kod | ⚠️ Sınıf seviyesi | ⚠️ Bağımlılık |
| **Performans** | ✅ Yüksek | ✅ Yüksek | ⚠️ Orta | ⚠️ Orta |
| **Bağımlılık** | ✅ Sıfır | ✅ Sıfır | ✅ Stdlib | ❌ Dış paket |
| **Seçici Control** | ✅ Property bazlı | ✅ Property bazlı | ❌ Tüm sınıf | ❌ Tüm sınıf |
| **Mutable Fields** | ✅ Destekler | ✅ Destekler | ❌ Desteklemez | ❌ Desteklemez |

### 💡 Neden Bu Kütüphaneyi Seçmelisiniz?

- **🏃‍♂️ Sıfır Öğrenme Eğrisi**: Sadece `@readonly` ekleyin, hazır!
- **⚡ Yüksek Performans**: Native Python property'lerinin performansı
- **🪶 Sıfır Bağımlılık**: Harici paket gerektirmez
- **🎛️ Granüler Kontrol**: Sadece istediğiniz property'leri readonly yapın
- **🔄 Karma Kullanım**: Aynı sınıfta readonly ve normal property'ler
- **🧵 Thread-Safe**: Çoklu thread ortamlarında güvenli
- **📦 Minimal Footprint**: Toplam ~50 satır kod

## 🚀 Hızlı Başlangıç

### Kurulum

```bash
# Bu projeyi klonlayın
git clone https://github.com/yourusername/py-readonlyx.git
cd py-readonlyx

# Python path'inize ekleyin veya doğrudan import edin
```

### Temel Kullanım

```python
from py_readonlyx import readonly, ReadOnlyError

class User:
    def __init__(self, name="Fırat", age=25):
        self._name = name
        self._age = age
        self._status = "active"  # Bu değiştirilebilir

    @readonly
    def name(self):
        """Kullanıcı adı - salt okunur"""
        return self._name

    @readonly  
    def age(self):
        """Kullanıcı yaşı - salt okunur"""
        return self._age

    # Normal property - değiştirilebilir
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self._status = value

# Kullanım
user = User("Ahmet", 30)

# ✅ Okuma işlemleri
print(user.name)    # "Ahmet"
print(user.age)     # 30

# ✅ Normal property değişikliği  
user.status = "inactive"  # Çalışır

# ❌ Read-only property değişikliği
user.name = "Mehmet"     # ReadOnlyError
user.age = 35            # ReadOnlyError
del user.name            # ReadOnlyError
```

## 🛠️ Gelişmiş Kullanım

### API Referansı

#### `@readonly` Decorator

Property'yi salt okunur hale getirir.

```python
@readonly
def property_name(self):
    return self._value
```

#### `ReadOnlyError` Exception

Read-only property'ye yazma/silme girişiminde fırlatılır.

```python
try:
    user.readonly_prop = "new_value"
except ReadOnlyError as e:
    print(f"Hata: {e}")
    # "Cannot set read-only property 'readonly_prop'"
```

### Kullanım Senaryoları

#### 1. Immutable Model Classes
```python
class Point:
    def __init__(self, x, y):
        self._x, self._y = x, y
    
    @readonly
    def x(self): return self._x
    
    @readonly  
    def y(self): return self._y
```

#### 2. Configuration Objects
```python
class Config:
    def __init__(self, api_key, database_url):
        self._api_key = api_key
        self._database_url = database_url
    
    @readonly
    def api_key(self): return self._api_key
    
    @readonly
    def database_url(self): return self._database_url
```

#### 3. Computed Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self): return self._radius
    
    @radius.setter  
    def radius(self, value): self._radius = value
    
    @readonly
    def area(self): return 3.14159 * self._radius ** 2
    
    @readonly
    def circumference(self): return 2 * 3.14159 * self._radius
```

## 🧪 Test Etme

```bash
# Test suite'i çalıştır
python main.py

# Beklenen çıktı:
# ✅ Tüm read-only testleri geçti
# ✅ Multiple instance desteği çalışıyor  
# ✅ Exception handling doğru
```

## 📊 Performans

```python
import timeit

# py-readonlyx (@readonly)
def test_readonly():
    return user.readonly_prop

# Manuel property
def test_manual():
    return user.manual_prop

# Her ikisi de ~aynı performans (native property hızı)
```

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📄 Lisans

Apache 2.0 License - Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🏷️ Versiyon Geçmişi

- **v1.0.0** - İlk kararlı sürüm
  - `@readonly` decorator
  - `ReadOnlyError` exception
  - Tam test coverage

---

<div align="center">

**⭐ Beğendiyseniz yıldız vermeyi unutmayın!**</br>
**Created by ❤️ [firatmio](https://github.com/firatmio)**

</div>
