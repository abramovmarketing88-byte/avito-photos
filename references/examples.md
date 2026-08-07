# Примеры

## Пример 1 — только ссылки (режим A)

**Вход:** Excel автозагрузки, 1000 кухонь, папка `kuhni/` с 96 jpg.

**Действия:**
1. Не трогать строки со старым AvitoId / статусом Активно (если есть).
2. Для `msk2026-kuh-*` проставить 10 URL из `kuhni`.
3. Первые файлы: цикл по 96 кадрам → ~10–11 объявлений на каждый lead.

**Ячейка:**

```text
https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel/kuhni/78.jpg | https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel/kuhni/16.jpg | ... (всего 10)
```

## Пример 2 — оверлей CTR (режим B1)

**ЦА:** семья в новостройке, боится скрытых доплат  
**Заголовок:** «Угловая кухня на заказ без доплат»  
**Кадр:** 1920×1440 4:3; хук целиком в safe-zone 1300×1300

**Оверлей:**
- Хук: «Цена в договоре»
- Выгода: «Без скрытых доплат»
- Плашка снизу ≤ ~10% площади, фасады не перекрыты
- Нельзя: «АКЦИЯ», телефон, watermark

Сохранить: `kuhni/gen-no-dopplat-01.jpg` → URL в автозагрузку.

## Пример 3 — генерация 4:3 (режим B2)

**Промпт:** matte anthracite handleless kitchen, oak worktop, LED under cabinets, herringbone floor, photoreal, horizontal 4:3, 1920x1440, no watermark no logo

Сохранить в `kuhni/`, ротировать как lead, не ставить первым у всех подряд.
