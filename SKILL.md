---
name: avito-photos
description: >-
  Фото для автозагрузки Авито: ImageUrls (Яндекс.Диск cloud-api) или архив ZIP
  + ImageNames; EN-папки, сеты 10×4 + уникальный hero, CTR-оверлеи 4:3 1920×1440
  (хук+CTA, не полный Title), товары и услуги; премиум арт-дирекшн (смыслы,
  3 обложки, карусель). Use when Авито фото, ImageUrls, ImageNames, архив фото,
  ZIP автозагрузка, Яндекс.Диск, CTR оверлеи, heroes, sets, uslugi, 4:3,
  1920x1440, арт-дирекшн, смыслы, 3 обложки, карусель Авито.
disable-model-invocation: true
---

# Avito Photos

Фото для Авито: **ссылки Яндекс.Диска (ImageUrls)** или **архив ZIP + ImageNames** + **генерация/оверлеи под CTR** с учётом модерации + **премиум арт-дирекшн** (режим E).

Работает с `avito-factory` (тексты/Excel). Этот скилл — только фото (ImageUrls **или** архив/ImageNames).

Перед усилением правил из внешних файлов — сверка: [references/rules-audit.md](references/rules-audit.md).

## Когда применять

- ImageUrls / `Ссылки на фото` в Excel автозагрузки
- ImageNames + ZIP-архив (без папок внутри) вместе с Excel
- RU→EN папки под Яндекс.Диск
- Наборы фото по смыслу категории (сеты + уникальный lead)
- Генерация или продающий текст на кадре (CTR)
- Споры про 4:3, 1920×1440, safe-zone, модерацию оверлеев
- Смыслы креативов / согласование текстов на кадрах
- 3 варианта обложки, единая визуальная система карусели, арт-дирекшн 1–N объявлений

## Выбор режима

| Задача | Режим |
|--------|--------|
| Кадры уже на Диске → только URL в Excel | **A** |
| Генерация / оверлей CTR | **B** → затем C или A |
| Массовый фид 10 сетов × 4 + heroes | **C** (дефолт фида) |
| Услуги: темы × 4–5 слайдов (storyline) | **D** |
| 1 объявление / премиум ≤15 / «3 обложки» / «согласуй смыслы» / арт-дирекшн | **E** |
| Архив ZIP + ImageNames (без Диска / явный запрос) | **F** |

**Не** запускать E с approve на каждую строку массового фида. Массовый Excel / ImageUrls / сеты → A/C/D; E — только по явному запросу или брифу «премиум ≤15».  
**F** не дефолт для массовых фидов (лимит **архив+Excel ≤ 100 МБ**); при Дискe — A/C/D.

Смыслы (массовый auto vs E approve): [references/meaning-strategy.md](references/meaning-strategy.md).  
Визуал / 3 стиля / карусель / identity: [references/creative-direction.md](references/creative-direction.md).

## Жёсткие правила брифа (не отменять)

1. При **ImageUrls**: папка синхронизируется с Яндекс.Диском; Авито к нему подключен в настройках автозагрузки. При режиме **F** Диск не обязателен.
2. **Длинная ссылка (предпочтительна):**
   `https://cloud-api.yandex.net/v1/disk/resources/download?path=/{DISK_ROOT}/{niche}/heroes/{Id}.jpg`
   Короткая `yandex_disk://...` допустима по инструкции Авито, но в пайплайне **не использовать**, если пользователь просит длинную.
3. В ячейке ImageUrls: `url1 | url2 | ...` (пробел-пайп-пробел). При URL **ImageNames не заполнять**.
4. Фото **по смыслу** кластера/категории. Не смешивать нес related в одном сете.
5. Папки и path на Диске — **ASCII/EN** (`sets`, `heroes`, `{niche-slug}`), без кириллицы в path.
6. Уже **активные** объявления — фото/ImageUrls/ImageNames не менять без явного запроса; у **новых** — менять.
7. Первые фото у объявлений **разные** (не один файл lead на всех).
8. Кадры для Авито — **4:3**, целевой размер **1920×1440**.
9. **Архив (режим F):** фото в ZIP **без вложенных папок**; в Excel — **ImageNames** (имя+расширение, ` | ` или перевод строки); ImageUrls пусто; ZIP + Excel **вместе**; сумма ≤ **100 МБ**. Подробно: [references/archive-upload.md](references/archive-upload.md).

### Корень на Диске

**`DISK_ROOT`** — из брифа (напр. `/AUTOZA/Brand_photos`). Локальная папка зеркалит path.

Примеры веток:
- **Товары:** `{niche-a}/`, `{niche-b}/` (отдельные product-кластеры)
- **Услуги:** `uslugi/` или `services/` → [references/services-photos.md](references/services-photos.md)
- **Премиум E (опц.):** `{niche}/premium/{Id}/` или стандартные `heroes/` + slides сета

Подробности URL: [references/yandex-disk-urls.md](references/yandex-disk-urls.md).

## Техстандарт кадра (проверенный)

| Параметр | Значение |
|----------|----------|
| Соотношение | **4:3** горизонталь |
| Целевой размер | **1920×1440** (также ок 1280×960) |
| Мин. качество | 1600×1200 / 1280×960 |
| Формат | JPG (осн.), PNG |
| Вес | ≤25 МБ; цель 0.3–2 МБ |
| Safe-zone текста | центр **1300×1300** — **весь** текстовый блок строго внутри |
| Объект в кадре | **60–80%** (товар виден; текст не перекрывает фасады целиком) |
| Оверлей (плашка+текст) | **10–25%** площади кадра **по композиции** (не «тонкая полоска») |
| Кегль @1920 | hero хук **88–92 px**, выгода **52–56 px**, CTA **48–50 px**; слайды 2–4: **76–88 px** |
| Кол-во в объявлении | **4–10** (дефолт сетов = **4**; добить до 10 при наличии кадров) |

**Мобилка / CTR:** если хук не читается в превью 1:1 на телефоне — оверлей бракованный. Плашка у самого края кадра вне safe-zone — брак.

Обложка = **готовый результат** или сильный оффер; не прайс/коллаж/абстрактная текстура.

**Hero-текст:** короткий **хук** (3–6 слов), не полный Title. CTA третьей строкой. См. [references/overlay-hooks.md](references/overlay-hooks.md).

Подробности: [references/ctr-overlays-4x3.md](references/ctr-overlays-4x3.md).

---

## Режим C — сеты + уникальные heroes (основной для массовых фидов)

Проверенный пайплайн: **10 смысловых сетов × 4 кадра**, затем на объявление — **свой hero** + хвост из сета.

Хуки без approve: search phrase + pain/value по [references/meaning-strategy.md](references/meaning-strategy.md) (не слепой truncate Title).

```
Task Progress:
- [ ] 10 сетов × 4 кадра (EN-папки), 1920×1440
- [ ] Heroes: 1 файл на Id, оверлей из Title (+ USP сета / строки)
- [ ] Цикл сетов 1→10→1 по порядку строк
- [ ] ImageUrls: длинный cloud-api path=/AUTOZA/Foto_mebel_1/...
- [ ] ImageNames пусто
- [ ] Активные старые ID не тронуты
- [ ] unique firsts ≈ числу объявлений
```

### Структура папок

```text
{DISK_ROOT}/
  {niche}/                 # uslugi | kuhni | wardrobes | {slug}
    sets/set-01-{slug}/…
    heroes/{Id}.jpg
```

Смысл сетов (пример кухонь): фикс.цена, 3D24, студия, угловая, производство, потолок, модуль, без роста цены, под ключ, 2 м — см. план проекта `output/images/SETS-PLAN.md` если есть. При создании новых сетов с нуля — один approve смыслов сетов (не на каждую строку Excel).

### Алгоритм на строку Excel

1. Взять `Id`, `Title` (и при необходимости Description) с листа.
2. `set_index = (порядковый_номер_новой_строки - 1) % 10` → `set-01` … `set-10` по кругу.
3. **Фото 1 (lead):** из `raw-01-hero.jpg` оверлей по [references/overlay-hooks.md](references/overlay-hooks.md):
   - строка 1 = **хук** (search + pain/value из Title, 3–6 слов);
   - строка 2 = USP сета;
   - строка 3 = CTA из whitelist («Напишите — посчитаем» / «Напишите» / «Позвоните»);
   - сохранить в `{kind}/heroes/{Id}.jpg`.
4. **Фото 2–4:** `02-angle.jpg`, `03-detail.jpg`, `04-fomo.jpg` того же сета (общие файлы — ок).
5. При необходимости **5–10:** добор других ракурсов/сетов той же категории **без** повтора lead; уникальность наборов усиливать вариацией сета + hero.
6. Записать ImageUrls:

```text
https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/kuhni/heroes/{Id}.jpg | https://cloud-api.yandex.net/v1/disk/resources/download?path=/AUTOZA/Foto_mebel_1/kuhni/sets/set-01-fixcena/02-angle.jpg | .../03-detail.jpg | .../04-fomo.jpg
```

7. `ImageNames` = пусто.
8. Синхронизировать локальные `kuhni/`, `wardrobes/` на Диск в `/AUTOZA/Foto_mebel_1/...`.

Скрипт проекта (эталон): `scripts/build_ad_photos_and_urls.py`.  
Бэкап Excel перед записью: `output/backups/…-before-photos.xlsx`.

### Смысл кадров в сете

| # | Файл | Роль |
|---|------|------|
| 1 | hero (per-Id) | Обложка CTR: search + pain/value из строки |
| 2 | angle | Ракурс / планировка (warm-up) |
| 3 | detail | Фактура / фурнитура / стык (warm-up) |
| 4 | fomo | Мягкий CTA без бан-листа («Пришлите размеры», «Расчёт сегодня») |

---

## Режим A — только ссылки (без новой генерации)

Если кадры уже лежат на Диске и нужны только URL:

```
Task Progress:
- [ ] Папки EN, path ASCII
- [ ] Маппинг категория → папка по смыслу
- [ ] Новые ID: 4–10 URL, разные lead-фото
- [ ] Активные старые: ImageUrls не тронуты
- [ ] Длинный URL + ` | `; ImageNames пусто
- [ ] Нет одного first на всю категорию
```

1. Корень фото + Excel; **маппинг колонок по header row** (услуги: ImageUrls часто col 5, не 8).
2. RU-папки → EN.
3. Маппинг по смыслу (`kuhni`, `wardrobes`, …).
4. Новые строки: **разные** lead; предпочтительно `heroes/{Id}.jpg`, иначе цикл по файлам папки.
5. Статус **Активно** / не-новые ID — skip.
6. **Услуги** — ветка `uslugi/`; см. [references/services-photos.md](references/services-photos.md).
7. Проверка unique firsts.

Валидатор скилла: `scripts/validate_image_urls.py` (`--expect 4` или `10`).

---

## Режим B — генерация и оверлеи CTR

### Цель

Выше CTR обложки + проход модерации. После генерации — режим C или A.  
Для сильного визуала сетов — стили из [references/creative-direction.md](references/creative-direction.md) (без обязательного approve 3 вариантов на каждую строку).

### Выбор

| Задача | Режим |
|--------|--------|
| Есть сильный исходник | B1 оверлей |
| Нет фото / новый ракурс | B2 генерация 4:3 1920×1440 |
| Референс конкурента | реверс → промпт → B2 |
| Массовый фид 1000+ | сначала 10 сетов (B2+B1), потом режим C |
| 3 равносильные обложки + approve смыслов | **E**, не B |

### B1 — оверлей

1. Хук из строки объявления (**не** полный Title на hero) — [references/overlay-hooks.md](references/overlay-hooks.md) + [references/meaning-strategy.md](references/meaning-strategy.md).
2. Хук короткий + опц. выгода; без бан-листа.
3. Весь текст и плашка — **только внутри** safe-zone 1300×1300.
4. Площадь плашки+текста = **10–25%** кадра (типично 15–20% для мебели). Не тонкая полоска ~5–8%.
5. Кегль: хук ≥62 px @1920 (цель ≥72); проверка «с телефона».
6. Товар остаётся узнаваем; текст не закрывает весь фасад.
7. Сохранить: сет → `sets/...`; per-ad → `heroes/{Id}.jpg` → режим A/C.

### B2 — генерация

1. Промпт: товар в чистом интерьере, мягкий дневной свет, натуральные цвета, **4:3 1920×1440**, без watermark/лого/телефонов/баннера; оставить низ/центр под текст.
2. Сгенерировать; иначе — crop в 4:3 без stretch + лёгкая ЦК.
3. В EN-папку сета (`raw-01-hero.jpg` и ракурсы) → режим C.

**После AI-генерации (обязательно):** выход часто **не 4:3** (напр. 1536×1024). Center-crop до 4:3 → resize **1920×1440** (LANCZOS), без stretch.

### B2 — услуги: живой человек (не заглушка)

Для бухгалтерии, юристов, консалтинга, медицины и т.п.:

| Правило | Детали |
|---------|--------|
| **Лицо на кадре** | Hero и слайды 2–5 — **живой эксперт/лицо бренда**, не абстрактный фон |
| **Запрет** | PIL/gradient-only слайды **без людей** = брак (даже с CTR-текстом) |
| **Референс** | Фото клиента из брифа → `reference_image_paths` при генерации; сохранять узнаваемое лицо |
| **Стиль** | Мягкий дневной свет, офис/интерьер, «живое» фото, не stock-watermark |
| **Объект** | Человек **40–60%** кадра; текст в safe-zone, лицо не закрывать целиком |
| **PDF/референсы** | Если в PDF-сторитейле люди — в генерации **тоже люди**, не вырезать |
| **Identity** | Не менять лицо/тело; не деформировать под текст — [references/creative-direction.md](references/creative-direction.md) |

Подробности: [references/services-photos.md](references/services-photos.md), storyline: [references/storyline-sets.md](references/storyline-sets.md).

### Режим D — storyline sets (услуги, 3×5)

Когда в брифе **темы × слайды** (PDF-сторитейл), а не 10×4:

- **3–N тем** (`marketplaces`, `construction`, `general`…) × **4–5 кадров** (`01-hero` … `05-cta`)
- Тема строки — по keywords Title / winners-matrix / `theme` в report JSON
- **Hero per Id:** оверлей(hook + USP темы + CTA) поверх `01-hero` с человеком
- Имена файлов сета **1:1** с `THEME_SETS` в скрипте assign (напр. `02-report.jpg`, не `02-support.jpg`)
- ImageUrls: hero | 02…05 (без дубля 01-hero в хвосте)
- При создании **новой** theme set — один approve смыслов темы; дальше auto-хуки по строкам
- Единый Accent A / типографика warm-up внутри темы — [references/creative-direction.md](references/creative-direction.md)

При **перегенерации** фото: старые `cloud-api` URL с тем же `DISK_ROOT/{niche}/` — **заменить**, не только дописать (избежать дублей в ячейке).

**Смешанные URL:** если сохраняем старые `http://avito.ru/autoload/…` — валидатор скилла может ругаться; это **ок**, если сохранение старых фото намеренное.

---

## Режим E — Creative Art Direction (премиум)

Штучный / премиум путь: смыслы → approve → 3 обложки → карусель → **handoff в production**.

Подробности: [references/meaning-strategy.md](references/meaning-strategy.md), [references/creative-direction.md](references/creative-direction.md).

```
Task Progress:
- [ ] Текст объявления + число фото в карусели
- [ ] Анализ ЦА / боли / ценность / возражения
- [ ] Смыслы на каждый кадр (headline + submeaning) — ждать approve
- [ ] 3 standalone обложки 4:3 (Deep Contrast / Clean Minimalism / Dynamic Accent)
- [ ] Выбор направления → остальные слайды в одной visual system
- [ ] Только approved text; CTA whitelist
- [ ] Handoff: 1920×1440, safe-zone, бан-лист, path + ImageUrls
```

### Шаги

1. Запросить **текст объявления** и **число фото** в карусели (если не даны).
2. Краткий анализ: продукт/услуга, ЦА, боли, желания, возражения, главная ценность.
3. Написать смыслы на каждый кадр (обычно headline + submeaning) по [references/meaning-strategy.md](references/meaning-strategy.md). **Ждать approve / правки.**
4. Запросить **первое** исходное фото для обложки.
5. Внутри спланировать композиции; создать **3 отдельных** готовых обложки (не коллаж, не grid):
   - Deep Contrast
   - Clean Minimalism
   - Dynamic Accent  
   Все три равносильные; один стиль = один файл. Детали: [references/creative-direction.md](references/creative-direction.md).
6. **Ждать** выбор / правки направления обложки.
7. Запросить остальные исходники; map 1:1 на слайды 2…N.
8. Собрать внутренние слайды в **одной** системе (Accent A, типографика, calmer than cover); финальный CTA крупнее, но в той же системе.
9. На кадрах — **только** approved текст. CTA: «Напишите», «Позвоните», «Напишите в чат» (+ конкретная выгода первым шагом). Не писать «Напишите в Авито» / «Оставьте заявку».
10. **Handoff в production (обязательно):**
    - center-crop 4:3 → resize **1920×1440** (LANCZOS);
    - весь текст/плашка в safe-zone **1300×1300**; оверлей **10–25%**; бан-лист photos;
    - сохранить: `heroes/{Id}.jpg` + слайды в `sets/...` или `{niche}/premium/{Id}/01-cover.jpg` …;
    - ImageUrls длинным cloud-api, ` | `, ImageNames пусто;
    - unique firsts; активные ID не трогать без override.

Если пользователь прислал фото до approve смыслов — продолжать, но уточнить, что смыслы ведут дизайн.

---

## Режим F — архив ZIP + ImageNames

Когда бриф просит **загрузку фото архивом** (не Яндекс.Диск):

```
Task Progress:
- [ ] Плоский ZIP: фото в корне, без папок внутри
- [ ] Имена продуманы / пронумерованы (`{Id}-01.jpg` …)
- [ ] ImageNames: `file.jpg | …` (или перевод строки); ImageUrls пусто
- [ ] ZIP загружается вместе с Excel
- [ ] sizeof(zip) + sizeof(xlsx) ≤ 100 МБ
- [ ] unique firsts; активные не тронуты
```

Полные правила и антипаттерны ZIP: [references/archive-upload.md](references/archive-upload.md).

После B/C/E кадры можно отдать и через F (staging → плоский ZIP), если пользователь выбрал архив вместо URL.

---

### Запреты оверлея / модерация

- Контакты, QR, сайты, чужие стоки и логотипы
- Рамки, коллажи на обложку, watermark «для защиты»
- «Срочно», «акция», «скидка», «дёшево», «ЛУЧШИЕ», «№1», «100%», «Гарантия результата»
- Имитация UI Авито; один lead на все объявления; обещания вне текста
- Текст **мельче мобильной читаемости** или **вне** 1300×1300
- Оверлей **&lt;10%** «для модерации» ценой CTR — в этом пайплайне не делать
- Оверлей **&gt;25%** / полкадра текстом — баннер, риск модерации
- Три варианта обложки в **одном** файле (коллаж / contact sheet) — брак (режим E)

Галерея: обложка (уникальный hero) → ракурсы → детали → FOMO/CTA.  
Уникальность lead между объявлениями — обязательна.

---

## Связь с avito-factory

| Factory | Этот скилл |
|---------|------------|
| Excel / автозагрузка | Режим A / C / D |
| Этап фото / сеты | Режим B → C |
| Премиум креатив 1–N | Режим E → handoff A/C (или F) |
| Архив + ImageNames | Режим **F** |
| QA товарка | Не трогать фото старых активных |

Отчёт: путь Excel, N строк, unique firsts, размер кадров (1920×1440), корень Диска **или** путь ZIP + сумма МБ, число URL/имён на строку (4 или 10), папки EN; для E — выбранный стиль обложки.

## Pre-launch (перед автозагрузкой)

```
Task Progress:
- [ ] Способ фото: URL (Диск) **или** ZIP+ImageNames — не оба в одной строке
- [ ] Яндекс.Диск синхронизирован (локальная папка = path в URL) — если режим A/C/D
- [ ] disk_jpgs ≈ sets + heroes (проверка count на диске) — если URL
- [ ] ZIP плоский; ImageNames; архив+Excel ≤ 100 МБ — если режим F
- [ ] Кадры 1920×1440, 4:3; на услугах — люди на hero/слайдах
- [ ] Активные AvitoId: ImageUrls/ImageNames не менялись (или явный override в брифе)
- [ ] unique firsts ≈ числу объявлений на листе
```

См. [references/prelaunch-checklist.md](references/prelaunch-checklist.md).

## Дополнительно

- [references/meaning-strategy.md](references/meaning-strategy.md) — смыслы, mass auto vs E approve
- [references/creative-direction.md](references/creative-direction.md) — 3 стиля, карусель, identity
- [references/overlay-hooks.md](references/overlay-hooks.md) — хук + CTA, кегли, anti-patterns
- [references/services-photos.md](references/services-photos.md) — услуги / uslugi, живой эксперт
- [references/storyline-sets.md](references/storyline-sets.md) — режим D, 3×5, темы
- [references/yandex-disk-urls.md](references/yandex-disk-urls.md)
- [references/archive-upload.md](references/archive-upload.md) — режим F: ZIP + ImageNames, ≤100 МБ
- [references/ctr-overlays-4x3.md](references/ctr-overlays-4x3.md)
- [references/examples.md](references/examples.md)
- [references/sets-pipeline.md](references/sets-pipeline.md) — чеклист сетов + heroes
- [references/prelaunch-checklist.md](references/prelaunch-checklist.md) — перед запуском фида
- [references/rules-audit.md](references/rules-audit.md) — сверка источников правил
