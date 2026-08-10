# Yandex Disk → Avito ImageUrls

## Канонический URL (длинный — предпочтителен)

```
https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/{relpath}
```

Примеры:

```
https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/kuhni/heroes/al-k2-1000.jpg
https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/kuhni/sets/set-01-fixcena/02-angle.jpg
```

- Корень по умолчанию: **`/AUTOZA/Foto_mebel_1`** (проект Foto_mebel_1).
- Старый корень `/AUTOZA/Foto_mebel` — только если пользователь явно указал.
- `{relpath}` — только ASCII (без кириллицы и пробелов).
- В браузере ссылка может отдать `Unauthorized` — это нормально (техническая ссылка для автозагрузки).

## Короткая форма (не дефолт)

```
yandex_disk://AUTOZA/Foto_mebel_1/kuhni/heroes/al-k2-1000.jpg
```

Инструкция Авито допускает обе формы. В этом скилле **всегда писать длинную**, если пользователь не попросил иначе («более длинная ссылка лучше работает»).

## Ячейка Excel

- Колонка: `ImageUrls` / `Ссылки на фото`
- Разделитель: ` | ` (пробел, пайп, пробел)
- Число URL: **4** (пайплайн сетов) или до **10**
- **`ImageNames` / «Названия фото» — оставлять пустыми** при заполнении URL (инструкция Авито)

## Переименование папок RU → EN

| Было (RU) | Стало (EN) |
|-----------|------------|
| kuhni | `kuhni` |
| Шкафы | `wardrobes` |
| Прихожие | `hallways` |
| ТВ-зоны | `tv-zones` |
| Egger мебель | `egger-furniture` |
| Шпон мебель | `veneer-furniture` |
| Стелажи, книжные полки | `shelves` |

Новые папки сразу: `lowercase-with-hyphens`.  
Внутри категории: `sets/set-NN-slug/`, `heroes/{Id}.jpg`.

## Смысловой маппинг категория → папка

| Лист / товар | Папка |
|--------------|--------|
| Кухонные гарнитуры / кухни | `kuhni` |
| Шкафы и буфеты / купе | `wardrobes` |
| Прихожие | `hallways` |
| ТВ-зоны / стенки | `tv-zones` |
| Стеллажи / полки | `shelves` |

Правило: **по смыслам** — не класть кухни в `wardrobes`.

## Разные первые фото

- Lead = **`{kind}/heroes/{Id}.jpg`** (уникальный файл на объявление) — целевой способ.
- Fallback без heroes: цикл/shuffle по файлам папки; **запрещено** один `1.jpg` первым у всех.

## Что не трогать

- Объявления со статусом **Активно** из старого экспорта
- Строки без маркера «новое», если пользователь так сказал
- Фото услуг без явного запроса

## Синхронизация

Локальный проект ↔ Диск:

`…/Foto_mebel_1/kuhni/...` → `/AUTOZA/Foto_mebel_1/kuhni/...`  
`…/Foto_mebel_1/wardrobes/...` → `/AUTOZA/Foto_mebel_1/wardrobes/...`

Яндекс.Диск должен быть **привязан** в настройках автозагрузки профиля Авито.

## Проверка

```text
- URL начинаются с https://cloud-api.yandex.net/v1/disk/resources/download?path=
- path содержит /AUTOZA/Foto_mebel_1/ (или согласованный корень)
- path без кириллицы
- ImageNames пусто на обновлённых строках
- число URL = 4 или 10 (как договорились)
- Counter(first_filename) ≈ числу объявлений (heroes), не 1 ключ на категорию
```

Валидатор: `scripts/validate_image_urls.py --expect 4`
