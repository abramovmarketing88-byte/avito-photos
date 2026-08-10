# Примеры

## Пример 1 — режим C (2000 объявлений, Foto_mebel_1)

**Вход:** `основной-aliris-2000.xlsx`, 1000 кухонь + 1000 шкафов-купе; 10 сетов × 4 кадра на категорию.

**Действия:**
1. Бэкап Excel.
2. Для каждой новой строки: сет по кругу, hero с Title в `kuhni/heroes/{Id}.jpg` или `wardrobes/heroes/{Id}.jpg`.
3. ImageUrls = 4 длинных URL; ImageNames пусто.
4. Синхрон на `/AUTOZA/Foto_mebel_1/...`.

**Ячейка (фрагмент):**

```text
https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/kuhni/heroes/al-k2-1000.jpg | https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/kuhni/sets/set-01-fixcena/02-angle.jpg | https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/kuhni/sets/set-01-fixcena/03-detail.jpg | https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/kuhni/sets/set-01-fixcena/04-fomo.jpg
```

**Обложка:** тёмная плашка внизу safe-zone, крупно «Кухня маленькая Елена на заказ», ниже «Фикс. цена в договоре».

## Пример 2 — только ссылки (режим A, legacy-папка)

**Вход:** 1000 кухонь, плоская папка `kuhni/*.jpg` без heroes.

**Действия:** цикл lead по файлам + 9 других; корень path согласовать с пользователем.

```text
https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/kuhni/78.jpg | ... (всего до 10)
```

## Пример 3 — оверлей CTR (режим B1)

**ЦА:** семья в новостройке, боится скрытых доплат  
**Title из Excel:** «Угловая кухня на заказ без доплат»  
**Кадр:** 1920×1440 4:3; хук целиком в safe-zone 1300×1300

**Оверлей:**
- Хук: Title / «Цена в договоре»
- Выгода: «Без скрытых доплат»
- Плашка 10–25% площади, фасады читаемы
- Нельзя: «АКЦИЯ», телефон, watermark

Сохранить: `kuhni/heroes/{Id}.jpg` или `sets/.../01-hero.jpg`.

## Пример 4 — генерация 4:3 (режим B2)

**Промпт:** matte anthracite handleless kitchen, oak worktop, LED under cabinets, herringbone floor, photoreal, horizontal 4:3, 1920x1440, no watermark no logo, leave lower center for text

Сохранить как `raw-01-hero.jpg` в сет → штамп heroes в режиме C.
