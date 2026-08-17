# Pre-launch checklist (фото + ImageUrls)

Перед загрузкой xlsx в автозагрузку Авито.

## Диск и файлы

- [ ] Локальная папка зеркалит `DISK_ROOT` на Яндекс.Диске
- [ ] **Синхронизация Диска завершена** (иначе Авито не подтянет новые JPG)
- [ ] `disk_jpgs` ≈ sets + heroes (напр. 15 sets + 300 heroes = 315)
- [ ] Размер кадров **1920×1440**, соотношение **4:3**

## Качество (услуги)

- [ ] Hero и слайды — **живые люди** (лицо эксперта), не PIL-заглушки
- [ ] Хук на hero читается в превью 1:1 на телефоне
- [ ] unique `heroes/{Id}.jpg` ≈ числу объявлений на листе

## Excel

- [ ] ImageUrls: `url1 | url2 | …`; ImageNames пусто
- [ ] Длинные cloud-api URL; path ASCII
- [ ] Активные объявления: ImageUrls **не менялись** (или был явный запрос)
- [ ] Нет лишних листов категорий (аренда, чужие ниши) — см. `avito-factory` этап 7.5
- [ ] Строки **уплотнены** (нет дыр между объявлениями)

## Быстрая проверка (Python)

```python
# ads count, empty ImageUrls, disk jpgs
import pandas as pd
from pathlib import Path

feed = Path("output/feeds/основной-{slug}.xlsx")
disk = Path("{local_disk_mirror}")  # напр. D:/Yandex.Disk/AUTOZA/uslugi
# ... count Title-filled rows, missing ImageUrls, len(list(disk.rglob('*.jpg')))
```

Отчёт: `output/reports/prelaunch-check.json`.

## Смешанные URL

Если в ячейке старые `http://avito.ru/autoload/…` + новые cloud-api — **нормально**, если старые фото сохраняем намеренно. Валидатор `validate_image_urls.py` может не пройти — не блокер для такого фида.
